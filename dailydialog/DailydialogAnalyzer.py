

class DailydialogAnalyzer:

    def __init__(self):
        
        # For reading emotion labels
        self._emotion_labels_dict = self._read_label_file('dialogues_emotion.txt')

        # For reading annotation labels
        self._annotation_labels_dict = self._read_label_file('dialogues_act.txt')

        # For reading topic labels
        self._topic_labels_dict = self._read_label_file('dialogues_topic.txt')

        return

    def _read_label_file(self, label_file: str) -> dict:
        label_dict = {}
    
        with open(f"data\{label_file}") as file:
            for index, line in enumerate(file.readlines()):
                label_dict[index] = line.split()
                
        return label_dict