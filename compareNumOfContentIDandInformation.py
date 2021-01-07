"""
검사하는 코드
contentTypeID로 데이터를 긁어오고도 개수가 정확히 맞지 않는 경우가 있는데
Information.txt에 기록된 contentID와 contentID.txt에 기록된 contentID를 하나하나 순서대로 대조시켜서
파일 끝까지 문제 없으면 잘 긁혀진 것
"""

r = open('Crolling Result Removed Tag/temp_Korean_레포츠28.txt', mode='rt', encoding='utf-8')
whyId = open('Korean_crollingResult_contentID_레포츠28.txt', mode='rt', encoding='utf-8') # contentID로 정보를 긁어오는데 ID와 맞지 않는경우가 있음, 검사하기 위해 사용
numOfContentID = 50000
i = 0

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
    cat1 = None; cat2 = None; cat3 = None;



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

    #검사 하는 코드

    ID = whyId.readline()

    if int(ID) == int(contentid):
        print("같음")
    else:
        print("다름")
        print("originalID :" , ID)
        break


    contenttypeid = readUntilOr(contenttypeid)
    dongcode = readUntilOr(dongcode)
    firstimage = readUntilOr(firstimage)
    homepage = readUntilOr(homepage)
    maps = readUntilOr(maps)
    overview = readUntilOr(overview)
    if(overview=='') :
        overview = "No overview"
    sigungucode = readUntilOr(sigungucode)
    tel = readUntilOr(tel)
    title = readUntilOr(title)
    print("title: ", title)

    zipcode = readUntilOr(zipcode)

    cat1 = readUntilOr(cat1)
    cat2 = readUntilOr(cat2)
    cat3 = readUntilOr(cat3)

    r.read(1)   #줄바꿈문자
    #여기까지 read

