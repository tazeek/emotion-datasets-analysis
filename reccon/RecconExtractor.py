# Dataset location: https://github.com/declare-lab/RECCON/tree/main/data/original_annotation
# Raw data: https://raw.githubusercontent.com/declare-lab/RECCON/main/data/original_annotation/dailydialog_test.json
import requests
import json

class RecconExtractor:

    def __init__(self) -> None:
        self._files_list = ['dailydialog_test.json', 
            'dailydialog_train.json', 'dailydialog_valid.json'#, 'iemocap_test.json'
        ]

        self._files_list = []
        self._json_url = 'https://raw.githubusercontent.com/declare-lab/RECCON/main/data/original_annotation/'

    def _prepare_url(self, file_name) -> str:

        return self._json_url + file_name

    def _save_file(self, filename) -> None:
        with open(filename, 'w') as file:
            json.dump(self._files_list, file, indent=4)

        return None

    def download_files(self) -> None:

        for file in self._files_list:
            url = self._prepare_url(file)
            extracted_json = requests.get(url).json()
            self._files_list.append(extracted_json)

        self._save_file('reccon/data_level0.json')

        return None