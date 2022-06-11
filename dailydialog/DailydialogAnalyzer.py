

class DailydialogAnalyzer:

    def __init__(self):
        
        # For reading emotion labels
        self._emotion_labels_dict = self._read_label_file('dialogues_emotion.txt')
        self._emotion_counts = {}

        # For reading annotation labels
        self._annotation_labels_dict = self._read_label_file('dialogues_act.txt')
        self._annotation_counts = {}

        # For reading topic labels
        self._topic_labels_dict = self._read_label_file('dialogues_topic.txt')
        self._topic_counts = {}

        # For extracting dialogues
        self._dialogue_dict = self._read_dialogue_file('dialogues_text.txt')

        # Find number of utterances (per dialog)
        self._utterance_num_dialog = []

        # Find length of utterance (overall)
        self._utterance_length = []

        # Find length of full dialog (per dialog)
        self._dialog_length = []

        # Perform analysis
        self._perform_analysis()

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

    def _tokenisation_utterance(self, utterance: str) -> list:
        return [word for word in utterance.split(" ") if word != '']

    def _extract_topic_distribution(self) -> None:

        mapper = self._get_topic_mapping()

        for label_num, topic_list in self._topic_labels_dict.items():
    
            # One dialogue only has one topic. Hence, access zero index
            topic = mapper[topic_list[0]]
            
            self._topic_counts[topic] = self._topic_counts.get(topic, 0) + 1
        
        return None

    def _extract_emotion_distribution(self) -> None:

        mapper = self._get_emotion_mapping()

        for label_num, emotion_list in self._emotion_labels_dict.items():

            for emotion in emotion_list:
                emotion = mapper[emotion]

                self._emotion_counts[emotion] = self._emotion_counts.get(emotion, 0) + 1
                
        
        return None
    
    def _extract_annotation_distribution(self) -> None:

        mapper = self._get_dialog_mapping()

        for label_num, annotation_list in self._annotation_labels_dict.items():

            for annotation in annotation_list:
                annotation = mapper[annotation] 

                self._annotation_counts[annotation] = \
                    self._annotation_counts.get(annotation, 0) + 1
                
        
        return None

    def _extract_utterances_per_dialog(self) -> None:
        self._utterance_num_dialog = \
            [len(dialog) for index, dialog in self._dialogue_dict]

        return None

    def _extract_utterance_length(self) -> None:
        
        for index, utterances in self._dialog_dict:

            utterances_length_list = [len(utterance) for utterance in utterances]

            # For utterance length (individual)
            self._utterance_length += [utterances_length_list]

            # For length of dialog
            self._dialog_length += [sum(utterances_length_list)]

        return None

    def _perform_analysis(self) -> None:
        
        self._extract_annotation_distribution()
        self._extract_emotion_distribution()
        self._extract_topic_distribution()
        self._extract_utterances_per_dialog()
        self._extract_utterance_length()

        return None

    def fetch_topic_distribution(self) -> dict:
        return self._topic_counts

    def fetch_emotion_distribution(self) -> dict:
        return self._emotion_counts

    def fetch_annotation_distribution(self) -> dict:
        return self._annotation_counts

    def fetch_dialog_length(self) -> list:
        return self._utterance_num_dialog

    def parse_utterances(self) -> list:
        utterance_length_list = []

        for index, dialog in self._annotation_labels_dict.items():

            for utterance in dialog:
                utterance_length_list += self._tokenisation_utterance(utterance)
        
        return utterance_length_list
