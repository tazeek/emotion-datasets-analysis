# Dataset location: https://github.com/declare-lab/RECCON/tree/main/data/original_annotation
# Raw data: https://raw.githubusercontent.com/declare-lab/RECCON/main/data/original_annotation/dailydialog_test.json

class RecconExtractor:

    def __init__(self) -> None:
        self._files_list = ['dailydialog_test.json', 
            'dailydialog_train.json', 'dailydialog_valid.json'#, 'iemocap_test.json'
        ]

        self._json_url = 'https://raw.githubusercontent.com/declare-lab/RECCON/main/data/original_annotation/'

    def _prepare_url(self, file_name) -> str:

        return self._json_url + file_name

    def download_files(self) -> None:

        for file in self._files_list:
            url = self._prepare_url(file)
            print(url)

        return None