"가공된 파일들을 번역해서 다시 텍스트문서로"
import json
import urllib.request

r = open('RemoveNewLine/Kor_음식점39_removeNewLine.txt', mode='rt', encoding='utf-8')
writeFile = open('Translated/TransToENG_Kor_음식점39.txt', mode='w', encoding='utf-8')
numOfContentID = 5158
i=0

def getTranslatedText(text) :
    """
    {
    "message":{
    	"@type":"response",
    	"@service":"naverservice.nmt.proxy",
    	"@version":"1.0.0",
    	"result":{
    		srcLangType":"ko","tarLangType":"en","translatedText":"Please enter a sentence to translate"
        }
      }
    }
    """
    client_id = "#####"
    client_secret = "##########"
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        response_body = json.loads(response_body) # dict 형식으로 바꾸고

        print(response_body["message"]["result"]['translatedText'])
        return response_body["message"]["result"]['translatedText']
        #print(response_body)
    else:
        print("Error Code:" + rescode)

def readUntilOr(variable):
    text = r.read(1)
    buffer = ''
    while (text != '|'):
        buffer = str(buffer) + text
        text = r.read(1)
    variable = buffer
    return variable


while(i < numOfContentID) :
    addr1 = None; areacode = None; contentid = None; contenttypeid = None; dongcode = None; firstimage = None;
    homepage = None; maps = None; overview = None; sigungucode = None; tel = None; title = None; zipcode = None;
    cat1 = None; cat2 = None; cat3 = None; numOfSearchResult = None;

    print("_____________NEW________________________")
    i = i+1
    print(i)

    addr1 = readUntilOr(addr1)

    #print("addr1 :", addr1)
    #count_OR = count_OR + 1

    areacode = readUntilOr(areacode)
    #print("areacode: ",areacode)
    #count_OR = count_OR + 1

    contentid = readUntilOr(contentid)
    print("contentid: ", contentid)
    #count_OR = count_OR + 1

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

    if(overview=='') :
        overview = "No overview"

    #count_OR = count_OR + 1

    sigungucode = readUntilOr(sigungucode)
    #print("sigungucode: ", sigungucode)
    #count_OR = count_OR + 1

    tel = readUntilOr(tel)
    #print("tel: ", tel)
    #count_OR = count_OR + 1

    title = readUntilOr(title)
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

    numOfSearchResult = readUntilOr(numOfSearchResult)
    print("numOfSearchResult: ", numOfSearchResult)

    r.read(1)   #줄바꿈문자
    #여기까지 read

    #파파고 API가 가~끔 제대로 호출이 안됨
    #*!처리 해놓고 끝나면 바꿔야 할듯
    try:
        addr1 = getTranslatedText(addr1)
    except:
        addr1 = "*!"
    try:
        overview = getTranslatedText(overview)
    except:
        overview = "*!"
    try:
        title = getTranslatedText(title)
    except:
        title = "*!"

    print(addr1)
    print("overview: ", overview)
    print("title: ", title)
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
        writeFile.write(numOfSearchResult)
        writeFile.write("|")
    except:
        writeFile.write("No numOfSearhResult")
        writeFile.write("|")
        print("None numOfSearchResult")


    writeFile.write('\n')