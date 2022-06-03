

class DailydialogAnalyzer:

    def __init__(self):
        pass

    def _read_label_file(self, label_file: str) -> dict:
        label_dict = {}
    
        with open(f"data\{label_file}") as file:
            for index, line in enumerate(file.readlines()):
                label_dict[index] = line.split()
                
        return label_dict