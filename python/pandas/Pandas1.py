import pandas as pd

dataframe = pd.read_csv('C:\\Users\\absolute_directory\\name.csv')
dummy = pd.get_dummies(dataframe.City).iloc[:,0:2] # there are three categories
dataframe = pd.concat([dataframe, dummy],axis=1) # concat column = 1, if row = 0
dataframe = dataframe.drop(['City'], axis=1)

