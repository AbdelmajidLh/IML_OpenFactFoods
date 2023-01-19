import pandas as pd
import logging
from logger_setings import *
from pipelines.extraction import GZFileDownloader
from pipelines.extraction import ExtractionPipeline
from constants import (
    zip_url_file, url
)

# download gz data
logger.debug("Downloading GZ file (big file ... please wait)")
#GZFileDownloader(url).download_and_uncompress()

# import csv file
logger.debug("Extract data ...")
#df = ExtractionPipeline().download_csv(url) { from zip file}
df = ExtractionPipeline().load_csv("en.openfoodfacts.org.products")
print(df.head())
print(df.shape)