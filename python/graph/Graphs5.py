import matplotlib.pyplot as graph

boy_marks = [70,43,56,91,76,64,71,83,41,76,56,64,49,76,94,98,76,73,76,91]
girl_marks = [79,68,99,67,64,73,81,43,89,99,76,78,59,90,87,77,79,79,81,90,95]
#graph.hist(marks, bin=3,rwidth=0.90,color='red')
graph.hist([boy_marks,girls_marks],color=['red', 'green'], label=['boys', 'girls'])
# graph.host(boy_marks, color='red', bins=[40,45,50,55,60,65,80,90,95,100])
graph.legend()
graph.show()

