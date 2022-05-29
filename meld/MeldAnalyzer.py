import json

class MeldAnalyzer:

    def __init__(self):
        self._json_file = None

    def _load_data(self) -> None:
        self._json_file = json.load(open('data_level0.json', encoding="utf8"))
        return None

    def extract_partitions(self):
        return self._json_file.keys()