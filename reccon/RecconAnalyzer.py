import json

class RecconAnalyzer:

    def __init__(self):
        self._json_file =self. _load_file()

        self._dataset_division = {
            'test': 0,
            'train': 1,
            'valid': 2,
        }

    def _load_file(self):
        return json.load(open('data_level0.json',encoding="utf-8"))

    def fetch_raw_json(self) -> json:
        return self._json_file
