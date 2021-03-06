"""
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


동일 cat 
관광
    자연
        1. 공원
        A01010100 = A01010200 = A01010300
        2. 산림
        A01010400 = A01010500 = A01010600 = A01010700
        3. 계곡
        A01010800 = A01010900 = A01011000
        4. 바다
        A01011100 = A01011200 = A01011300 = A01011400 = A01011500 = A01011600
        5. 강&호수
        A01011700 = A01011800
        6. 동굴
        A01011900 = A01020200
    인문
        1. 역사
        A02010100 = A02010200 = A02010300 = A02010400 = A02010500 = A02010600 = A02010700 = A02010800 = A02061100
        2. 피로회복
        A02020300 = A02020400 = A02020500
        3. 놀이동산&도심공원
        A02020600 = A02020700
        4. 이색체험
        A02030200 = A02030400 = A02030600
        = A02030100 = A02030500 (from 관광)
        5. 기타(종교성지, 안보관람, 유원지, 식음료, 기타)
        A02010900 = A02011000 = A02020100 = A02040600 = A02040800 = A02050100 = A02060900 = A02061000
        6. 박물관
        A02060100
        7. 미술관
        A02060200 = A02060300 = A02060500
        8. 축제(기존의 축제 + 청록색?)
        A02080100 = A02080100 = A02081300 = A02070100 = A02070200 = A02010900
    레포츠
        1. 육상
        A03020500 = A03020700 = A03022200 = A03022400 = A03022700
        2. 육상겨울
        A03021200 = A03021300 = A03021400 
        3. 수상
        A03030100 = A03030200 = A03030300 = A03030400 = A03030700 = A03030800
        4. 항공&복합레포츠
        A03040300 = A03050100
        
숙박
    1. 호텔
    B02010100 = B02010400 = B02011500
    2. 모텔
    B02010900
    3. 한옥스테이
    B02011600
    4. 기타
    B02010500 = B02010600 = B02010700 = B02011100 = B02011200 = B02011300
    
쇼핑
    1. 전통시장
    A04010100 = A04010200
    2. 백화점 & 면세점
    A04010300 = A04010400
    
음식
    1. 한식
    A05020100
    2. 서양식
    A05020200
    3. 일식
    A05020300
    4. 중식
    A05020400
    5. 채식&기타
    A05020800 = A05020500 = A05020700
    6. 바&카페
    A05020900
    
"""
