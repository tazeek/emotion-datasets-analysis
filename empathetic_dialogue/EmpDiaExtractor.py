# Repository: https://github.com/facebookresearch/EmpatheticDialogues
# File location: https://dl.fbaipublicfiles.com/parlai/empatheticdialogues/empatheticdialogues.tar.gz

from io import BytesIO
import requests, zipfile

class EmpDiaExtractor:

    def __init__(self) -> None:
        self._file_url = "https://dl.fbaipublicfiles.com/parlai/empatheticdialogues/empatheticdialogues.tar.gz"
        self._data_dir = "empathetic-dialogue/data/"

    def _rename_file(self, file_fragment):
        return self._data_dir + file_fragment.filename.split('/')[-1]

    def download_files(self) -> None:

        req = requests.get(self._file_url)

        zip_file= zipfile.ZipFile(BytesIO(req.content))

        for file in zip_file.infolist():
            if self._filter_files_zip(file.filename):
                file.filename = self._rename_file(file)
                zip_file.extract(file)

        return None