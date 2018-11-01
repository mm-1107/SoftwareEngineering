import scipy.stats
import scipy.spatial
from numpy.random import RandomState
import matplotlib.pyplot as plt

# setting
randomValue = RandomState(100000)
ax = plt.figure().add_subplot(111)

# coordinate of locations (locations=[[x,...],[y,...]])
locations = randomValue.randint(0, 500, size=(2, 100))
# values of locations (values=[0,0,...])
values = randomValue.randint(0, 1000, size=(100))


# triangulation
triangulation = scipy.spatial.Delaunay(locations.T)

# plot
plt.triplot(locations[1],
            locations[0],
            triangles=triangulation.simplices.copy())
plt.plot(locations[1], locations[0], 'o')
plt.savefig('triangular01.png')
