import json

class RecconAnalyzer:

    def __init__(self):
        self._json_file =self. _load_file()

        self._dataset_division = {
            'test': 0,
            'train': 1,
            'valid': 2,
        }

    def _load_file(self) -> json:
        return json.load(open('data_level0.json',encoding="utf-8"))
    
    def _parse_utterance_dict(self, utt_dict: dict) -> None:
        pass

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
