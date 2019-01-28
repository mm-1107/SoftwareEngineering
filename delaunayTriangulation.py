import scipy.stats
import scipy.spatial
from numpy.random import RandomState
import numpy as np
import matplotlib.pyplot as plt
import sys
import json
import argparse

def generateRandomJsonData(seed=None):
    """To generate random Json data.
    This return 2 arrays, "locations" and "values".
    "locations" is two dimention arrays that have x and y coordinate.
    "values" is one dimention array that has value of coordinate point.

    :param none
    :return1 locations
    :rtype 2darray
    :return2 values
    :rtype 1darray
    """
    randomValue = RandomState(seed)
    # coordinate of locations (locations=[[x,...],[y,...]])
    locations = randomValue.randint(0, 500, size=(2, 100))
    # values of locations (values=[0,0,...])
    values = randomValue.randint(0, 1000, size=(100))
    return locations, values


def getJsonData(jsonFile):
    """To read json data.
    Json data has 3 keys x, y and value. 
    (x and y dimention and values of coordinate point)
    This creates from json data to 2 format arrays.
    If json data([{"x":x, "y":y, "value":0},...]) is recieved, 
    2 arrays(locations=[[x,...],[y,...]], values=[0,...]) are created.
    "locations" is two dimention arrays that have x and y coordinate.
    "values" is one dimention array that has value of coordinate point.

    :param jsonFile
    :type file(json dict)
    :return1 locations
    :rtype 2darray
    :return2 values
    :rtype 1darray
    """
    if jsonFile:
        f = open(jsonFile, 'r')
        jsonData = json.load(f)
        locations = np.array([[],[]])
        values = np.array([])

        for row in jsonData:
            locations = np.concatenate((locations,np.array([[row["x"]],[row["y"]]])),axis=1)
            values = np.append(values,row["value"])
        f.close()
        return locations, values
    else:
        return generateRandomJsonData()


def calculationTriangles(locations):
    """To confirm the triangle for making delaunay trianglations from locations.
    "triangulation" is class of Delaunay.
    "triangles" is equel to "Delaunay.vertices". 

    :param locations
    :type 2darray
    :return1 triangulation
    :rtype scipy.spatial.qhull.Delaunay
    :return2 triangles
    :rtype 2darray
    """
    # triangulation
    triangulation = scipy.spatial.Delaunay(locations.T)
    triangles = triangulation.simplices.copy()
    return triangulation, triangles


def calculationStandardScore(colorList):
    """To calculate deviation value of colorList.
    Deviation value is that score when adjustment is made 
    so that average point 50 standard deviation 10.

    :param colorList
    :type 1darray
    :return score
    :rtype 1darray
    """
    score = np.round_(50+10*(colorList-np.average(colorList))/np.std(colorList))
    return score


def detectColor(triangulation, locations, values):
    """To detect color of triangles from values by checking deviation value 
    and draw delaunay trianglations by matplotlib.
    Value is high if it is close to red, value is small if it is close to black.

    :param1 triangulation
    :type1 scipy.spatial.qhull.Delaunay
    :param2 locations
    :type2 2darray
    :param3 values
    :type3 1darray
    :return1 ax
    :rtype matplotlib.axes._subplots.AxesSubplot
    :return2 colors
    :rtype 2darray
    """
    ax = plt.figure().add_subplot(111)
    def assimVertex(index): return triangulation.points[index]
    triangleSet = map(assimVertex, triangulation.vertices)
    # triangle color
    index = 0
    colorList = np.array([])

    # create colorAverage list roop
    for trianglePointIndexes in triangulation.simplices:
        colors = values[trianglePointIndexes]
        colorAverage = np.average(colors)
        colorList = np.append(colorList,colorAverage)

    score = calculationStandardScore(colorList)
    colors = []
    # paint color roop
    for trianglePointIndexes in triangulation.simplices:
        triangle = locations.T[trianglePointIndexes]
        if score[index]>65:
            color = "red"
            colors.append([score[index],color])
        elif score[index]>50:
            color = "yellow"
            colors.append([score[index],color])
        elif score[index] > 40:
            color = "green"
            colors.append([score[index],color])
        elif score[index]>30:
            color = "blue"
            colors.append([score[index],color])
        else:
            color = "black"
            colors.append([score,color])
        ax.add_patch(plt.Polygon(triangle,
                                 facecolor=color,
                                 alpha=0.5))
        index += 1
    return ax, colors


def plotTriangles(locations, triangles, imageName):
    """To deal with plotting the triangles by matplotlib 
    and create [imageName].png

    :param1 locations
    :type1 2darray
    :param2 triangles
    :type2 2darray
    :param3 imageName
    :type3 str
    :return none
    """
    # liner
    plt.triplot(locations[0],
                locations[1],
                triangles=triangles,
                color='black',
                linewidth=0.5)
    plt.savefig(imageName)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog="delaunayTriangulation.py",
                usage="python delaunayTriangulation.py -j data/testData.json -i output/testData.png",
                description="colorize the Delaunay figure according to the mean value of the points.",
                add_help = True
                )
    parser.add_argument("-j","--json",
                        help="json file directory"
                        )
    parser.add_argument("-i","--image",
                        help="output image directory",
                        required = True
                        )
    args = parser.parse_args()
    jsonFile = args.json
    imageName = args.image

    locations, values = getJsonData(jsonFile)
    triangulation, triangles = calculationTriangles(locations)
    ax, colors = detectColor(triangulation, locations, values)
    plotTriangles(locations, triangles, imageName)
