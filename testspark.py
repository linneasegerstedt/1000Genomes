import os
import sys
from pyspark import SparkContext
from matplotlib import pyplot

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

path = sys.argv[1]
fileNames = ['HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.sam'] # Should get all filenames in the directory in our final solution

for fileName in fileNames:
	fileNameParts = fileName.split('.')
	individual = fileNameParts[0]
	country = fileNameParts[4]
	lines = sc.textFile(path + '/' + fileName)

	fullLines = lines.map(lambda line: [individual, country] + line.split())
	filteredLines = fullLines.filter(lambda line: abs(int(line[10])) > 1000)

	# Doing a collect here might be unnecessary
	groupedLines = filteredLines.groupBy(lambda line: line[2]).collect()
	unsortedLines = [(id, list(fragments)) for (id, fragments) in groupedLines]

	plotData = [([0, int(reads[1][5])], [int(reads[0][5]), 0]) for (_, reads) in unsortedLines]

	for (xData, yData) in plotData:
		pyplot.plot(xData, yData)
	
	pyplot.show()
