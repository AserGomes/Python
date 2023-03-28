import numpy
import pandas as pd
import numpy as np
import datetime
import requests
import io
import matplotlib
import matplotlib.pyplot as plt
import time
import mplfinance as mpl

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
data = r.content.decode('utf=8')
table = pd.read_csv(io.StringIO(data),names=['Alcohol','Malic_acid','Ash','Alcalinity_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','OD280/OD315_diluted_wines','Proline'])
df = pd.DataFrame(table)
df=df.reset_index(drop=True)
#https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.names
#https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
#https://archive.ics.uci.edu/ml/machine-learning-databases/wine/Index

#('Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline')

print(df)