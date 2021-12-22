import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20210101"),
        "C": pd.Series([1.2, 3.7, 5.5, 6], dtype="float32"),
        "D": np.array([12,5,6,9], dtype="int32"),
        "E": pd.Categorical(["novo", "usado", "usado", "novo"])
    }
)
print("Abaixo esta a parte de cima do nosso dataframe")
print(dataframe.head())

print("abaixo esta a parte  de baixo do nosso dataframe")
print(dataframe.tail(2))

print("abaixo estão os indices do nosso dataframe")
print(dataframe.index)

print("abaixo estão as colunas do nosso dataframe")
print(dataframe.columns)

print("abaixo esta nosso dataframe convertido para um array numpy")
print(dataframe.to_numpy())

print("abaixo estão estatisticas basicas dobre nosso dataframe")
print(dataframe.describe())

print("abaixo esta nosso dataframe ordenado por uma coluna")
print(dataframe.sort_values(by="D"))

