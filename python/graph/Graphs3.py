import matplotlib.pyplot as graph
import pandas as pd

dataframe = pd.read_csv('C://Users//datasets//landprice.csv')
X = dataframe.iloc[0: ,0]
y = dataframe.iloc[0: ,1]

graph.scatter(X,Y,color='red')
graph.title("Area vs Price of Lands")
graph.xlabel("Area of the land in thousand Sq Foot")
graph.ylabel("Price of the land in Million US Dollars")
