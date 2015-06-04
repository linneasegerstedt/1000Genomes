import os
import sys
from pyspark import SparkContext
from matplotlib import pyplot

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

path = sys.argv[1]
fileNames = ['HG00122.chrom20.ILLUMINA.bwa.GBR.low_coverage.20121211.sam'] # Should get all filenames in the directory in our final solution

countryDictionary = {'CDX': 'EAS', 'CHB': 'EAS', 'JPT': 'EAS', 'KHV': 'EAS', 'CHS': 'EAS', 'BEB': 'SAS', 'GIH': 'SAS', 'ITU': 'SAS', 'PJL': 'SAS', 'STU': 'SAS', 'ASW': 'AFR', 'ACB': 'AFR', 'ESN': 'AFR', 'GWD': 'AFR', 'LWK': 'AFR', 'MSL': 'AFR', 'YRI': 'AFR', 'GBR': 'EUR', 'FIN': 'EUR', 'IBS': 'EUR', 'TSI': 'EUR', 'CEU': 'EUR', 'CLM': 'AMR', 'MXL': 'AMR', 'PEL': 'AMR', 'PUR': 'AMR'}

for fileName in fileNames:
	fileNameParts = fileName.split('.')
	individual = fileNameParts[0]
	country = fileNameParts[4]
	lines = sc.textFile(path + '/' + fileName)

	fullLines = lines.map(lambda line: [individual, countryDictionary[country]] + line.split())
	filteredLines = fullLines.filter(lambda line: abs(int(line[10])) > 1000)

	# Doing a collect here might be unnecessary
	groupedLines = filteredLines.groupBy(lambda line: line[2]).collect()
	unsortedLines = [(id, list(fragments)) for (id, fragments) in groupedLines]

	print unsortedLines

#	plotData = [([0, int(reads[1][5])], [int(reads[0][5]), 0]) for (_, reads) in unsortedLines]

#	for (xData, yData) in plotData:
#		pyplot.plot(xData, yData)
	
#	pyplot.show()
