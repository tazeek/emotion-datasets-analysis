# Website link: http://yanran.li/dailydialog
# Dataset: http://yanran.li/files/ijcnlp_dailydialog.zip
# Parser reference: https://github.com/Sanghoon94/DailyDialogue-Parser/blob/master/parser.py

from io import BytesIO
import requests, zipfile

class DailydialogExtractor:

    def __init__(self) -> None:
        self._file_url = "http://yanran.li/files/ijcnlp_dailydialog.zip"
    
    def download_files(self) -> None:

        req = requests.get(self._file_url)

        data_zip= zipfile.ZipFile(BytesIO(req.content))
        print(data_zip)
        #data_zip.extractall(r'dailydialog/')

        return None