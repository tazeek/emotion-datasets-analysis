# Website link: http://yanran.li/dailydialog
# Dataset: http://yanran.li/files/ijcnlp_dailydialog.zip
from io import BytesIO
import requests, zipfile

class DailydialogExtractor:

    def __init__(self) -> None:
        self._file_url = "http://yanran.li/files/ijcnlp_dailydialog.zip"
    
    def download_files(self) -> None:

        req = requests.get(self._file_url)
        print(req.content)

        zipfile= zipfile.ZipFile(BytesIO(req.content))
        zipfile.extractall(r'data/')

        return None