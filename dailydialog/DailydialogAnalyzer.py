

class DailydialogAnalyzer:

    def __init__(self):
        
        # For reading emotion labels
        self._emotion_labels_dict = self._read_label_file('dialogues_emotion.txt')

        # For reading annotation labels
        self._annotation_labels_dict = self._read_label_file('dialogues_act.txt')

        # For reading topic labels
        self._topic_labels_dict = self._read_label_file('dialogues_topic.txt')

        # For extracting dialogues
        self._dialogue_dict = self._read_dialogue_file('dialogues_text.txt')

        return

    def _read_label_file(self, label_file: str) -> dict:
        label_dict = {}
    
        with open(f"data\{label_file}") as file:
            for index, line in enumerate(file.readlines()):
                label_dict[index] = line.split()
                
        return label_dict

    def _read_dialogue_file(self, dialogue_file: str) -> dict:
        utterances_dict = {}
    
        with open(f"data\{dialogue_file}", encoding='utf8') as file:
            for index,line in enumerate(file.readlines()):
                line = line.replace('’',"'")
                utterances = line.split('__eou__')
                
                # Remove the '\n' character
                utterances.pop(-1)
                utterances_dict[index] = utterances
        
        return utterances_dict

    def _get_topic_mapping(self) -> dict:
        return {
            '1': 'Ordinary Life', '2': 'School Life', '3': 'Culture & Education',
            '4': 'Attitude & Emotion', '5': 'Relationship', '6': 'Tourism' , '7': 'Health', 
            '8': 'Work', '9': 'Politics', '10': 'Finance'
        }

    def _get_dialog_mapping(self) -> dict:
        return {
            '1': 'inform', '2': 'question', '3': 'directive', '4': 'commissive'
        }

    def _get_emotion_mapping(self) -> dict:
        return { 
            '0': 'no emotion', '1': 'anger', '2': 'disgust', '3': 'fear', 
            '4': 'happiness', '5': 'sadness', '6': 'surprise'
        }

    def get_topic_distribution(self) -> dict:

        mapper = self._get_topic_mapping()
        topic_counter = {}

        for label_num, topic_list in self._topic_labels_dict.items():
    
            # One dialogue only has one topic. Hence, access zero index
            topic = mapper[topic_list[0]]
            
            topic_counter[topic] = topic_counter.get(topic, 0) + 1
        
        return topic_counter

    def get_emotion_distribution(self) -> dict:

        mapper = self._get_emotion_mapping()
        emotion_counter = {}

        for label_num, emotion_list in self._emotion_labels_dict.items():
            emotion_list = [mapper[emotion] for emotion in emotion_list]
            
            for emotion in emotion_list:
                emotion_counter[emotion] = emotion_counter.get(emotion, 0) + 1
        
        return emotion_counter