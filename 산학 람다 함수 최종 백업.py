rom __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
import decimal
import json

#case 문으로 처리하면 너무 코드가 길다
#함수 매개변수로 자연, 리스트(ex[A01010100,A01010200,A01010300])
#를 받아서 검색하는 함수를 만들까 

# cat1(대분류) : 1.관광/2.숙박/3.쇼핑/4.음식
#
# cat2(중분류) : (1.자연/2.인문/3.레포츠)                                                   //관광
#                (1.호텔/2.모텔/3.한옥스테이/4.기타)                                        //숙박
#                (1.전통시장/2.백화점&면세점)                                               //쇼핑
#                (1.한식/2.서양식/3.일식/4.중식/5.채식&기타/6.바&카페)                      //음식
#
# cat3(소분류) : (1.공원/2.산림/3.계곡/4.바다/5.강&호수/6.동굴)                             //관광-자연
#                (1.역사/2.피로회복/3.놀이동산/4.이색체험/5.기타/6.박물관/7.미술관/8.축제)  //관광-인문
#                (1.육상/2.육상겨울/3.수상/4.항공&복합레포츠)                               //관광-레포츠

# cat1이 관광일 경우만 cat3 존재

#관광
    #자연
        #[공원,삼림,계곡,바다,강&호수,동굴]
TourNatureCat3 = [
['A01010100', 'A01010200', 'A01010300'],
['A01010400', 'A01010500', 'A01010600', 'A01010700'],
['A01010800', 'A01010900', 'A01011000'],
['A01011100', 'A01011200', 'A01011300', 'A01011400', 'A01011500', 'A01011600'],
['A01011700', 'A01011800'],
['A01011900', 'A01020200']
]
    #인문
        #[역사, 피로회복, 놀이동산, 이색체험, 기타, 박물관, 미술관, 축제]
TourCultureCat3 = [
['A02010100', 'A02010200', 'A02010300', 'A02010400', 'A02010500', 'A02010600', 'A02010700', 'A02010800', 'A02061100'],
['A02020300', 'A02020400', 'A02020500'],
['A02020600', 'A02020700'],
['A02030200', 'A02030400', 'A02030600', 'A02030100', 'A02030500'],
['A02010900', 'A02011000', 'A02020100', 'A02040600', 'A02040800', 'A02050100', 'A02060900', 'A02061000'],
['A02060100'],
['A02060200', 'A02060300', 'A02060500'],
['A02080100', 'A02080100', 'A02081300', 'A02070100', 'A02070200', 'A02010900']
]
    #레포츠
        #[육상, 육상겨울, 수상, 항공&복합레포츠]
TourLeportsCat3 = [
['A03020500', 'A03020700', 'A03022200', 'A03022400', 'A03022700'],
['A03021200', 'A03021300', 'A03021400'],
['A03030100', 'A03030200', 'A03030300', 'A03030400', 'A03030700', 'A03030800'],
['A03040300', 'A03050100']
]
#숙박
    #[호텔, 모텔, 한옥스테이, 기타]
AccommodationCat2 = [
['B02010100', 'B02010400', 'B02011500'],
['B02010900'],
['B02011600'],
['B02010500', 'B02010600', 'B02010700', 'B02011100', 'B02011200', 'B02011300']
]
#쇼핑
    #[전통시장, 백화점&면세점]
ShoppingCat2 = [
['A04010100', 'A04010200'],
['A04010300', 'A04010400']
]
#음식
    #[한식, 서양식, 일식, 중식, 채식&기타, 바&카페]
FoodCat2 = [
['A05020100'],
['A05020200'],
['A05020300'],
['A05020400'],
['A05020800', 'A05020500', 'A05020700'],
['A05020900']
]

#검색하기 쉽게 한데 모으자
TourTotalCat3 = [TourNatureCat3, TourCultureCat3, TourLeportsCat3]  #아니 이게 되네???

TotalCat = [TourTotalCat3, AccommodationCat2, ShoppingCat2, FoodCat2]   # 1.관광/2.숙박/3.쇼핑/4.음식

dynamodb = boto3.resource('dynamodb')

# areaCode에 따른 테이블 dictionary
SearchTable = {1: 'ChatBotForSearch_Seoul', 2: 'ChatBotForSearch_Incheon', 3: 'ChatBotForSearch_Daejeon', 4: 'ChatBotForSearch_Daegu', 5: 'ChatBotForSearch_Gwangju',
                 6: 'ChatBotForSearch_Busan', 7: 'ChatBotForSearch_Ulsan', 8: 'ChatBotForSearch_Sejong', 31: 'ChatBotForSearch_Gyeonggi_do', 32: 'ChatBotForSearch_Gangwon_do',
                 33: 'ChatBotForSearch_Chungcheongbuk_do', 34: 'ChatBotForSearch_Chungcheongnam_do', 35: 'ChatBotForSearch_Gyeongsangbuk_do', 36: 'ChatBotForSearch_Gyeongsangnam_do', 37:'ChatBotForSearch_Jeollabuk_do',
                 38:'ChatBotForSearch_Jeollanam_do', 39:'ChatBotForSearch_Jeju_do'}


"""
def getContentID(areaCode, contentTypeID):
    
    listContentID = []
    SearchResponse = TableSearch.scan(FilterExpression=Attr('areaCode').eq(areaCode) & Attr('contentTypeID').eq(contentTypeID))
    
    for i in SearchResponse['Items']: 
        listContentID.append(i['contentID'])
        #for i in range(len(listContentID)) :
            #print(listContentID)
    
    return listContentID
    
"""    
"""
def getInformationByContentIDList(listContentID) :
    listTitle = []     #contentID, addr, firstImage, homepage, overview, tel, title
    list = []
    
    for i in listContentID : 
        contentID = i
        InformationResponse = TableInformation.get_item(Key={'contentID': contentID })
        
        listTitle.append(InformationResponse['Item']['title'])                              # 타이틀만
        #print (InformationResponse['Item']['title'])
    
    return listTitle
"""
    
"""   
def getTourInformationByList(listContentID) :

    listTourInformation = []     #contentID, addr, firstImage, homepage, overview, tel, title
    list = []
    index = 0
    
    for i in listContentID : 
        contentID = i
        InformationResponse = TableInformation.get_item(Key={'contentID': contentID })
        #print(InformationResponse)
        listTourInformation.append(InformationResponse)     #뭉탱이로 넣었는데 분류가 필요할듯       필요 없을 것 같기도
        print(InformationResponse)
        for i in InformationResponse['Items']: 
            print(i)
    
    
    return listTourInformation

"""
def getSearchTable(areacode) :
    try:
        return SearchTable[int(areacode)]
    except:
        #No areacode
        return -1


#위에서 같다고 정의한 cat들을 모아 DB를 검색해 리스트에 담아 반환하는 함수, numOfSearchResult에 기반하여 정렬하는 함수를 호출하여 정렬한 뒤 반환?
def getSearchResult(catList, Mytable) :   
    listForSorting = []
    
    for cat in catList:
        
        SearchResponse = Mytable.scan(FilterExpression=Attr('cat3').eq(cat))
    
        for item in SearchResponse['Items']: 
            #if len(listContentID) >= 3 :        # 길이가 너무 길면 시간이 오래 걸려 반환하기 힘들기 때문에 일단 3개만(추후 수정필요) //이제 다 해도 될듯 DBTable하나만 건드리기 때문에 속도가 괜찮음
                #break;
            listForSorting.append([item['contentID'], item['title'], item['numOfSearchResult']])
            
            
    listForSorting = sorted(listForSorting, reverse=True, key=lambda x:x[2])    # numOfSearchResult가 많은 순으로 정렬
    
    
    return listForSorting


    

def lambda_handler (event, context):
    
    try:
        print('Received event: ' + json.dumps(event, indent=2))
    except:
        print("error: Event does not exist")
    
    areaCode = int(event['areaCode'])
    mytable = getSearchTable(areaCode)          # areacode에 따른 테이블 get
    table = dynamodb.Table(mytable)
    
    cat1 = int(event['cat1'])
    cat2 = int(event['cat2'])
    try:                                        # cat3는 없을수도 있으니까
        cat3 = int(event['cat3'])
    except:
        cat3 = None
        
    catList = []                                # 검색에 필요한 카테고리를 모두 넣어두는 리스트
    listAfterSorting = []
    
    if cat3 == None:                            #숙박,쇼핑,음식
        catList = TotalCat[cat1-1][cat2-1]      #인덱스는 0번부터~
        listAfterSorting = getSearchResult(catList, table)

    elif cat3 != None :                         #cat3 != None이면 관광
        catList = TotalCat[cat1-1][cat2-1][cat3-1]
        listAfterSorting = getSearchResult(catList, table)
        
    
    
    #listContentIDTitle = [listContentID, listTitle]
    
    return listAfterSorting
        
    #listContentID = getContentID(areaCode, contentTypeID)
    
    #listTourInformation = getTourInformationByList(listContentID)
    
    #print(listTourInformation)
    #print(listTourInformation[0]['Item']['overview'])   
    #return listTourInformation
    #return listTourInformation[0]['Item']['title'] #이런식으로 title만 return 할 수도 있다.
    
    
