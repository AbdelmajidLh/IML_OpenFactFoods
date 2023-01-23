from typing import List

from cleaning.data_info import ExploratoryAnalysis
#from cleaning.filter_contract import FilterContractCleaning
#from cleaning.format_date import FormatDateCleaning
#from cleaning.format_numeric import FormatNumericCleaning
#from cleaning.remove_whitespace import RemoveWhitespaceCleaning
#from cleaning.order_data import OrderDataCleaning
#from cleaning.fill_nan import FillNanCleaning
#from cleaning.convert_ratio import ConvertRatioCleaning
from utils.pipeline import Pipeline

#from constants import ID_CONTRACT_COLUMNS


class CleaningPipeline(Pipeline):
    def __init__(self) -> None:
        Pipeline.__init__(self, [
            ExploratoryAnalysis()
            # FormatDateCleaning(),
            # FormatNumericCleaning(),
            # RemoveWhitespaceCleaning(),
            # ConvertRatioCleaning(),
            # FillNanCleaning(FILL_NAN_COLUMNS, 0.0),
            # OrderDataCleaning(ID_CONTRACT_COLUMNS)
        ])
