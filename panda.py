import pandas as pd
import numpy as np 

serie = pd.Series([1, 3, 5, 6, 9])
print("Essa é uma estrutura de series no pandas")
print(serie)

indice = np.array(['A', 'B,' 'C', 'D', 'E'])
serie = pd.Series([1, 3, 5, 6, 9], index=indice)
print("Essa é uma estrutura de serie com um indice nomeado no pandas")
print(serie)