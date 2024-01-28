import matplotlib.pyplot as graph

player_Names = ['Modric', 'Ronaldo', 'Kane', 'Messi', 'Mibape', 'Williamson']
Goals = [22,29,13,33,16,6]

separator=[0,0,0.1,0,0.3,0]
graph.pie(Goals,labels=player_Names,autopct='%0.1f%%', explode=separator)
graph.title("Players Goals in their last 10 matchs")
graph.show()
