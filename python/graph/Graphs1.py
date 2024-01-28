import matplotlib.pyplot as graph
import pandas as pd

dataframe = pd.read_csv("c://Users/datasets/CricketMatch.csv")
Over_X = dataframe.iloc[0: ,0]
Eng_ScoreY = dataframe.iloc[0: ,1]
Nz_ScoreY = dataframe.iloc[0: ,2]

graph.plot(Over_X,Eng_ScoreY,color='red')
graph.plot(Over_X,Nz_ScoreY,color='blue')
graph.title("Score comparsion between Eng and Nz")
graph.xlabel("Overs")
graph.ylabel("Scores")

graph.show()
