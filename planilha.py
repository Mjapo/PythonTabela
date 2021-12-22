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

print("Exportando dataframe para o formato CSV")
dataframe.to_csv("arquivo_csv.csv")

print("exportando dataframe para o formato XLSX")
dataframe.to_excel("arquivo_excel.xlsx", sheet_name="sheet1")

print("Convertendo o dataframe para o formato JSON")
print(dataframe.to_json())
