import scipy.stats
import scipy.spatial
from numpy.random import RandomState
import matplotlib.pyplot as plt
import sys

def generateRandomJsonData(seed=None):
    """To generate random JsonData.
    This return array, "locations" and "values".
    "locations" is two dimention array that have x and y coordinate.
    "values" is one dimention array that have value of coordinate point

    :param none
    :return1 locations
    :rtype array
    :return2 values
    :rtype array
    """
    randomValue = RandomState(seed)
    # coordinate of locations (locations=[[x,...],[y,...]])
    locations = randomValue.randint(0, 500, size=(2, 100))
    print(type(locations))
    # values of locations (values=[0,0,...])
    values = randomValue.randint(0, 1000, size=(100))
    return locations, values
    #return [(locations[i][0],locations[i][1],values[i]) for i in range(len(locations)) ]

def getJsonData(jsonFile):
    """.

    :param jsonFile:This file have x and y dimention and values of coordinate point.
    :type jsondict
    :return1 none
    :return2 generateRandomJsonData()
    :rtype array
    """
    if jsonFile:
        return None       
    else:
        return generateRandomJsonData() 

def calculationTriangles(locations):
    """[Calculation Triangles]
    Deals with plotting the triangles
    """
    # triangulation
    triangulation = scipy.spatial.Delaunay(locations.T)
    triangles = triangulation.simplices.copy()
    return triangulation, triangles


def detectColor(triangulation, locations, values):
    ax = plt.figure().add_subplot(111)
    def assimVertex(index): return triangulation.points[index]
    triangleSet = map(assimVertex, triangulation.vertices)
    # triangle color
    print("Vertices list",triangulation.vertices)
    print("Locations",locations)
    index = 0
    for trianglePointIndexes in triangulation.simplices:
        
        triangle = locations.T[trianglePointIndexes]
        print("Triangle",triangle)
        colors = values[trianglePointIndexes]
        print("Colors",colors)
        ax.add_patch(plt.Polygon(triangle,
                                 facecolor='0.3',
                                 alpha=0.5))
        index += 1
    return ax


def plotTriangles(locations, triangles, imageName):
    """plotTriangles
    Deals with plotting the triangles
    """
    # liner
    plt.triplot(locations[0],
                locations[1],
                #triangles=triangleSet,
                triangles=triangles,
                color='black',
                linewidth=0.5)
    plt.savefig(imageName)

if __name__ == '__main__':
    
    #args = sys.argv
    #commandType = args[1]
    #jsonFile = args[2]
    #imageName = args[3]
    locations, values = getJsonData(False)
    triangulation, triangles = calculationTriangles(locations)
    ax = detectColor(triangulation, locations, values)
    #plotTriangles(locations, triangles, imageName)
