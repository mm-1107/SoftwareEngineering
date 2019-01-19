import requests
from bs4 import BeautifulSoup

def getHTMLcontents(url):
    url = url
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "lxml")
    return soup#.contents

if __name__ == '__main__':
    mapsData = getHTMLcontents("http://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/tokyo_heso.htm")
    #populationData = getHTMLcontents("http://area-info.jpn.org/FornPerPop130001.html")
    mapsData = mapsData.select('body')
    i = 0
    mainJson = {}
    subJson = {}
    for data in mapsData[0]:
        if(len(subJson)==3):
            mainJson.update({i:subJson})
            subJson={}
        if(12 <= i and i <= 257 and i%4 == 0):
            subJson.update({"name":data})
        elif(12 <= i and i <= 257 and i%4 == 1):
            j = 0
            for table in data:
                #if(j==3 or j==5):
                #print(j)
                #print(table)
                j += 1
        i += 1
    print(mainJson)
    
#12,16,20
#13,17,21

    #print(populationData)
