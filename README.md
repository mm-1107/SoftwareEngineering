# Software Engineering 2018
A project to try to make a script to colorize the Delaunay figure according to the mean value of the points.  
Value is high if it is close to red, value is small if it is close to black.

## What is 'Delaunay'?
It is a figure which is obtained for a set of discretely distributed points within the distance space and which connects them by sides according to a certain method.
![Alt text](/output/triangular.png)

For example, if you use data/productionData1.json that value is population ratio of foreigner in Tokyo
, you can get the following image.

![Alt text](/output/populationRatioInTokyo.png)

**<font color="red">Red</font> : high**

**<font color="yellow">Yellow</font> : mid-high**

**<font color="green">Green</font> : mid-low**

**<font color="blue">Blue</font> : low**

## Member
- 1620501 Akari Iijima
- 1620536 Marin Matsumoto

## Version
- python 3.6.0

## Preparation

```
[~/SoftwareEngineering$] python -m venv env
[~/SoftwareEngineering$] source env/bin/activate
[~/SoftwareEngineering$] pip install -r requirements.txt
```
- If an error occurs in matplotlib [HERE](https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)
- Please install scipy, RandomState, numpy, matplotlib, sys, json if necessary.

## How to create Delaunay figure
1. Prepare a json file with x, y, value in key.  
_※This is sample of json file_  
_※Please use double quotation in key because error occurs when using single quotation._  
**○○○.json**

```

[{"x": 100, "y": 400, "value": 50},
 {"x": 438, "y": 22,  "value": 800},
 {"x": 412, "y": 219, "value": 120},
  :
  :
]
```

2. Please enter the following command at terminal.

```
[~/SoftwareEngineering$] python delaunayTriangulation.py -j [Json Data File] -i [Output Delaunay Image Name]
```

  if you want to try to run random data, please enter the following command.

```
[~/SoftwareEngineering$] python delaunayTriangulation.py -i [Output Delaunay Image Name]
```

## Constitution

```
SoftwareEngineering /
┣ delaunayTriangulation.py      # Delaunay diagram creation script
┣ delaunayTriangulationTest.py  # Test of delaunay diagram creation script
┣ delaunayTriangulation.html    # pydoc
┣ fetchData.py                  # Create format json data by Scraping
┣ requirements.txt              # When necessary for environment construction
┣ data /
┃ 	┣ test_data.json       # {x,y,value}
┃ 	┣ mapsData.json        # {name,x,y}
┃ 	┣ populationData.json  # {name,value}
┃ 	┣ productionData1.json # {x,y,value} Data of Tokyo
┃ 	┗ productionData2.json # {x,y,value} Data of Japan
┗ output /
 	┣ test_data.png         # Created by data/test_data.json
	┣ triangular.png        # Created by random data
	┣ triangular01.png      # Created by random data
	┣ populationRatioInTokyo.png	# Created by data/productionData1.json
 	┗ populationRatioInJapan.png	# Created by data/productionData2.json


```
