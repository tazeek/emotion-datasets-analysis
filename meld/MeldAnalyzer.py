import json
import re
class MeldAnalyzer:

    def __init__(self, partition_file: str) -> None:

        # Raw data
        self._json_file = None

        # Extract dialogues with the list of utterances (IDs only)
        self._dialogue_list = {}

        # Count number of emotions (per utterance)
        self._emotion_utterance = {}

        # Count number of sentiment (per utterance)
        self._sentiment_utterance = {}

        # Count number of tokens (per utterance)
        self._tokens_utterance = []

        # Count number of emotions per sentiment (per utterance)
        self._emotions_per_sentiment = {
            'positive': {},
            'negative': {},
            'neutral': {}
        }

        # Find number of speakers (per dialog)
        self._speakers_count = []

        # Find utterance length for emotion (per utterance)
        self._utterance_emotion_len = {}

        # Find total length of dialog (per dialog)
        self._dialog_length = []

        # Load and partition first
        self._load_data()
        self._partition_file = self._get_partition_file(partition_file)

        # Perform Analysis
        self._analyze_partition()

        return None

    def _get_partition_file(self, key: str) -> json:
        return self._json_file[key]

    def _load_data(self) -> None:
        self._json_file = json.load(open('data.json', encoding="utf8"))
        return None

    def _sort_utterance_list(self, utterance_list: list['str']) -> list['str']:

        # Motivation: https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
        # Utterance IDs are not ordered properly (Utt0, Utt1, Utt10, Utt11, Utt2)
        # Hence, the sequence is broken from the beginning

        # Check if there are any number or not
        convert = lambda text: int(text) if text.isdigit() else text

        # Extract the number from string by using regex
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]

        # Sort the list
        utterance_list.sort(key = alphanum_key)

        return utterance_list

    def _extract_dialogues_utterances(self, data: json) -> None:
        for dialogue_utterance in data:
            dialog_num, utterance_num = dialogue_utterance.split("_")
            
            self._dialogue_list[dialog_num] = \
                self._dialogue_list.get(dialog_num, []) + [utterance_num]

        # Now sort the utterance order per dialogue
        for dialogue, utterance_list in self._dialogue_list.items():
            self._dialogue_list[dialogue] = self._sort_utterance_list(utterance_list)

        return None

    def _update_emotion_sentiment(self, emotion: str, sentiment: str) -> None:
        self._emotions_per_sentiment[sentiment][emotion] = \
            self._emotions_per_sentiment[sentiment].get(emotion, 0) + 1
        
        return None
    
    def _update_emotion_utterance_len(self, emotion: str, utterance_len: int) -> None:

        if self._utterance_emotion_len.get(emotion, None):
            self._utterance_emotion_len[emotion] += [utterance_len]
        else:
            self._utterance_emotion_len[emotion] = [utterance_len]
        
        return None

    def _update_speaker_count(self, utterances: list) -> None:
        
        # Get all the speakers
        speakers_list = {utterance['Speaker'] for utterance in utterances}

        # Add to attribute list
        self._speakers_count += [len(speakers_list)]

        return None

    def _update_dialog_len(self, utterances: list) -> None:
        
        # Capture and preprocess utterance
        helper = lambda utt: self._preprocess_utterance(utt)
        all_utterances = [helper(utterance['Utterance']) for utterance in utterances]

        # Find the total length
        total_len = sum(len(utterance.split(" ")) for utterance in all_utterances)

        self._dialog_length += [total_len]

        return None

    def _preprocess_utterance(self, utterance: str) -> str:
        utterance = utterance.replace("’","'")

        return utterance

    def _extract_utterances(self, dialog_id, utt_id_list: list) -> list:

        # Get all the IDs associated with given dialog
        dialog_utt_ids = [dialog_id + '_' + id for id in utt_id_list]

        # Extract all the utterances
        return [self._partition_file[id] for id in dialog_utt_ids]

    def _parse_by_dialog(self, utterance_list: list) -> None:

        # Extract the relevant data
        self._update_speaker_count(utterance_list)
        self._update_dialog_len(utterance_list)
        
        return None

    def _parse_by_utterance(self, file_dict: dict) -> None:
        emotion = file_dict['Emotion']
        sentiment = file_dict['Sentiment']
        utterance = self._preprocess_utterance(file_dict['Utterance'])

        utterance_tokens = utterance.split(" ")

        self._emotion_utterance[emotion] = self._emotion_utterance.get(emotion, 0) + 1
        self._sentiment_utterance[sentiment] = self._sentiment_utterance.get(sentiment, 0) + 1
        self._tokens_utterance += [len(utterance_tokens)]

        self._update_emotion_sentiment(emotion, sentiment)
        self._update_emotion_utterance_len(emotion, len(utterance_tokens))
        
        return None
    
    def _analyze_partition(self) -> None:
        
        # First: extract and sort the dialogues and utterances
        # This is because the dataset structure is messy
        self._extract_dialogues_utterances(self._partition_file)

        # Second: Loop through the partitioned dataset
        # Combination: Dialogue_id + "_" + Utterance_ID
        for dialogue_id, utterance_id_list in self._dialogue_list.items():

            # Parsing dialog level
            utterance_list = self._extract_utterances(dialogue_id, utterance_id_list)
            self._parse_by_dialog(utterance_list)

            # Third: Extract the utterance from the JSON file
            for utterance in utterance_list:

                # Parsing utterance level
                self._parse_by_utterance(utterance)

        return None

    def fetch_emotion_utterance(self) -> dict:
        return self._emotion_utterance
    
    def fetch_sentiment_utterance(self) -> dict:
        return self._sentiment_utterance
    
    def fetch_dialogue_utterance_list(self) -> dict:
        return self._dialogue_list.copy()

    def fetch_token_length_utterances(self) -> list:
        return self._tokens_utterance

    def fetch_partitions_keys(self) -> list:
        return list(self._json_file.keys())

    def fetch_raw_data(self) -> json:
        return self._json_file

    def fetch_speakers_count(self) -> dict:
        return self._speakers_count

    def fetch_emotions_sentiment(self) -> dict:
        return self._emotions_per_sentiment

    def fetch_emotions_utterance_len(self) -> dict:
        return self._utterance_emotion_len

    def fetch_dialog_length(self) -> list:
        return self._dialog_length