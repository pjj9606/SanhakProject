from bs4 import BeautifulSoup
import requests
import datetime
import json
"""
관광정보를 긁어오려면 최소 contentID와 contentTypeID가 필요함
contentTypeID에 따라 contentID를 긁어오는 코드
"""
i = 1
file = open('Korean_crollingResult_contentID_레포츠28.txt', mode='w', encoding='utf-8')
contentTypeId = 28
serviceKey = '##################' #운영계정
while (i < 100) :
    #eng
    #info_url = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaBasedList?ServiceKey=' + serviceKey + '&contentTypeId=' + str(contentTypeId) + '=&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&listYN=Y&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&arrange=A&numOfRows=120&pageNo=' + str(i)

    #kor
    info_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=' + serviceKey + '&contentTypeId=' + str(contentTypeId) + '&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&listYN=Y&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&arrange=A&numOfRows=120&pageNo=' + str(i)
    i = i + 1
    response = requests.get(info_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('item')

    for item in items:
        try:
            contentId = item.find('contentid').text
            print(contentId)
            file.write(contentId)
            file.write('\n')
        except :
            print("non contentId")