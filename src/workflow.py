import pandas as pd
import logging
from logger_setings import *
from pipelines.extraction import ExtractionPipeline
#from pipelines.cleaning import CleaningPipeline
from cleaning.data_info import ExploratoryAnalysis
from pipelines.cleaning import DataCleaningPipeline
from constants import (
    zip_url_file, url, DATE_COLS
)

# download gz data
#logger.debug("Downloading GZ file (big file ... please wait)")
#GZFileDownloader(url).download_and_uncompress()

# import csv file
logger.debug("Extract data ...")
df_raw = ExtractionPipeline().load_csv("en.openfoodfacts.org.products")

# data exploration
logger.debug("Start data exploration ")
ExploratoryAnalysis(df_raw).run()

# data cleaning
logger.debug("Start data cleaning ")
df_clean = DataCleaningPipeline(df_raw).clean_data()
del df_raw

print(type(df_clean))