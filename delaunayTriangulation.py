import scipy.stats
import scipy.spatial
from numpy.random import RandomState
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

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
    print(locations)
    print(type(locations))
    # values of locations (values=[0,0,...])
    values = randomValue.randint(0, 1000, size=(100))
    print(values)
    return locations, values


def getJsonData(jsonFile):
    """.

    :param jsonFile:This file have x and y dimention and values of coordinate point.
    :type jsondict
    :return1 none
    :return2 generateRandomJsonData()
    :rtype array
    """
    if jsonFile:
        f = open(jsonFile, 'r')
        jsonData = json.load(f)
        print(jsonData)
        locations = np.array([[],[]])
        values = np.array([])

        for row in jsonData:
            locations = np.concatenate((locations,np.array([[row["x"]],[row["y"]]])),axis=1)
            values = np.append(values,row["value"])
            print("locations",locations)
            print("values",values)
        f.close()
        return locations, values
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


def calculationStandardScore(color_list):
    score = np.round_(50+10*(color_list-np.average(color_list))/np.std(color_list))
    return score


def detectColor(triangulation, locations, values):
    ax = plt.figure().add_subplot(111)
    def assimVertex(index): return triangulation.points[index]
    triangleSet = map(assimVertex, triangulation.vertices)
    # triangle color
    print("Vertices list",triangulation.vertices)
    print("Locations",locations)
    index = 0
    color_list = np.array([])

    # create color_average list roop
    for trianglePointIndexes in triangulation.simplices:
        print("trianglePointIndexes",trianglePointIndexes)
        colors = values[trianglePointIndexes]
        print(colors)
        # テスト
        color_average = np.average(colors)
        print("color_average",color_average)
        color_list = np.append(color_list,color_average)
        print("color_list",color_list)

    score = calculationStandardScore(color_list)
    print("score",score)
    # paint color roop
    for trianglePointIndexes in triangulation.simplices:
        triangle = locations.T[trianglePointIndexes]
        if score[index]>65:
            color = "red"
        elif score[index]>50:
            color = "yellow"
        elif score[index] > 40:
            color = "green"
        elif score[index]>30:
            color = "blue"
        else:
            color = "black"
        print(score[index],color)
        ax.add_patch(plt.Polygon(triangle,
                                 facecolor=color,
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

    args = sys.argv
    jsonFile = args[1]
    imageName = args[2]
    locations, values = getJsonData(jsonFile)
    triangulation, triangles = calculationTriangles(locations)
    print("Triangulation", triangulation)
    print("triangules",triangles)
    score = calculationStandardScore(values)
    print(score)
    ax = detectColor(triangulation, locations, values)
    plotTriangles(locations, triangles, imageName)
