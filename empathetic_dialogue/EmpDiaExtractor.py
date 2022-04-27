# Repository: https://github.com/facebookresearch/EmpatheticDialogues
# File location: https://dl.fbaipublicfiles.com/parlai/empatheticdialogues/empatheticdialogues.tar.gz

from io import BytesIO
import requests, tarfile

class EmpDiaExtractor:

    def __init__(self) -> None:
        self._file_url = "https://dl.fbaipublicfiles.com/parlai/empatheticdialogues/empatheticdialogues.tar.gz"
        self._data_dir = "empathetic_dialogue/data/"
        self._csv_files = ['empatheticdialogues/test.csv', 
            'empatheticdialogues/train.csv', 'empatheticdialogues/valid.csv']
    
    def _filter_files_zip(self, filename) -> bool:
        return filename.endswith(('csv'))

    def _rename_file(self, file_fragment):
        return self._data_dir + file_fragment.name.split('/')[-1]

    def download_files(self) -> None:

        req = requests.get(self._file_url, stream=True)
        file_list = tarfile.open(fileobj=req.raw, mode="r|gz")

        file_list.extractall(self._data_dir)

        return None