# Website link: http://yanran.li/dailydialog
# Dataset: http://yanran.li/files/ijcnlp_dailydialog.zip
# Parser reference: https://github.com/Sanghoon94/DailyDialogue-Parser/blob/master/parser.py

from io import BytesIO
import requests, zipfile

class DailydialogExtractor:

    def __init__(self) -> None:
        self._file_url = "http://yanran.li/files/ijcnlp_dailydialog.zip"
        self._data_dir = "dailydialog/data/"

    def _filter_files_zip(self, filename) -> bool:
        return filename.endswith(('txt','zip'))

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