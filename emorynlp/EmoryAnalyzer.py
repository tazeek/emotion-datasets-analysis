import json

class EmoryAnalyzer:

    def __init__(self):

        self._json_file = self._load_file
        pass

    def _load_file(self):
        filename = 'data_level0.json'
        f = open(filename)
        return json.load(f)