import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

CURRENT_DIRECTORY = os.getcwd()
pd.set_option('display.width', 300)
np.set_printoptions(linewidth=300)
pd.set_option('display.max_columns',10)



lm = LinearRegression()



df = pd.read_excel('Data/data_combined.xlsx')
print(df.head())

X = df[['AI_patents_WW']]
Y = df['value_worldwide[bil.USD]']

sns.regplot('AI_patents_WW', 'value_worldwide[bil.USD]', df)
#lm.fit(X,Y)

#Yhat=lm.predict(X)
#print(Yhat[0:5])