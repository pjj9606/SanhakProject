from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
import requests
from time import sleep
import time
"""셀레니움을 사용해서 구글 검색 개수를 기록하는 코드"""
"""셀레니움 밴먹어서 BS로 전환"""
# beautifulSoup로 안되서 selenium 사용
# Festival 함, Dinning 함, Cultural 함, Accommodation 함, TourisAttraction 함, Shopping 함
#


r = open('Crolling Result Removed Tag/temp_Korean_레포츠28.txt', mode='rt', encoding='utf-8')
writeFile = open('Crolling Result Removed Tag + numOfSearchResult/0608KOR_crollingResult_레포츠28.txt', mode='w', encoding='utf-8')
numOfContentID = 1

i = 0

def getNumOfSearchResultByBS(keyword):
    #sleep(3)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    url = 'https://www.google.com/search?q=' + str(keyword)
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        Result = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False)
    except:
        return -1

    try:
        filter1 = Result.split("약 ")[1]
    except:
        filter1 = Result.split("검색결과 ")[1]      # 검색결과 수가 너무 적으면 '약'문자가 없음

    numOfSearchResult = filter1.split("개")[0]

    numOfSearchResult = numOfSearchResult.replace(",", '')
    print("numOfSearchResult: ", numOfSearchResult)
    return numOfSearchResult
    #phrase_extract = soup.find(id="result-stats")

    #phrase_text = phrase_extract.text





def getNumOfSearchResultBySel(keyword):
    driver = webdriver.Chrome('/Users/2015125080/Downloads/chromedriver')
    driver.implicitly_wait(3)


    url = 'https://www.google.com/search?q=' + str(keyword)
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    driver.get(header, url)
    Result = driver.find_element_by_id('result-stats').text


    try:
        Result = driver.find_element_by_id('result-stats').text
    except:
        return -1       # 아니 무슨 검색결과 개수가 안나오는게 있냐 진짜
    try:
        filter1 = Result.split("약 ")[1]
    except:
        filter1 = Result.split("검색결과 ")[1]      # 검색결과 수가 너무 적으면 '약'문자가 없음

    numOfSearchResult = filter1.split("개")[0]

    numOfSearchResult.replace(",", '')
    print("numOfSearchResult: ", numOfSearchResult)


    driver.close()
    return numOfSearchResult

def readUntilOr(variable):
    text = r.read(1)
    buffer = ''
    while (text != '|'):
        buffer = str(buffer) + text
        text = r.read(1)
    variable = buffer
    return variable

def removeTag(msg):
    #이거 돌리면 겁나 이상한 태그 몇개 남는데 이건 그냥 손으로 지움
    msg = msg.replace("<br>", "")
    msg = msg.replace("<br >", "")
    msg = msg.replace("<br/>", "")
    msg = msg.replace("<br />", "")
    msg = msg.replace("<a href=", "")
    msg = msg.replace("<BR>", "")
    msg = msg.replace("<Br>", "")
    msg = msg.replace("</Br>", "")
    msg = msg.replace("</a>", "")
    msg = msg.replace("<i>", "")
    msg = msg.replace("</i>", "")
    msg = msg.replace("<em>", "")
    msg = msg.replace("</em>", "")
    msg = msg.replace("</b>", "")
    msg = msg.replace("<b>", "")
    msg = msg.replace("<am>", "")
    msg = msg.replace("</am>", "")
    msg = msg.replace("<sup>", "")
    msg = msg.replace("</sup>", "")
    msg = msg.replace("<bR>", "")
    msg = msg.replace("br>", "")
    msg = msg.replace("</font>", "")
    msg = msg.replace("<div>", "")
    msg = msg.replace("</div>", "")
    msg = msg.replace("<strong>", "")
    msg = msg.replace("</strong>", "")
    msg = msg.replace("<be>", "")
    msg = msg.replace("</be>", "")
    msg = msg.replace("<u>", "")
    msg = msg.replace("</u>", "")

    return msg

def readHomepage(HP) : #긁어온 양식을 조금 수정해서 http만 남도록
    start_Index = HP.find("http")
    slicedHomepage = ''

    if (start_Index == -1):
        return "None homepage"

    i = start_Index
    try :
        while(HP[i] != '''"''') :
            slicedHomepage = slicedHomepage + HP[i]
            i = i+1
        return slicedHomepage
    except:
        return HP


while(i < numOfContentID) :
    addr1 = None; areacode = None; contentid = None; contenttypeid = None; dongcode = None; firstimage = None;
    homepage = None; maps = None; overview = None; sigungucode = None; tel = None; title = None; zipcode = None;
    cat1 = None; cat2 = None; cat3 = None; numOfSearchResult = None;



    print("_____________NEW________________________")
    i = i+1
    print(i)

    addr1 = readUntilOr(addr1)
    addr1 = removeTag(addr1)
    #print("addr1 :", addr1)
    #count_OR = count_OR + 1

    areacode = readUntilOr(areacode)
    #print("areacode: ",areacode)
    #count_OR = count_OR + 1

    contentid = readUntilOr(contentid)
    print("contentid: ", contentid)
    #count_OR = count_OR + 1

    #검사용
    """
    ID = whyId.readline()

    if int(ID) == int(contentid):
        print("같음")
    else:
        print("다름")
        print("originalID :" , ID)
        break
    """

    contenttypeid = readUntilOr(contenttypeid)
    #print("contenttypeid: ", contenttypeid)
    #count_OR = count_OR + 1

    dongcode = readUntilOr(dongcode)
    #print("dongcode: ", dongcode)
    #count_OR = count_OR + 1

    firstimage = readUntilOr(firstimage)
    #print("firstImage: ", firstimage)
    #count_OR = count_OR + 1

    homepage = readUntilOr(homepage)
    #homepage = readHomepage(homepage)
    #homepage = removeTag(homepage)
    print("homepage:", homepage)
    #count_OR = count_OR + 1

    maps = readUntilOr(maps)
    #print("maps: ", maps)
    #count_OR = count_OR + 1

    overview = readUntilOr(overview)
    overview = removeTag(overview)
    if(overview=='') :
        overview = "No overview"
    #print("overview: ", overview)
    #count_OR = count_OR + 1

    sigungucode = readUntilOr(sigungucode)
    #print("sigungucode: ", sigungucode)
    #count_OR = count_OR + 1

    tel = readUntilOr(tel)
    tel = removeTag(tel)
    #print("tel: ", tel)
    #count_OR = count_OR + 1

    title = readUntilOr(title)
    print("title: ", title)
    #count_OR = count_OR + 1

    zipcode = readUntilOr(zipcode)
    #print("zipcode: ", zipcode)
    #count_OR = count_OR + 1

    cat1 = readUntilOr(cat1)
    print("cat1: ", cat1)

    cat2 = readUntilOr(cat2)
    print("cat2: ", cat2)

    cat3 = readUntilOr(cat3)
    print("cat3: ", cat3)


    if(areacode == "No areacode"):      # 아니무슨 areacode가 없는 놈들이있냐
        areacode = -1

    #numOfSearchResult = readUntilOr(numOfSearchResult) # 마지막으로 개수 확인할 때

    r.read(1)   #줄바꿈문자
    #여기까지 read

    try:
        #numOfSearchResult = getNumOfSearchResultBySel(title)
        numOfSearchResult = getNumOfSearchResultByBS(title)
    except:
        numOfSearchResult = -1

    try:
        writeFile.write(addr1)
        writeFile.write("|")
    except:
        writeFile.write('No addr1')
        writeFile.write("|")
        print("None addr1")

    try:
        writeFile.write(areacode)
        writeFile.write("|")
    except:
        writeFile.write('No areacode')
        writeFile.write("|")
        print("None areaCode")

    try:
        writeFile.write(contentid)
        writeFile.write("|")
    except:
        writeFile.write('No contentid')
        writeFile.write("|")
        print("None contentid")

    try:
        #print(contenttypeid)
        writeFile.write(contenttypeid)
        writeFile.write("|")
    except:
        writeFile.write('No contenttypeid')
        writeFile.write("|")
        print("None contenttypeid")

    try:
        #print(dongCode)
        writeFile.write(dongcode)
        writeFile.write("|")
    except:
        writeFile.write('No dongcode')
        writeFile.write("|")
        print("None dongCode")

    try:
        writeFile.write(firstimage)
        writeFile.write("|")
    except:
        writeFile.write('No firstimage')
        writeFile.write("|")
        print('None firstimage')

    try:
        #print(homepage)
        writeFile.write(homepage)
        writeFile.write("|")
    except:
        writeFile.write('No homepage')
        writeFile.write("|")
        print("None homepage")

    try:
        writeFile.write(maps)
        writeFile.write("|")
    except:
        writeFile.write('No map')
        writeFile.write("|")
        print("None map")

    try:
        writeFile.write(overview)
        writeFile.write("|")
    except:
        writeFile.write('No overview')
        writeFile.write("|")
        print("None overview")

    try:
        writeFile.write(sigungucode)
        writeFile.write("|")
    except:
        writeFile.write('No sigungucode')
        writeFile.write("|")
        print("None sigunguCode")

    try:
        writeFile.write(tel)
        writeFile.write("|")
    except:
        writeFile.write('No tel')
        writeFile.write("|")
        print("None tel")

    try:
        writeFile.write(title)
        writeFile.write("|")
    except:
        writeFile.write('No title')
        writeFile.write("|")
        print("None title")

    try:
        writeFile.write(zipcode)
        writeFile.write("|")
    except:
        writeFile.write('No zipcode')
        writeFile.write("|")
        print("None zipcode")

    try:
        writeFile.write(cat1)
        writeFile.write("|")
    except:
        writeFile.write('No cat1')
        writeFile.write("|")
        print("None cat1")

    try:
        writeFile.write(cat2)
        writeFile.write("|")
    except:
        writeFile.write('No cat2')
        writeFile.write("|")
        print("None cat2")

    try:
        writeFile.write(cat3)
        writeFile.write("|")
    except:
        writeFile.write('No cat3')
        writeFile.write("|")
        print("None cat3")

    try:
        numOfSearchResult = numOfSearchResult.replace(",", "")
        writeFile.write(numOfSearchResult)
        writeFile.write("|")
    except:
        writeFile.write("No numOfSearhResult")
        writeFile.write("|")
        print("None numOfSearchResult")


    writeFile.write('\n')