import matplotlib.pyplot as graph

goal_scores = [3,7,4,2,9,3,1]
match_no = [1,2,3,4,5,6,7]

graph.bar(match_no,goal_scores, color="red",width=0.2,edgecolor='yellow',linewidth=3,xerr=1,yerr=1,ecolor='blue',alpha=0.4,align='edge') #alpha = blurred = 0 - 1
#graph.barh(match_no,goal_scores) # horizontal
graph.title("Goals Scored")
graph.xlabel("Match #")
graph.ylabel("No of Goals Scored")
graph.show()
