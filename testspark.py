import os
import sys
from pyspark import SparkContext
from matplotlib import pyplot

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

path = sys.argv[1]

countryDictionary = {'CDX': 'EAS', 'CHB': 'EAS', 'JPT': 'EAS', 'KHV': 'EAS', 'CHS': 'EAS', 'BEB': 'SAS', 'GIH': 'SAS', 'ITU': 'SAS', 'PJL': 'SAS', 'STU': 'SAS', 'ASW': 'AFR', 'ACB': 'AFR', 'ESN': 'AFR', 'GWD': 'AFR', 'LWK': 'AFR', 'MSL': 'AFR', 'YRI': 'AFR', 'GBR': 'EUR', 'FIN': 'EUR', 'IBS': 'EUR', 'TSI': 'EUR', 'CEU': 'EUR', 'CLM': 'AMR', 'MXL': 'AMR', 'PEL': 'AMR', 'PUR': 'AMR'}

# Get a list of all SAM files in the directory
fileFile = open(path + '.txt', 'r') # Smarter way to get list of files?
files = fileFile.readlines()
fileFile.close()

totalLines = sc.parallelize([])
print "********************************************************************"
print "START PARTITIONS: " + str(totalLines.getNumPartitions())
print "********************************************************************"

for file in files:
    fileNameParts = file[:-1].split('.')
    country = fileNameParts[4]
    lines = sc.textFile('/' + path + '/' + file[:-1])
    print "********************************************************************"
    print "ADDED PARTITIONS " + file + ": " + str(lines.getNumPartitions())
    print "********************************************************************"

    continentLines = lines.map(lambda line: (countryDictionary[country], line.split()))
    totalLines = totalLines.union(continentLines)

totalCounts = totalLines.countByKey()

filteredLines = totalLines.filter(lambda (_, line): abs(int(line[8])) > 1000)
filteredCounts = filteredLines.countByKey()

for continent, filteredCount in filteredCounts.iteritems():
        print continent + ": " + str(float(filteredCount) / totalCounts[continent])
