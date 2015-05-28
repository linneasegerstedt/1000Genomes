#!/usr/bin/env python
import os
import sys
from pyspark import SparkContext

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

path = sys.argv[1]
fileNames = ['HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.sam'] # Should get all filenames in the directory in our final solution

def lenlimit(line):
        return abs(int(line[10])) > 1000

for fileName in fileNames:
	fileNameParts = fileName.split('.')
	individualID = fileNameParts[0]
	lines = sc.textFile(path + '/' + fileName)

	fullLines = lines.map(lambda line: [individualID] + line.split())
	filteredLines = fullLines.filter(lenlimit).collect()
		
	for line in filteredLines:
		pos1 = int(fileNameParts[3])
		pos2 = int(fileNameParts[7])
			
		def combine(pos1, pos2):
			return pos1 == pos2
			
	groupedLines = filteredLines.groupBy(combine).collect() 
	
	print (groupedLines)
