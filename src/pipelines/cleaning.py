import pandas as pd
from constants import (
    KEEP_COLS, DROP_NA_COLS, NEW_COLNAMES, DATE_COLS
)

class DataCleaning:
    def __init__(self, df):
        self.df = df
        self.KEEP_COLUMNS = KEEP_COLS
        self.DROP_COLS = DROP_NA_COLS
        self.NEW_COLNAMES = NEW_COLNAMES
        self.DATE_COLS = DATE_COLS
    
    def select_columns(self):
        self.df = self.df[self.KEEP_COLUMNS]
        return self.df
    
    def drop_missing_values(self):
        self.df = self.df.dropna(subset=self.DROP_COLS)
        return self.df
    
    def rename_columns(self):
        self.df = self.df.rename(columns=self.NEW_COLNAMES)
        return self.df
    
    def convert_date_columns(self):
        for col in self.DATE_COLS:
            self.df[col] = pd.to_datetime(self.df[col])
        return self.df
    
    def clean_data(self):
        self.select_columns()
        self.drop_missing_values()
        self.rename_columns()
        self.convert_date_columns()








#from typing import List

#from cleaning.data_info import ExploratoryAnalysis
#from cleaning.filter_contract import FilterContractCleaning
#from cleaning.format_date import FormatDateCleaning
#from cleaning.format_numeric import FormatNumericCleaning
#from cleaning.remove_whitespace import RemoveWhitespaceCleaning
#from cleaning.order_data import OrderDataCleaning
#from cleaning.fill_nan import FillNanCleaning
#from cleaning.convert_ratio import ConvertRatioCleaning
#from utils.pipeline import Pipeline

#from constants import ID_CONTRACT_COLUMNS


# class CleaningPipeline(Pipeline):
#     def __init__(self) -> None:
#         Pipeline.__init__(self, [
#             ExploratoryAnalysis()
#             # FormatDateCleaning(),
#             # FormatNumericCleaning(),
#             # RemoveWhitespaceCleaning(),
#             # ConvertRatioCleaning(),
#             # FillNanCleaning(FILL_NAN_COLUMNS, 0.0),
#             # OrderDataCleaning(ID_CONTRACT_COLUMNS)
#         ])
