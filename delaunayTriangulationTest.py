import unittest
from delaunayTriangulation import generateRandomJsonData, getJsonData, calculationTriangles, detectColor, plotTriangles

# This is test file.

class delaunayTriangulation(unittest.TestCase):
    """test class of delaunayTriangulation.py
    """

    def test_generateRandomJsonData(self):
        """test method for generateRandomJsonData
        value1 = 2
        value2 = 6
        expected = 8
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)"""
        actual = generateRandomJsonData()

    def test_getJsonData(self):
        """test method for getJsonData
        """
        actual = getJsonData(jsonFile)
        
    def test_calculationTriangles(self):
        """test method for calculationTriangles
        """
        actual = calculationTriangles(locations)

    def test_detectColor(self):
        """test method for detectColor
        """
        actual = detectColor(triangulation, locations, values)

    def test_plotTriangles(self):
        """test method for plotTriangles
        """
        actual = plotTriangles(locations, triangles, imageName)

if __name__ == "__main__":
    unittest.main()
    
