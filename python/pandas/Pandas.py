import pandas as pd

dataframe = pd.read_csv('Buy_Book.csv')
head = dataframe.head() # first few row
tail = dataframe.tail(3) # last few row
tail = dataframe[5:11] # 5 to 10
rows,columns = dataframe.shape
print(rows, " " , columns)
income = dataframe.Income # column name == dataframe['Income']
# dataframe[['Age', 'Income']]
x = dataframe.iloc[0:11,1:3] # integer location
# x = dataframe.iloc[0:11,-1]
# x = dataframe.loc[ ['country','flag'],[]] # string value only, in spite of integer

stat = dataframe['Age'].max() # min count mean(Average), std(standard deviation)
stat = dataframe.describe()
stat = dataframe[dataframe.Age>35] # == dataframe['Age'].max()
stat = dataframe[['Student','Income']]dataframe[dataframe.Age>35]


