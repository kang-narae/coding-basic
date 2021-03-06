# 옥션TV :  평점 4.5이상, 후기 200개이상 구매 500명 이상 구매한 상품만 출력하시오. (제목, 가격, 평점, 리뷰.)

import requests
import re
from bs4 import BeautifulSoup

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv&f=bs:b&k=32&p=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 1차 xpath내용으로 검색 ://*[@id="section--inner_content_body_container"]/div[2]/div[1]/div/div[2]

div1 = soup.find("div",{"id":"section--inner_content_body_container"})
itemcards = div1.find_all("div",{"class":"itemcard"})
for itemcard in itemcards:
    title = itemcard.find("span",{"class":"text--title"}).get_text()
    price = itemcard.find("strong",{"class":"text--price_seller"}).get_text()
    rate = itemcard.find("div",{"class":"seller_awards"})
    if rate:
        titlerate = rate["title"]   #rate에서 title속성의 값만 뽑아낸다.
        intrate = re.sub(r'[^0-9.]','',titlerate) 
        # 정규표현식 re 쓰자.  0-9가 아닌 문자는 ''뽑아내어(sub) ''없앤다, titlerate의 값에서. 그게 intrate이다.
        if float(intrate)>=4.5:
            pass
        else:
            continue
    else:
        # print("평점 없음")
        continue
    review = itemcard.find("span",{"class":"text--reviewcnt"}).get_text()
    intreview = re.sub(r'[^0-9]','',review)
    #마찬가지로, intreview는 review의 문자열 중 0-9가 아닌 값을 sub추출해서 ''없앤 것.
    if int(intreview) >= 200:
        pass
    else:
        continue
    # 문자에서 숫자만 남기고 문자는 모두 제거 하는 함수
    # 문자열을 1개씩 일어와서 [^0-9] 0-9까지의 숫자를 비교해서 아니면 빈공백 처리
    # sub()는 string에서 pattern과 일치하는 문자들을 해당형태로 교체
    # re.sub(pattern, repl, string)   [^a-zA-Z]
    # intprice = re.sub(r'[^0-9]','',price)
   
    print("제목 : ",title)
    print("바뀌기 전 가격 : ",price)
    print("평점 : ",intrate)
    print("리뷰 : ",intreview)
    print("-"*30)