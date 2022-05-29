import json

class MeldAnalyzer:

    def __init__(self) -> None:

        # Raw data
        self._json_file = None
        self._dialogue_list = {}

        self._load_data()

        return None

    def _load_data(self) -> None:
        self._json_file = json.load(open('data_level0.json', encoding="utf8"))
        return None

    def _extract_dialogues_utterances(self, data: json) -> None:
        for dialogue_utterances in data:

        return None

    def fetch_partitions_keys(self) -> list:
        return list(self._json_file.keys())

    def fetch_raw_data(self) -> json:
        return self._json_file

    def partition_file(self, key: str) -> json:
        return self._json_file[key]

    def analyze_partition(self, partition: json) -> None:
        
        # First: extract and sort the dialogues and utterances
        # This is because the dataset structure is messy
        return None