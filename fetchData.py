import requests
from bs4 import BeautifulSoup
import json

def getHTMLcontents(url):
    url = url
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "lxml")
    return soup

def mapsFormatJson(mainData):
    i = 0
    mainJson = []
    subJson = {}
    for data in mainData[0]:
        #print(subJson)
        if(len(subJson)==3):
            mainJson.append(subJson)
            subJson={}
        elif(12 <= i and i <= 257 and i%4 == 0):
            subJson.update({"name":data.rstrip("\r\n")})
        elif(12 <= i and i <= 257 and i%4 == 1):
            j = 0
            for table in data:
                if(j==3 or j==5):
                    l = 0
                    for td in table:
                        if(l==3):
                            if(j==3):
                                subJson.update({"y":float(td.string[1:-7]) + (float(td.string[5:-4])*60.0 + float(td.string[8:-1]))/3600.0})
                            elif(j==5):
                                subJson.update({"x":float(td.string[1:-7]) + (float(td.string[5:-4])*60.0 + float(td.string[8:-1]))/3600.0})
                        l += 1
                j += 1
        i += 1
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
                jsonData.append({"x":maps["x"],"y":maps["y"],"value":population["value"]})
                break
    return jsonData


if __name__ == '__main__':
    #Create maps data json.
    #mapsData = getHTMLcontents("http://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/tokyo_heso.htm")
    #mapsData = mapsData.select('body')
    #mapsJson = mapsFormatJson(mapsData)
    #print(mapsJson)

    #Create population data json.
    #populationData = getHTMLcontents("http://area-info.jpn.org/FornPerPop130001.html")
    #populationData = populationData.select('body')
    #populationJson = populationFormatJson(populationData)
    #print(populationJson)

    #Create required data format
    mapsJsonData = getJsonData("data/mapsData.json")
    populationJsonData = getJsonData("data/populationData.json")
    formatData = createFormatJsonData(mapsJsonData,populationJsonData)
    print(formatData)
