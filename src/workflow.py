import pandas as pd
import logging
from logger_setings import *
from download.GzipDownloader import CSVDownloader
from constants import (
    zip_url_file
)

# download and import data
try:
    logger.debug("Try to Import data from : zip_url_file")
    downloader = CSVDownloader()
    df = downloader.download_csv("https://github.com/AbdelmajidLh/datasets/raw/main/en.openfoodfacts.org.products-df5.zip")
    print(df.head())
except Exception as e:
    logger.debug("data not imported")

logger.debug("without try")
downloader = CSVDownloader()
df = downloader.download_csv("https://github.com/AbdelmajidLh/datasets/raw/main/en.openfoodfacts.org.products-df5.zip")
print(df.head())