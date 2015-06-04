
#!/usr/bin/python
import os
import sys
from pyspark import SparkContext
sc = SparkContext(appName = 'continents', master = os.environ['MASTER'])

#countries = [('EAS', 'CDX'), ('EAS', 'CHB'), ('AFS', 'JPT'), ('EAS', 'GHN')]
countries = {'EAS': 'CDX', 'EAS': 'CHB', 'EAS': 'JPT', 'EUR': 'GBR'};
#groups = sc.parallelize(countries) #creates an RDD of the list countries
continents = groups.groupWith('EAS').collect()
print continents

sc.stop()
