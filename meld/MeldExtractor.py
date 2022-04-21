# Dataset: https://raw.githubusercontent.com/declare-lab/MELD/master/data/MELD/datasets.yaml
import requests

class MeldExtractor:

    def __init__(self) -> None:
        self._dataset_url = "https://raw.githubusercontent.com/declare-lab/MELD/master/data/MELD/datasets.yaml"

    def download_file(self) -> None:
        downloaded_file = requests.get(self._dataset_url).json()

        return None