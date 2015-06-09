import os
import sys
from pyspark import SparkContext
import pickle

sc = SparkContext(appName = 'genes', master = os.environ['MASTER'])
path = sys.argv[1]

countryDictionary = {'CDX': 'EAS', 'CHB': 'EAS', 'JPT': 'EAS', 'KHV': 'EAS', 'CHS': 'EAS', 'BEB': 'SAS', 'GIH': 'SAS', 'ITU': 'SAS', 'PJL': 'SAS', 'STU': 'SAS', 'ASW': 'AFR', 'ACB': 'AFR', 'ESN': 'AFR', 'GWD': 'AFR', 'LWK': 'AFR', 'MSL': 'AFR', 'YRI': 'AFR', 'GBR': 'EUR', 'FIN': 'EUR', 'IBS': 'EUR', 'TSI': 'EUR', 'CEU': 'EUR', 'CLM': 'AMR', 'MXL': 'AMR', 'PEL': 'AMR', 'PUR': 'AMR'}


### For each "continent" (group of populations), find the share of fragments ###
### for which the alignment indicates a length of more than 1000 base pairs. ###

# Read a list of all SAM files in the directory. Presupposes that there is a file
# called <path>.txt which contains such a list.  
fileFile = open(path + '.txt', 'r')
files = fileFile.readlines()
fileFile.close()

outputFile = open(path + '-output.txt', 'wb')

totalLines = sc.parallelize([])
outputFile.write('Initial number of partitions: ' + str(totalLines.getNumPartitions()) + '\n\n')

for file in files:
    fileName = file[:-1] # Take away newline character
    fileNameParts = fileName.split('.')
    country = fileNameParts[4]
    lines = sc.textFile('/' + path + '/' + fileName)
    outputFile.write('Added number of partitions for ' + fileName + ': ' + str(lines.getNumPartitions()) + '\n\n')

    continentLines = lines.map(lambda line: (countryDictionary[country], line.split()))
    totalLines = totalLines.union(continentLines)

filteredLines = totalLines.filter(lambda (_, line): abs(int(line[8])) > 1000)

totalCounts = totalLines.countByKey()
filteredCounts = filteredLines.countByKey()
for continent, filteredCount in filteredCounts.iteritems():
    outputFile.write(continent + '\n')
    outputFile.write('Total count: ' + str(totalCounts[continent]) + '\n')
    outputFile.write('Filtered count: ' + str(filteredCount) + '\n')
    outputFile.write('Share: ' + str(float(filteredCount) / totalCounts[continent]) + '\n\n')

outputFile.close()


### Group the locations of reads by "continent" (group of populations) ###

def seqFunc(locations, line):
    locations.append(int(line[3]))
    return locations

def combFunc(firstLocations, secondLocations):
    return firstLocations + secondLocations

locationsByContinent = filteredLines.aggregateByKey([], seqFunc, combFunc).collect()

pickleFile = open(path + '-pickle.txt', 'wb')
pickle.dump(locationsByContinent, pickleFile)
pickleFile.close()
