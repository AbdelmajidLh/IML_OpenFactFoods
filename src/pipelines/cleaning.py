import pandas as pd
from typing import Optional
from constants import (
    KEEP_COLS, 
    DROP_NA_COLS, 
    NEW_COLNAMES, 
    DATE_COLS
)

class DataCleaningPipeline:
    def __init__(self, df) -> pd.DataFrame:
        self.df = df
        self.KEEP_COLUMNS = KEEP_COLS
        self.DROP_COLS = DROP_NA_COLS
        self.NEW_COLNAMES = NEW_COLNAMES
        self.DATE_COLS = DATE_COLS
    
    def select_columns(self) -> pd.DataFrame:
        self.df = self.df[self.KEEP_COLUMNS]
        print('select column df shape :', self.df.shape)
        return self.df
    
    def drop_missing_values(self) -> pd.DataFrame:
        self.df = self.df.dropna(subset=self.DROP_COLS)
        print('drop_missing_values df shape :', self.df.shape)
        return self.df
    
    def rename_columns(self) -> pd.DataFrame:
        self.df = self.df.rename(columns=self.NEW_COLNAMES)
        print('rename_columns df shape :', self.df.shape)
        print('new columns', self.df.columns)
        return self.df
    
    def convert_date_columns(self) -> pd.DataFrame:
        for col in self.DATE_COLS:
            self.df[col] = pd.to_datetime(self.df[col])
            print('convert_date_columns df shape :', self.df.shape)

        return self.df
    
    def clean_data(self):
        self.select_columns()
        self.drop_missing_values()
        self.rename_columns()
        self.convert_date_columns()
    
        return self.df








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
