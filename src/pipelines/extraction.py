import os
import zipfile
import urllib.parse
import urllib.request
import pandas as pd
from typing import Optional
from logger_setings import *
import gzip

from constants import (
    zip_url_file, url, RAW_DATA,
    ARCHIVE_DATA
)

# class pour telecharger et decompresser un fichier gz a partir d'un lien
#import urllib.request

class GZFileDownloaderPipeline:
    """
    Telecharger un fichier GZ et le decompresser
    Args : 
        url : le lien gz
        save_path [optional] : dossier pour les archives
        uncompressed_path [optional] : dossier pour les fichiers decompresses
    """
    def __init__(self, url, save_path, uncompressed_path):
        self.url = url
        self.save_path = save_path
        self.uncompressed_path = uncompressed_path
        self.file_name = os.path.basename(self.url)

    def download_and_uncompress(self):
        logger.debug("Downloading GZ file (big file ... please wait)")
        """Download the file if it does not exist"""
        if os.path.exists(f"{self.save_path}{self.file_name.split('.gz')[0]}"):
            print('File already exists')
        else:
            # Download the file from the URL
            urllib.request.urlretrieve(self.url, os.path.join(self.save_path, self.file_name))
            # Uncompress the file
            with gzip.open(os.path.join(self.save_path, self.file_name), 'rb') as f_in:
                with open(os.path.join(self.uncompressed_path, self.file_name.split(".gz")[0]), 'wb') as f_out:
                    f_out.write(f_in.read())
            os.remove(f"{self.save_path}{self.file_name}")
            print(f"{self.file_name} successfully downloaded and uncompressed!")
            logger.debug("successfully downloaded and uncompressed!")



# class pour telecharger, decompresser et importer un fichier zip (au format csv)
class ExtractionPipeline:
    """
    Class pour telecharger les fichiers zip a partir d'un lien, les decompresser puis importer le fichier csv
    Args :
        url : lien csv.zip
        file_name [optional]
    """
    def __init__(self):
        self.url = ""
        self.file_name = ""
        self.csvFile=""

    def download_csv(self, link):
        self.url = link
        self.file_name = link.split("/")[-1]
        raw_data_path = RAW_DATA
        if not os.path.exists(raw_data_path):
            os.makedirs(raw_data_path)
        with urllib.request.urlopen(self.url) as url:
            data = url.read()
            with open(f"{raw_data_path}/{self.file_name}", "wb") as f:
                f.write(data)

        with zipfile.ZipFile(f"{raw_data_path}/{self.file_name}", 'r') as zip_ref:
            zip_ref.extractall(raw_data_path)

        for file in os.listdir(raw_data_path):
            if file.endswith('.csv'):
                csv_file = file
                break
        os.remove(f"{raw_data_path}/{self.file_name}")
        df = pd.read_csv(f"{raw_data_path}/{csv_file}", low_memory=False)

    def load_csv(self, csvFile):
        self.raw_data_path = RAW_DATA
        self.file_name = csvFile
        mylist = []
        for chunk in  pd.read_csv(f"{self.raw_data_path}{self.file_name}.csv", \
            low_memory=False, sep='\t', chunksize=20000):
            mylist.append(chunk)
        df = pd.concat(mylist, axis= 0)
        del mylist
        return df