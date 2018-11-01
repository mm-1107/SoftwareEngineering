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

def assimVertex(index): return triangulation.points[index]
triangleSet = map(assimVertex, triangulation.vertices)

# liner
plt.triplot(locations[0],
            locations[1],
            #triangles=triangleSet,
            triangles=triangulation.simplices.copy(),
            color='black',
            linewidth=0.5)

# triangle color
index = 0
for triangle in triangleSet:
    ax.add_patch(plt.Polygon(triangle,
                             facecolor='0.3',
                             alpha=0.5))
    index += 1

# output
plt.savefig('triangular.png')
#plt.show()
