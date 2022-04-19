# Website link: http://yanran.li/dailydialog
# Dataset: http://yanran.li/files/ijcnlp_dailydialog.zip
# Parser reference: https://github.com/Sanghoon94/DailyDialogue-Parser/blob/master/parser.py

from io import BytesIO
from xmlrpc.client import Boolean
import requests, zipfile

class DailydialogExtractor:

    def __init__(self) -> None:
        self._file_url = "http://yanran.li/files/ijcnlp_dailydialog.zip"

    def _filter_files_zip(self, filename) -> Boolean:
        return filename.endswith(('txt','zip'))
    
    def download_files(self) -> None:

        req = requests.get(self._file_url)

        data_zip= zipfile.ZipFile(BytesIO(req.content))

        for file in data_zip.namelist():
            if self._filter_files_zip(file):
                print(file)
        #print(data_zip.namelist())
        #data_zip.extractall(r'dailydialog/')

        return None