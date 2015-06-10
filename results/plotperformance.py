from matplotlib import pyplot
import pickle

# Percentage of "long" reads
# Use results based on more data
pyplot.bar([1.1, 2.1, 3.1, 4.1, 5.1], [0.0167378327358, 0.0231216091488, 0.0193579776567, 0.0207411411105, 0.0247012411701])
pyplot.xlabel('Ancestry')
pyplot.ylabel('Long reads (%)')
pyplot.xticks([1.5, 2.5, 3.5, 4.5, 5.5], ['SAS', 'EAS', 'AMR', 'AFR', 'EUR'])
pyplot.show()

# Locations of structural variation
pickleFile = open('seqdata-four_slaves-12-pickle.txt', 'rb') # Use one based on more data
locationsByContinent = pickle.load(pickleFile)
for (continent, locations) in locationsByContinent:
    pyplot.hist(locations, 100)
    pyplot.show()

# Strong scaling
pyplot.plot([2, 4, 6], [133.44, 90.78, 41.98])
pyplot.xticks([2, 4, 6, 8])
pyplot.yticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
pyplot.xlabel('Number of slaves')
pyplot.ylabel('Time (minutes)')
pyplot.show()

# Weak scaling
pyplot.plot([2, 4], [133.44, 182.76])
pyplot.xticks([2, 4, 6, 8])
pyplot.yticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
pyplot.xlabel('Number of slaves')
pyplot.ylabel('Time (minutes)')
pyplot.show()
