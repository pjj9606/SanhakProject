from bs4 import BeautifulSoup
import requests
import time

"""contentID를 기반으로 관광정보를 크롤링 하는 코드"""
#남은거    75 76 77 78 79 80
#한것 82 85 80


# 콘텐트 아이디 개수와 공공 데이터포털 개수와 비교 하고 부족하면 ID 먼저 긁고
# 정보를 다시 빠짐없이 긁고(removeTag)도
# 개수 맞나 확인하고 googleCrolling
# 하고도 개수 맞나 확인해야함
# 왜 끝에 몇개가 안긁히지 # i 수를 정확히 하면 됨

#여기를 바꿔야 크롤링
serviceKey = '###################' #운영계정
r = open('Korean_crollingResult_contentID_레포츠28.txt', mode='rt', encoding='utf-8')
#writeFile = open('crollingResult_Total_Festival85.txt', mode='w', encoding='utf-8')
writeFile = open('temp_Korean_레포츠28.txt', mode='w', encoding='utf-8')
contentType = 28
numOfContentID = 1426 # 이 수를 정확히 입력해야 텍스트파일에 끝까지 입력됨
i = 0




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

while(i<numOfContentID) : #개수를 정확히 해야 끝까지 텍스트파일에 기록이 되네
    #time.sleep(0.5)
    #파일 한줄 씩 읽고
    i = i + 1
    contentID = r.readline()
    contentID = contentID.rstrip('\n')

    #Kor
    info_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?ServiceKey=' + serviceKey + '&contentTypeId=' + str(contentType) + '&contentId=' + str(contentID) + '&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&transGuideYN=Y'
    #Eng
    #info_url = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/detailCommon?ServiceKey=' + serviceKey + '&contentTypeId=' + str(contentType) + '&contentId=' + str(contentID) + '&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&transGuideYN=Y'

    print("__________",i,"___________")

    try:
        response = requests.get(info_url)
    except:
        continue
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('item')

    for item in items:
        try:
            addr1 = item.find('addr1').text
            addr1 = removeTag(addr1)
            print("addr1: " + addr1)
            writeFile.write(addr1)
            writeFile.write("|")
        except:
            writeFile.write('No addr1')
            writeFile.write("|")
            print("None addr1")

        try:
            areaCode = item.find('areacode').text
            print("areaCode: " + areaCode)
            writeFile.write(areaCode)
            writeFile.write("|")
        except:
            writeFile.write('No areacode')
            writeFile.write("|")
            print("None areaCode")

        try:
            contentid2 = item.find('contentid').text
            print("contentID: " + contentid2)
            writeFile.write(contentid2)
            writeFile.write("|")
        except:
            writeFile.write('No contentid')
            writeFile.write("|")
            print("None contentid")

        try:
            contenttypeid = item.find('contenttypeid').text
            print("contentTypeID: " + contenttypeid)
            writeFile.write(contenttypeid)
            writeFile.write("|")
        except:
            writeFile.write('No contenttypeid')
            writeFile.write("|")
            print("None contenttypeid")

        try:
            dongCode = item.find('dongcode').text
            print("dongCode: " + dongCode)
            writeFile.write(dongCode)
            writeFile.write("|")
        except:
            writeFile.write('No dongcode')
            writeFile.write("|")
            print("None dongCode")

        try:
            firstimage = item.find('firstimage').text
            print("firstImage: " + firstimage)
            writeFile.write(firstimage)
            writeFile.write("|")
        except:
            writeFile.write('No firstimage')
            writeFile.write("|")
            print('None firstimage')

        try:
            homepage = item.find('homepage').text
            homepage = readHomepage(homepage)
            homepage = removeTag(homepage)
            print("homepage: " + homepage)
            writeFile.write(homepage)
            writeFile.write("|")
        except:
            writeFile.write('No homepage')
            writeFile.write("|")
            print("None homepage")

        try:
            mapx = item.find('mapx').text
            mapy = item.find('mapy').text
            print(mapx, mapy)
            writeFile.write(mapx)
            writeFile.write(',')
            writeFile.write(mapy)
            writeFile.write("|")
        except:
            writeFile.write('No map')
            writeFile.write("|")
            print("None map")

        try:
            overview = item.find('overview').text
            overview = removeTag(overview)
            print(overview)
            writeFile.write(overview)
            writeFile.write("|")
        except:
            writeFile.write('No overview')
            writeFile.write("|")
            print("None overview")

        try:
            sigunguCode = item.find('sigungucode').text
            print("sigunguCode:" + sigunguCode)
            writeFile.write(sigunguCode)
            writeFile.write("|")
        except:
            writeFile.write('No sigungucode')
            writeFile.write("|")
            print("None sigunguCode")

        try:
            tel = item.find('tel').text
            tel = removeTag(tel)
            print("tel: " + tel)
            writeFile.write(tel)
            writeFile.write("|")
        except:
            writeFile.write('No tel')
            writeFile.write("|")
            print("None tel")

        try:
            title = item.find('title').text
            print("title: " + title)
            writeFile.write(title)
            writeFile.write("|")
        except:
            writeFile.write('No title')
            writeFile.write("|")
            print("None title")

        try:
            zipcode = item.find('zipcode').text
            print("zipCode: " + zipcode)
            writeFile.write(zipcode)
            writeFile.write("|")
        except:
            writeFile.write('No zipcode')
            writeFile.write("|")
            print("None zipcode")

        try:
            cat1 = item.find('cat1').text
            print("cat1: " + cat1)
            writeFile.write(cat1)
            writeFile.write("|")
        except:
            writeFile.write('No cat1')
            writeFile.write("|")
            print("None cat1")

        try:
            cat2 = item.find('cat2').text
            print("cat2: " + cat2)
            writeFile.write(cat2)
            writeFile.write("|")
        except:
            writeFile.write('No cat2')
            writeFile.write("|")
            print("None cat2")

        try:
            cat3 = item.find('cat3').text
            print("cat3: " + cat3)
            writeFile.write(cat3)
            writeFile.write("|")
        except:
            writeFile.write('No cat3')
            writeFile.write("|")
            print("None cat3")


        writeFile.write('\n')



