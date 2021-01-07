from bs4 import BeautifulSoup
import requests
import datetime
import json

i = 10
file = open('crollingResult_Incheon.txt', mode='w', encoding='utf-8')

while (i < 20) :
    info_url = '################'
    i = i + 1
    print(i)
    response = requests.get(info_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('item')

    for item in items:
        try:
            contentID = item.find('contentid')
            file.write(contentID)
            file.write('\n')
        except:
            print('None contentId')

