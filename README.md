# Software Engineering 2018
- A project to try to make a script to colorize the Delaunay figure according to the mean value of the points.

## Member
1620501 Akari Iijima
1620536 Marin Matsumoto

## Version
- python 3.6.0

## Preparation

```
[~/work/SoftwareEngineering$] python -m venv env
[~/work/SoftwareEngineering$] source env/bin/activate
[~/work/SoftwareEngineering$] pip install -r requirements.txt
```
- If an error occurs in matplotlib [HERE](https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)

## Constitution

```
SoftwareEngineering /
┣ delaunayTriangulation.py      # Delaunay diagram creation script
┣ delaunayTriangulationTest.py  # Test of delaunay diagram creation script
┣ fetchData.py                  # Create format json data by Scraping
┣ plot_delaunay.py              # Delaunay diagram creation script by mm-1107
┣ requirements.txt              # When necessary for environment construction
┣ data /
┃ 	┣ test_data.json	# {x,y,value}
┃ 	┣ mapsData.json	# {name,x,y}
┃ 	┣ populationData.json	# {name,value}
┃ 	┣ productionData1.json	# {x,y,value} Data of Tokyo
┃ 	┗ productionData2.json	# {x,y,value} Data of Japan
┗ output /
 	┣ test_data.png	# Created by data/test_data.json
	┣ triangular.png	# Created by random data
	┣ triangular01.png	# Created by random data
	┣ populationRatioInTokyo.png	# Created by data/productionData1.json
 	┗ populationRatioInJapan.png	# Created by data/productionData2.json


```
