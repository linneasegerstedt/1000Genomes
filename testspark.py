import os
import sys
from pyspark import SparkContext

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

#def lenlimit(line):
#        return abs(int(line[10])) > 1000

path = sys.argv[1]
fileNames = ['HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.sam'] # Should get all filenames in the directory in our final solution

for fileName in fileNames:
	fileNameParts = fileName.split('.')
	individual = fileNameParts[0]
	country = fileNameParts[4]
	lines = sc.textFile(path + '/' + fileName)

	fullLines = lines.map(lambda line: [individual, country] + line.split())
	filteredLines = fullLines.filter(lambda line: abs(int(line[10])) > 1000) #lenlimit

	# Doing a collect here might be unnecessary
	groupedLines = filteredLines.groupBy(lambda line: line[2]).collect()
	unsortedLines = [(id, list(fragments)) for (id, fragments) in groupedLines]

	plotData = [([0, reads[1][5]], [reads[0][5], 0]) for (_, reads) in groupedLines]

	print plotData
#		firstLocation = reads[0][5]
#		secondLocation = reads[1][5]
#		print firstLocation + ", " + secondLocation

	# print groupedLines

#	unsortedLines = [(id, list(fragments)) for (id, fragments) in groupedLines]
	#	print unsortedLines

#	sortedLines = sorted([(id, sorted(fragments)) for (id, fragments) in groupedLines])
#	print sortedLines
#	print len(sortedLines)
