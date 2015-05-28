from matplotlib import pyplot

xData = ([0, 200], [0, 350])
yData = ([300, 0], [250, 0])

for x, y in xData, yData:
  pyplot.plot(x, y)
  pyplot.show() 
