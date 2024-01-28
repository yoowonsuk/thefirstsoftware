import matplotlib.pyplot as graph
import numpy as np

a = np.arange(0,210,30)
x = np.cos(a) # tan, exp, sqrt, log
y = np.sin(a)
graph.plot(a,x, color='r')
graph.plot(a,y, color='g')
graph.show()
