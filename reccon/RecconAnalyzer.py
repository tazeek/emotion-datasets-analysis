import json

class RecconAnalyzer:

    def __init__(self):
        self._json_file =self. _load_file()

        self._dataset_division = {
            'test': 0,
            'train': 1,
            'valid': 2,
        }

        # For finding the distribution of emotions
        self._emotion_counter = {}

        # For finding the types of cause, for emotions
        self._cause_type_counter = {}

    def _load_file(self) -> json:
        return json.load(open('data_level0.json',encoding="utf-8"))

    def _update_emotion_counter(self, emotion: str) -> None:
        self._emotion_counter[emotion] = self._emotion_counter.get(emotion, 0) + 1

        return None
    
    def _update_type_counter(self, type_list: list) -> None:
        for type in type_list:
            self._cause_type_counter[type] = self._cause_type_counter.get(type, 0) + 1

        return None
    
    def _parse_utterance_dict(self, utt_dict: dict) -> None:
        emotion = utt_dict.get("emotion", None)
        cause_type_list = utt_dict.get("type", ['empty'])

        self._update_emotion_counter(emotion)
        self._update_type_counter(cause_type_list)

        return None

    def fetch_cause_counts(self) -> dict:
        return self._cause_type_counter

    def fetch_emotion_counts(self) -> dict:
        return self._emotion_counter

    def fetch_raw_json(self) -> json:
        return self._json_file

    def fetch_partition_file(self, part: str) -> json:
        index =  self._dataset_division[part]
        return self._json_file[index]

    def perform_analysis(self, file: json) -> None:
        
        for key in file.keys():
            dialogue_set = file[key][0]

            for utterance_dict in dialogue_set:
                self._parse_utterance_dict(utterance_dict)
        
        return None
