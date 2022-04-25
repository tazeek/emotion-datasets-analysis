# Dataset location: https://github.com/declare-lab/RECCON/tree/main/data/original_annotation
# Raw data: https://github.com/declare-lab/RECCON/blob/main/data/original_annotation/dailydialog_test.json

class RecconExtractor:

    def __init__(self) -> None:
        self._files_list = ['dailydialog_test.json', 
        'dailydialog_train.json', 'dailydialog_valid.json', 'iemocap_test.json'
    ]