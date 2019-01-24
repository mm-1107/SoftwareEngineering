import requests
from bs4 import BeautifulSoup
import json

def getHTMLcontents(url):
    url = url
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "lxml")
    return soup

def mapsFormatJson(mainData):
    i=0
    mainJson = []
    nameData = mainData.findAll("td",{"align":"center"})
    xyData = mainData.findAll("td",{"align":"right"})
    for data in nameData:
        if(i%7==0):
            mainJson.append({"name":data.get_text()[:-1]})
        i += 1
    j=0
    for data in xyData:
        if(j%10==0):
            print(data)
            #mainJson[int(j/10)].update({"y":float(data.get_text()[:3]) + (float(data.get_text()[4:6])*60.0 + float(data.get_text()[-3:-1]))/3600.0})
        if(j%10==5):
            print(data)
            #mainJson[int(j/10)].update({"x":float(data.get_text()[:2]) + (float(data.get_text()[3:5])*60.0 + float(data.get_text()[-3:-1]))/3600.0})
        j += 1
    return mainJson

def populationFormatJson(mainData):
    mainJson = []
    nameList = mainData[0].findAll("",{"class":"name"})
    ratioList = mainData[0].findAll("td",{"align":"right"})
    for name in nameList:
        mainJson.append({"name":name.get_text()[1:]})
    i=0
    for ratio in ratioList:
        if(i%3==0):
            mainJson[int(i/3)].update({"value":float(ratio.get_text()[:-1])})
        i += 1
    return mainJson

def getJsonData(path):
    f = open(path, 'r')
    jsonData = json.load(f)
    return jsonData

def createFormatJsonData(mapsData,populationData):
    jsonData = []
    
    for population in populationData:
        for maps in mapsData:
            if(maps["name"] == population["name"]):
                jsonData.append({"x":maps["y"],"y":maps["x"],"value":population["value"]})
                break
    return jsonData


if __name__ == '__main__':
    #Create maps data json.
    #Tokyo
    #mapsData = getHTMLcontents("http://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/tokyo_heso.htm")
    #Japan
    #mapsData = getHTMLcontents("http://www.gsi.go.jp/KOKUJYOHO/CENTER/zenken.htm")
    #mapsJson = mapsFormatJson(mapsData)
    #print(mapsJson)

    #Create population data json.
    #Tokyo
    #populationData = getHTMLcontents("http://area-info.jpn.org/FornPerPop130001.html")
    #Japan
    #populationData = getHTMLcontents("http://area-info.jpn.org/FornPerPop.html")
    #populationData = populationData.select('body')
    #populationJson = populationFormatJson(populationData)
    #print(populationJson)

    #Create required data format
    mapsJsonData = getJsonData("data/mapsData.json")
    populationJsonData = getJsonData("data/populationData.json")
    formatData = createFormatJsonData(mapsJsonData,populationJsonData)
    print(formatData)

