import json

class EmoryAnalyzer:

    def __init__(self):

        self._json_file = self._load_file
        pass

    def _season_analysis(self):
        pass

    def _load_file(self):
        filename = 'data_level0.json'
        f = open(filename)
        return json.load(f)

    def _begin_analysis(self):

        for season in self._json_file:
            pass