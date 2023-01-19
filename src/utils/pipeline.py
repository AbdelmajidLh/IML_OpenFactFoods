import pandas as pd
from typing import List

from utils.transformer import Transformer


class Pipeline(Transformer):
    def __init__(self, transformers: List[Transformer]) -> None:
        super().__init__()
        self.transformers = transformers

    def transform(self, df_to_transform: pd.DataFrame) -> pd.DataFrame:
        df = df_to_transform.copy()
        for transformer in self.transformers:
            df = transformer.transform(df)
        return df