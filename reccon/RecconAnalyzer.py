import json
from urllib.parse import _NetlocResultMixinStr

class RecconAnalyzer:

    def __init__(self, partition_name: str):
        self._json_file =self. _load_file()

        self._dataset_division = {
            'test': 0,
            'train': 1,
            'valid': 2,
        }

        # For finding the distribution of emotions (per utterance)
        self._emotion_counter = {}

        # For finding the types of cause, for emotions (per utterance)
        self._cause_type_counter = {}

        # Find the number of tokens (per utterance)
        self._token_counts = []

        # Find the number of tokens (per emotion)
        self._emotion_token_counts = {}

        # Find the number of utterances (per dialogue)
        self._utt_per_diag_counter = []

        # Find the number of tokens (per dialogue)
        self._token_counts_per_diag = []

        # Find the given emotions for dialog length (per dialog)
        self._dialog_len_emotions = {
            'even': {},
            'odd': {}
        }

        # Find emotion shift counts (per dialog)
        self._emotion_shift_counts = []

        # Find turn number(s) count of emotion cause (per dialog)
        self._emotion_turn_cause = {}

        # Find dialog length per emotion shift (per dialog)
        self._dialog_length_emotion_shift = {}

        # Find pairwise checks between emotion causes (per dialog)
        self._pairwise_emotions = {
            'same_emotion': 0,
            'different_emotion': 0
        }

        # Find checks between sentiment-level of emotion causes (per dialog)
        self._pairwise_sentiment = {
            'same_sentiment': 0,
            'different_sentiment': 0
        }

        # Begin Analysis
        file = self._fetch_partition_file(partition_name)
        self._perform_analysis(file)

        return None

    def _fetch_partition_file(self, part: str) -> json:
        index =  self._dataset_division[part]
        return self._json_file[index]

    def _load_file(self) -> json:
        return json.load(open('data_level0.json',encoding="utf-8")) 

    def _update_utt_counter(self, utter_len: int) -> None:
        self._token_counts += [utter_len]

        return None

    def _update_emotion_counter(self, emotion: str) -> None:
        self._emotion_counter[emotion] = self._emotion_counter.get(emotion, 0) + 1

        return None

    def _update_emotion_token_counter(self, emotion: str, token_length: int) -> None:
        self._emotion_token_counts[emotion] = \
            self._emotion_token_counts.get(emotion, [token_length]) + [token_length]
        
        return None
    
    def _update_type_counter(self, type_list: list) -> None:
        for type in type_list:
            self._cause_type_counter[type] = self._cause_type_counter.get(type, 0) + 1

        return None

    def _tokenize_utterance(self, utterance: str) -> list:
        return utterance.split(" ")
    
    def _update_utter_diag_counter(self, utter_list: list) -> None:
        self._utt_per_diag_counter += [len(utter_list)]

        return None

    def _update_tokens_per_diag(self, dialog_list: list) -> None:
      
      # Extract the utterances
      utterance_list = [utt_dict.get("utterance", "") for utt_dict in dialog_list]

      # Lambda function for getting overall length of utterances
      lambda_fun = lambda utt: len(self._tokenize_utterance(utt))

      # Get the total summation
      total_length = sum(lambda_fun(utt) for utt in utterance_list)
      self._token_counts_per_diag += [total_length]

      return None 

    def _update_dialog_len_emotion(self, dialog_list: list) -> None:
        
        # Get number of utterances
        num_utterances = len(dialog_list)

        # Get all the emotions in the dialog
        emotions_list = [utt.get('emotion', "") for utt in dialog_list]

        even_or_odd = 'even' if num_utterances % 2 == 0 else 'odd'

        # Increment dictionary
        for emotion in emotions_list:
            
            self._dialog_len_emotions[even_or_odd][emotion] = \
                self._dialog_len_emotions[even_or_odd].get(emotion, 0) + 1

        return None

    def _update_emotion_shift_counts(self, dialog_list: list) -> None:

        # Get all the emotions
        emotions_list = [utt.get('emotion', "") for utt in dialog_list]

        current_emotion = emotions_list[0]

        # Loop through one emotion at a time
        emotion_shifts_count = 0

        for emotion in emotions_list:
            
            # Emotion shift happens here
            if emotion != current_emotion:
                emotion_shifts_count += 1
                current_emotion = emotion
        
        self._emotion_shift_counts += [emotion_shifts_count]
        return None

    def _update_emotion_turn_cause_counts(self, dialog_list: list) -> None:

        helper_lambda = lambda utt: utt.get('expanded emotion cause evidence', [])

        # Extract the turn cause via key 'expanded emotion cause evidence'
        emotion_cause_turn_lists = [helper_lambda(utt) for utt in dialog_list]
        turn_numbers = [utt.get('turn','0') for utt in dialog_list]

        for turn_number, cause_list in zip(turn_numbers, emotion_cause_turn_lists):

            # List is empty
            if len(cause_list) == 0:
                continue
            
            for cause in cause_list:

                # Latent emotions are labeled as "b"
                # These are utterances, where the cause is in the future utterance(s)
                if cause == 'b':
                    self._emotion_turn_cause['latent'] = \
                        self._emotion_turn_cause.get('latent', 0) + 1
                else:
                    difference = turn_number - cause

                    if difference < 0:
                        print(dialog_list)
                        print("\n")
                    self._emotion_turn_cause[difference] = \
                        self._emotion_turn_cause.get(difference, 0) + 1

        return None

    def _parse_dialog_dict(self, dialog_list: list) -> None:
        self._update_utter_diag_counter(dialog_list)
        self._update_tokens_per_diag(dialog_list)
        self._update_dialog_len_emotion(dialog_list)
        self._update_emotion_shift_counts(dialog_list)
        self._update_emotion_turn_cause_counts(dialog_list)

        return None
    
    def _parse_utterance_dict(self, utt_dict: dict, total_tokens_list: list) -> None:
        emotion = utt_dict.get("emotion", None)
        cause_type_list = utt_dict.get("type", ['empty'])
        utterance = utt_dict.get("utterance", "")

        utterance_tokens = self._tokenize_utterance(utterance)
        utter_len = len(utterance_tokens)

        # Count number of tokens
        total_tokens_list += [utter_len]

        # Update respective functions (per utterance)
        self._update_emotion_counter(emotion)
        self._update_type_counter(cause_type_list)
        self._update_utt_counter(utter_len)
        self._update_emotion_token_counter(emotion, utter_len)

        return None

    def _perform_analysis(self, file: json) -> None:
        
        for key in file.keys():
            dialogue_set = file[key][0]
            total_tokens_list = []

            # Update respective functions (per dialogue)
            self._parse_dialog_dict(dialogue_set)

            for utterance_dict in dialogue_set:
                # Update respective functions (per utterance)
                self._parse_utterance_dict(utterance_dict, total_tokens_list)
        
        return None

    def fetch_cause_counts(self) -> dict:
        return self._cause_type_counter

    def fetch_emotion_counts(self) -> dict:
        return self._emotion_counter

    def fetch_raw_json(self) -> json:
        return self._json_file

    def fetch_utter_diag_counts(self) -> list:
        return self._utt_per_diag_counter

    def fetch_token_counter(self) -> list:
        return self._token_counts

    def fetch_token_counts_diag(self) -> list:
        return self._token_counts_per_diag

    def fetch_token_counts_emotion(self) -> dict:
        return self._emotion_token_counts

    def fetch_emotion_dialog_len(self) -> dict:
        return self._dialog_len_emotions

    def fetch_emotion_shift_counts(self) -> list:
        return self._emotion_shift_counts

    def fetch_emotion_turn_causes(self) -> dict:
        return self._emotion_turn_cause.copy()
