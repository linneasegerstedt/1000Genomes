import os
import sys
from pyspark import SparkContext
from matplotlib import pyplot

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])

path = sys.argv[1]

countryDictionary = {'CDX': 'EAS', 'CHB': 'EAS', 'JPT': 'EAS', 'KHV': 'EAS', 'CHS': 'EAS', 'BEB': 'SAS', 'GIH': 'SAS', 'ITU': 'SAS', 'PJL': 'SAS', 'STU': 'SAS', 'ASW': 'AFR', 'ACB': 'AFR', 'ESN': 'AFR', 'GWD': 'AFR', 'LWK': 'AFR', 'MSL': 'AFR', 'YRI': 'AFR', 'GBR': 'EUR', 'FIN': 'EUR', 'IBS': 'EUR', 'TSI': 'EUR', 'CEU': 'EUR', 'CLM': 'AMR', 'MXL': 'AMR', 'PEL': 'AMR', 'PUR': 'AMR'}

def splitFile((fileName, fileContent)):
	fileNameParts = fileName.split('.')
	country = fileNameParts[5]
        continent = countryDictionary[country]
        lines = fileContent.strip().split('\n')
        return [(continent, line.split()) for line in lines]

files = sc.wholeTextFiles(path)
splitFiles = files.flatMap(splitFile)
totalCounts = splitFiles.countByKey()

filteredLines = splitFiles.filter(lambda (_, line): abs(int(line[8])) > 1000)
filteredCounts = filteredLines.countByKey()

for continent, filteredCount in filteredCounts.iteritems():
        print continent + ": " + str(float(filteredCount) / totalCounts[continent])
