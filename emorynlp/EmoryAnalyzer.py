import json

class EmoryAnalyzer:

    def __init__(self):

        self._json_file = self._load_file

        self._episodes_per_season = []

        self._scenes_per_episode = []

        self._utterances_per_scene = []

        pass

    def _load_file(self):
        filename = 'data_level0.json'
        f = open(filename)
        return json.load(f)

    def _begin_analysis(self):

        for season in self._json_file:
            season_number = season['season_id']
            episodes = season['episodes']

            # Find number of episodes per season
            self._episodes_per_season += [len(episodes)]
            
            self._episode_analysis(episodes)

        return None

    def _season_analysis(self):
        pass

    def _episode_analysis(self, episodes: list):
        
        for episode in episodes:
            scenes = episode['scenes']

            # Find number of scenes per episode
            self._scenes_per_episode += [len(scenes)]

            self._scenes_analysis(scenes)


        return None

    def _scenes_analysis(self, scenes: list):
        
        for scene in scenes:
            utterances = scene['utterances']

            self._utterances_per_scene += [len(utterances)]

        return None

    def _utterance_analysis(self):
        pass