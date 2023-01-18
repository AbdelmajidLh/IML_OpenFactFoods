import os
import zipfile
import urllib.request
import pandas as pd
#from constants import RAW_DATA

RAW_DATA = 'data/raw'

class CSVDownloader:
    def __init__(self):
        self.url = ""
        self.file_name = ""

    def download_csv(self, link):
        self.url = link
        self.file_name = link.split("/")[-1]
        raw_data_path = RAW_DATA
        if not os.path.exists(raw_data_path):
            os.makedirs(raw_data_path)
        urllib.request.urlretrieve(self.url, f"{raw_data_path}/{self.file_name}")

        with zipfile.ZipFile(f"{raw_data_path}/{self.file_name}", 'r') as zip_ref:
            zip_ref.extractall(raw_data_path)

        for file in os.listdir(raw_data_path):
            if file.endswith('.csv'):
                csv_file = file
                break
        os.remove(f"{raw_data_path}/{self.file_name}")
        df = pd.read_csv(f"{raw_data_path}/{csv_file}", low_memory=False)
        return df
