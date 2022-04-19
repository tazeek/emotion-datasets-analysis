# Repository of file: https://github.com/emorynlp/character-mining/tree/master/json
# Example of raw file: https://raw.githubusercontent.com/emorynlp/character-mining/master/json/friends_season_01.json

import requests
import json

class EmoryExtractor:

    def __init__(self) -> None:
        self._files_list = []
        self._total_files = 10
        self._file_name = "friends_season"
        self._url_json = "https://raw.githubusercontent.com/emorynlp/character-mining/master/json/"

        return None

    def _prepare_url(self, index):
        """
            Prepare the filename to be added to the end of the URL
            Filename example: friends_season_01.json
        """

        file_num = ""

        if index < 10:
            file_num += "0"
        
        file_num += str(index)

        return self._url_json + f"{self._file_name}_{file_num}.json"

    def download_files(self):
        """
            Downloads the JSON files, converts to a dictionary, and stores in a list.
            This is done for all 10 files (file count as at 19/04/2022)
        """

        for i in range(self._total_files + 1):
            url = self._prepare_url(i)
            extracted_json = requests.get(url).json()
            self._files_list.append(extracted_json)

        return None