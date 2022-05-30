import json
import re
class MeldAnalyzer:

    def __init__(self) -> None:

        # Raw data
        self._json_file = None

        # Extract dialogues with the list of utterances (IDs only)
        self._dialogue_list = {}

        # Count number of emotions (per utterance)
        self._emotion_utterance = {}

        # Count number of sentiment (per utterance)
        self._sentiment_utterance = {}

        self._load_data()

        return None

    def _load_data(self) -> None:
        self._json_file = json.load(open('data_level0.json', encoding="utf8"))
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

    def _preprocess_utterance(self, utterance: str) -> str:
        utterance = utterance.replace("’","'")

        return utterance

    def _parse_by_utterance(self, file_dict: dict) -> None:
        emotion = file_dict['Emotion']
        sentiment = file_dict['Sentiment']
        utterance = self._preprocess_utterance(file_dict['Utterance'])

        self._emotion_utterance[emotion] = self._emotion_utterance.get(emotion, 0) + 1
        self._sentiment_utterance[sentiment] = self._sentiment_utterance.get(sentiment, 0) + 1
        
        return None

    def fetch_emotion_utterance(self) -> dict:
        return self._emotion_utterance
    
    def fetch_sentiment_utterance(self) -> dict:
        return self._sentiment_utterance
    
    def fetch_dialogue_utterance_list(self) -> dict:
        return self._dialogue_list.copy()

    def fetch_partitions_keys(self) -> list:
        return list(self._json_file.keys())

    def fetch_raw_data(self) -> json:
        return self._json_file

    def partition_file(self, key: str) -> json:
        return self._json_file[key]

    def analyze_partition(self, partition: json) -> None:
        
        # First: extract and sort the dialogues and utterances
        # This is because the dataset structure is messy
        self._extract_dialogues_utterances(partition)

        # Second: Loop through the partitioned dataset
        # Combination: Dialogue_id + "_" + Utterance_ID
        for dialogue_id, utterance_id_list in self._dialogue_list.items():

            # Third: Extract the utterance from the JSON file
            for id in utterance_id_list:
                full_id = dialogue_id + "_" + id
                utterance_dict = partition[full_id]

                self._parse_by_utterance(utterance_dict)

        return None