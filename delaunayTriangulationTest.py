import HtmlTestRunner
import unittest
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.spatial
from delaunayTriangulation import generateRandomJsonData, getJsonData, calculationStandardScore,calculationTriangles, detectColor, plotTriangles

# This is test file.
class delaunayTriangulation(unittest.TestCase):
    """test class of delaunayTriangulation.py
    """
    def test_generateRandomJsonData(self):
        """test method for generateRandomJsonData
        1.check range
        2.check length
        """
        expectedLocationsRange = 500
        expectedValuesRange = 1000
        expectedValuesLength = 100
        acutualLocations,actualValues= generateRandomJsonData()
        maxX = max(acutualLocations[0])
        minX = min(acutualLocations[0])
        maxY = max(acutualLocations[1])
        minY = min(acutualLocations[1])
        maxValue = max(actualValues)
        minValue = min(actualValues)
        lengthX = len(acutualLocations[0])
        lengthY = len(acutualLocations[1])
        lengthValue = len(actualValues)
        self.assertEqual(True , 0 <= minX and
                         maxX <= expectedLocationsRange)
        self.assertEqual(True , 0 <= minY and
                         maxY <= expectedLocationsRange)
        self.assertEqual(True , 0 <= minValue and
                         maxValue <= expectedValuesRange)
        self.assertEqual(expectedValuesLength , lengthX)
        self.assertEqual(expectedValuesLength , lengthY)
        self.assertEqual(expectedValuesLength , lengthValue)

    def test_getJsonData(self):
        """test method for getJsonData(with argument)
        1.check length(1st dimension)
        2.check length(2nd dimension)※certainly 3 length
        """
        jsonFile = "./data/testData.json"
        expected1stDimensionLength = 2
        expected2ndDimensionLength = 7
        actualLocations, actualValues = getJsonData(jsonFile)
        self.assertEqual(len(actualLocations[0]),
                         len(actualValues))
        self.assertEqual(len(actualLocations[1]),
                         len(actualValues))
        self.assertEqual(expected1stDimensionLength,
                         len(actualLocations))
        self.assertEqual(expected2ndDimensionLength,
                         len(actualLocations[0]))
        self.assertEqual(expected2ndDimensionLength,
                         len(actualLocations[1]))


    def test_getJsonNoData(self):
        """test method for getJsonData(without argument)
        1.check range
        2.check length
        """
        expectedLocationsRange = 500
        expectedValuesRange = 1000
        expectedValuesLength = 100
        acutualLocations, actualValues = getJsonData(None)
        maxX = max(acutualLocations[0])
        minX = min(acutualLocations[0])
        maxY = max(acutualLocations[1])
        minY = min(acutualLocations[1])
        maxValue = max(actualValues)
        minValue = min(actualValues)
        lengthX = len(acutualLocations[0])
        lengthY = len(acutualLocations[1])
        lengthValue = len(actualValues)
        self.assertEqual(True , 0 <= minX and
                         maxX <= expectedLocationsRange)
        self.assertEqual(True , 0 <= minY and
                         maxY <= expectedLocationsRange)
        self.assertEqual(True , 0 <= minValue and
                         maxValue <= expectedValuesRange)
        self.assertEqual(expectedValuesLength , lengthX)
        self.assertEqual(expectedValuesLength , lengthY)
        self.assertEqual(expectedValuesLength , lengthValue)

    def test_calculationTriangles(self):
        """test method for calculationTriangles
        1.check having same triangiles
        2.check length
        """
        locationsList = np.array([[1., 1., 2., 3., 5.],
                                  [1., 3., 1., 4., 2.]])
        actualTriangulation, actualTriangles = calculationTriangles(locationsList)
        expectedTriangles = np.array([[0, 2, 1],
                                      [3, 1, 2],
                                      [2, 3, 4]])
        actualTriangulationLength = len(actualTriangulation.vertices)
        actualTrianglesLength = len(actualTriangles)
        expectedTrianglesLength = len(expectedTriangles) 
        # sort each element
        for data in actualTriangulation.vertices: data = data.sort()
        for data in actualTriangles: data = data.sort()
        for data in expectedTriangles: data = data.sort()
        # create set
        actualTriangulationVerticesSet = set(((actualTriangulation.vertices[i,0],
                                               actualTriangulation.vertices[i,1],
                                               actualTriangulation.vertices[i,2])
                                              for i in range(len(actualTriangulation.vertices))))
        actualTrianglesSet = set(((actualTriangles[i,0],
                                   actualTriangles[i,1],
                                   actualTriangles[i,2])
                                  for i in range(len(actualTriangles))))
        expectedTrianglesSet = set(((expectedTriangles[i,0],
                                     expectedTriangles[i,1],
                                     expectedTriangles[i,2])
                                    for i in range(len(expectedTriangles))))
        self.assertEqual(actualTriangulationVerticesSet, actualTrianglesSet)
        self.assertEqual(actualTriangulationVerticesSet, expectedTrianglesSet)
        self.assertEqual(actualTrianglesSet, expectedTrianglesSet)
        self.assertEqual(actualTriangulationLength, actualTrianglesLength)
        self.assertEqual(actualTriangulationLength, expectedTrianglesLength)
        self.assertEqual(actualTrianglesLength, expectedTrianglesLength)
    
    def test_calculationStandardScore(self):
        """test method for calculationStandardScore
        1.check calculation
        2.check length
        """
        colorList = np.array([5., 10., 30., 25., 35.])
        actualScore = calculationStandardScore(colorList)
        actualScoreLength = len(actualScore)
        expectedScore = np.array([36., 40., 58., 53., 62.])
        expectedScoreLength = len(expectedScore)x
        self.assertEqual(expectedScore.all(),actualScore.all())
        self.assertEqual(expectedScoreLength,actualScoreLength)

    def test_detectColor(self):
        """test method for detectColor
        1.check having same colors
        2.check length
        """
        locations = np.array([[1., 1., 2., 3., 5.],
                              [1., 3., 1., 4., 2.]])
        values = np.array([5., 10., 30., 25., 35.])
        triangulation = scipy.spatial.Delaunay(locations.T)
        expectedColors = [[49.,"green"],[63.,"yellow"],[38.,"blue"]]
        expectedColorsLength = len(expectedColors)
        actualAx, actualColors = detectColor(triangulation, locations, values)
        actualColorsLength = len(actualColors)
        self.assertEqual(expectedColors.sort(),actualColors.sort())
        self.assertEqual(expectedColorsLength,actualColorsLength)
    
    def test_plotTriangles(self):
        """test method for plotTriangles
        1.check weather an image exists or not
        """
        locations = np.array([[1., 1., 2., 3., 5.],
                              [1., 3., 1., 4., 2.]])
        triangles = np.array([[0, 2, 1],
                              [3, 1, 2],
                              [2, 3, 4]])
        expectedImageName = "output/unitTestExpectedImage"
        plotTriangles(locations, triangles, expectedImageName)
        self.assertEqual(os.path.exists("output/unitTestExpectedImage.png"),True)
        os.remove("output/unitTestExpectedImage.png")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='delaunay'))


    
