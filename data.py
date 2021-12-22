import pandas as pd
import numpy as np
from pandas.core.construction import array
from pandas.core.frame import DataFrame

indice_datas = pd.date_range("20211207", periods=6)

print("Abaixo esta a estrutura que contem o indice das datas")
print(indice_datas)

array_aleatorio = np.empty((6,4), dtype=np.int32)
print("abaixo esta nosso array aleatorio que  representa os dados do dataframe")
print(array_aleatorio)

DataFrame = pd.DataFrame(array_aleatorio, index=indice_datas, columns=['A', 'B', 'C', 'D'])
print("abaixo esta nosso dataframe")
print(DataFrame)
