import json

class EmoryAnalyzer:

    def __init__(self):

        self._json_file = self._load_file()

        # Find all utterances
        self._utterance_list = []

        # Find length of utterance
        self._utterance_length = []

        # Find number of emotions
        self._emotion_count_dict = {}

        self._begin_analysis()

        return None

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
        
        tokenizer_help = lambda utter: utter.split(" ")

        for utterance_dict in utterances:

            utterance = utterance_dict.get('transcript', "")
            emotion = utterance_dict.get('emotion', ['none'])
            
            self._utterance_list += [utterance]

            # Extract utterances respective length
            self._utterance_length += [len(tokenizer_help(utterance))]

            # Extract the respective emotion per utterance
            self._emotion_count_dict[emotion] = \
                self._emotion_count_dict.get(emotion, 0) + 1

        return None

    def fetch_all_utterances(self) -> list:
        return self._utterance_list

    def fetch_utterances_length(self) -> list:
        return self._utterance_length