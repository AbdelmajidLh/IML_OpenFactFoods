import pandas as pd
import logging
from logger_setings import *
from pipelines.extraction import GZFileDownloaderPipeline
from pipelines.extraction import ExtractionPipeline
#from pipelines.cleaning import CleaningPipeline
#from cleaning.data_info import ExploratoryAnalysis
from pipelines.cleaning import DataCleaningPipeline
from constants import (
    RAW_DATA, url, DATE_COLS
)

# download gz data
GZFileDownloaderPipeline(url=url, save_path=RAW_DATA, uncompressed_path=RAW_DATA).download_and_uncompress()

# import csv file
df_raw = ExtractionPipeline().load_csv("en.openfoodfacts.org.products")
print(df_raw.head())

# data exploration
# logger.debug("Start data exploration ")
# ExploratoryAnalysis(df_raw).run()

# data cleaning
# logger.debug("Start data cleaning ")
# df_clean = DataCleaningPipeline(df_raw).clean_data()
# del df_raw

# print(type(df_clean))