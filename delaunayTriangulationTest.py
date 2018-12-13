import unittest
from delaunayTriangulation import generateRandomJsonData, getJsonData, calculationTriangles, detectColor, plotTriangles

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
        expectedValuesLength = 100
        acutualLocations, actualValues = generateRandomJsonData()
        maxX = max(acutualLocations[0])
        minX = min(acutualLocations[0])
        maxY = max(acutualLocations[1])
        minY = min(acutualLocations[1])
        maxValue = max(actualValues)
        minValue = min(actualValues)
        lengthX = len(acutualLocations[0])
        lengthY = len(acutualLocations[1])
        lengthValue = len(actualValues)
        self.assertEqual(True , 0 <= minX and maxX <= 500)
        self.assertEqual(True , 0 <= minY and maxY <= 500)
        self.assertEqual(True , 0 <= minValue and maxValue <= 1000)
        self.assertEqual(100 , lengthX)
        self.assertEqual(100 , lengthY)
        self.assertEqual(100 , lengthValue)

    '''
    def test_getJsonData(self):
        """test method for getJsonData
        1.check type(except string or boolean)
        2.check length
        """
        actualLocations, actualValues = getJsonData(jsonFile)

    def test_getJsonNoData(self):
        """test method for getJsonData
        1.check type(except string or boolean)
        2.check length
        """
        acutualLocations, actualValues = getJsonData()

    def test_calculationTriangles(self):
        """test method for calculationTriangles
        1.triangilation 
        2.triangules have three index number
        """
        actualTriangulation, actualTriangles = calculationTriangles(locations)

    def test_detectColor(self):
        """test method for detectColor
        """
        actual = detectColor(triangulation, locations, values)

    def test_plotTriangles(self):
        """test method for plotTriangles
        """
        plotTriangles(locations, triangles, imageName)
      '''  

if __name__ == "__main__":
    unittest.main()
    
