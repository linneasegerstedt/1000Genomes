import matplotlib.pyplot as plot
from matplotlib import pyplot
all_data = [[1,2],[2,5]]
for point in all_data:
	for point2 in all_data:
		pyplot.plot([point[0], point2[0]], [point[1], point2[1]])
pyplot.show() 
