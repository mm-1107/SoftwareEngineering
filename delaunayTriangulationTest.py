import HtmlTestRunner
import unittest
import numpy as np
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
        jsonFile = "./data/test_data.json"
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
        1.triangilation
        2.triangules have three index number
        """
        locationsList = np.array([[100., 438., 412., 123., 234., 31., 451.],
                                  [400., 22., 219., 56., 456., 56., 500.]])
        actualTriangulation, actualTriangles = calculationTriangles(locationsList)
        expectedTriangulationType = actualTriangulation.vertices
        #self.assertEqual(expectedTriangulationType,actualTriangles)
    
    def calculationStandardScore(self):
        """test method for calculationStandardScore
        1.check calculation
        """
        colorList = [64.33333333,331.,204.,323.33333333,470.66666667,604.,344.33333333,324.,77.66666667,57.33333333,350.,633.33333333,500.]
        acutual = calculationStandardScore(color_list)
        score = [36., 50., 43., 50., 58., 65., 51., 50., 36., 35., 51., 66., 59.]
        self.assertEqual(score,actual)

 
    # def test_detectColor(self):
    #     """test method for detectColor
    #     """
    #     actual = detectColor(triangulation, locations, values)
    #
    # def test_plotTriangles(self):
    #     """test method for plotTriangles
    #     """
    #     plotTriangles(locations, triangles, imageName)
    #   '''

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='delaunay'))
