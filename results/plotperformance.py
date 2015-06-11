from matplotlib import pyplot
import pickle

# Percentage of "long" reads
# Use results based on more data
pyplot.bar([1.1, 2.1, 3.1, 4.1, 5.1], [0.0169075601112, 0.0204209396628, 0.0181498564408, 0.0198870805245, 0.0245655416287])
pyplot.xlabel('Ancestry group')
pyplot.ylabel('Reads from "long" fragments (%)')
pyplot.xticks([1.5, 2.5, 3.5, 4.5, 5.5], ['South Asian', 'East Asian', 'American', 'African', 'European'])
pyplot.show()

# Locations of structural variation
pickleFile = open('seqdata-six_slaves_8-pickle.txt', 'rb')
locationsByContinent = pickle.load(pickleFile)
for (continent, locations) in locationsByContinent:
    print continent
    pyplot.hist(locations, 100)
    pyplot.xlabel('Location')
    pyplot.ylabel('Reads from "long" fragments')
    pyplot.show()

# Strong scaling
pyplot.plot([2, 4, 6], [133.44, 90.78, 41.98])
pyplot.xticks([2, 4, 6])
pyplot.yticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
pyplot.xlabel('Number of slaves')
pyplot.ylabel('Time (minutes)')
pyplot.show()

# Weak scaling
pyplot.plot([2, 4, 6], [133.44, 182.76, 171.12])
pyplot.xticks([2, 4, 6])
pyplot.yticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
pyplot.xlabel('Number of slaves')
pyplot.ylabel('Time (minutes)')
pyplot.show()
