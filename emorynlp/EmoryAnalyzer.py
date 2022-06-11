import json

class EmoryAnalyzer:

    def __init__(self):

        self._json_file = self._load_file

        self._utterance_list = []

        pass

    def _load_file(self):
        filename = 'data_level0.json'
        f = open(filename)
        return json.load(f)

    def _begin_analysis(self) -> None:

        for season in self._json_file:
            episodes = season['episodes']
            
            self._episode_analysis(episodes)

        return None

    def _episode_analysis(self, episodes: list) -> None:
        
        for episode in episodes:
            scenes = episode['scenes']

            self._scenes_analysis(scenes)


        return None

    def _scenes_analysis(self, scenes: list) -> None:
        
        for scene in scenes:
            utterances = scene['utterances']

            self._utterance_analysis(utterances)

        return None

    def _utterance_analysis(self, utterances: list) -> None:
        
        for utterance in utterances:

            # Extract utterance via 'transcript' key
            self._utterance_list += [utterance['transcript']]

        return None