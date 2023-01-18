import pandas as pd
import logging
from logger_setings import *
from pipelines.extraction import ExtractionPipeline
from constants import (
    zip_url_file
)

# download and import data
logger.debug("Extract data ...")
df = ExtractionPipeline().download_csv(zip_url_file)
print(df.head())