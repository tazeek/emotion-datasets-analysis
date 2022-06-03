

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

    def topic_mapping() -> dict:
        return {
            '1': 'Ordinary Life', '2': 'School Life', '3': 'Culture & Education',
            '4': 'Attitude & Emotion', '5': 'Relationship', '6': 'Tourism' , '7': 'Health', 
            '8': 'Work', '9': 'Politics', '10': 'Finance'
        }

    def dialog_mapping() -> dict:
        return {
            '1': 'inform', '2': 'question', '3': 'directive', '4': 'commissive'
        }

    def emotion_mapping() -> dict:
        return { 
            '0': 'no emotion', '1': 'anger', '2': 'disgust', '3': 'fear', 
            '4': 'happiness', '5': 'sadness', '6': 'surprise'
        }