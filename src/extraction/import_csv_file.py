import pandas as pd

class CSVImporter:
    def __init__(self):
        self.file_name = ""

    def import_csv(self, file_name):
        self.file_name = file_name
        try:
            df = pd.read_csv(self.file_name, low_memory=False)
            if df.empty:
                raise ValueError("The file is empty")
            return df
        except FileNotFoundError:
            raise FileNotFoundError("The file does not exist")
