import pandas as pd 
import numpy as np
from pandas.core.arrays.categorical import Categorical 

dataframe = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20210101"),
        "C": pd.Series([1.2, 3.7, 5.5, 6], dtype="float32"),
        "D": np.array([12,5,6,9], dtype="int32"),
        "E": pd.Categorical(["novo", "usado", "usado", "novo"])
    }
)

print("abaixo esta nosso dataframe constuido a partir de um dicionario")
print(dataframe)