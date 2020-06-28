import telepot
import os
import time
from urllib.request import urlopen



token = '1251352869:AAHY_ZiBXNjn-F1r31XufN1AMRYuNLJIUDA'
mc = '1251352869'
bot = telepot.Bot(token)

status = True


def handle(msg):
    content, chat, id = telepot.glance(msg)

    text = msg['text']
    args = text.split(',')

    if content == 'text':

        if len(args) == 3:
            InfoL = SearchPharmacy(args)
            if len(InfoL) >= 1:
                bot.sendMessage(id, '약국 목록을 출력합니다.')
                for i in range(len(InfoL)):
                    bot.sendMessage(id,"약국명 : " +InfoL[i][0]+"\n"+"주소 : "+InfoL[i][1]+"\n"+"전화번호 : "+InfoL[i][2])
            elif len(InfoL) == 0:
                bot.sendMessage(id,"검색 결과가 없습니다.")
        else:
            bot.sendMessage(id, "안녕하세요! 약국 검색 프로그램입니다.")
            bot.sendMessage(id, '시/도 , 시/구/군, 약국명을 입력하세요.')




def SearchPharmacy(args):
    import urllib
    import http.client
    from xml.dom.minidom import parse, parseString



    q0 = urllib.parse.quote(args[0])

    pharmacyName = urllib.parse.quote(args[2])

    q1 = urllib.parse.quote(args[1])

    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET",
                 "/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=8XK%2Bij2DKNI36pf9ut8UMhJv3qdDqq8FbA8cZpBvnRFxFYUGAztnNNXsa2mCM%2B2Pf40yOmEqxvtmeUW7LzAmTQ%3D%3D&Q0="+q0+"&Q1="+q1+"&QN="+pharmacyName+"&numOfRows=100")
                #  "/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=8XK%2Bij2DKNI36pf9ut8UMhJv3qdDqq8FbA8cZpBvnRFxFYUGAztnNNXsa2mCM%2B2Pf40yOmEqxvtmeUW7LzAmTQ%3D%3D&Q0="+address1+"&Q1="+address2+"&pageNo=1&numOfRows=1")
    req = conn.getresponse()
    DataList=[]
    DataList.clear()


    print(req.status, req.reason)

    if int(req.status == 200):  # req.status가 200이면 연결 완료!
        # cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
      #  print("출력")

      #  print(parseString(req.read().decode('utf-8')).toprettyxml())

        pharmacyData = req.read().decode('utf-8')  # 데이터를 한글로 읽기
        parseData = parseString(pharmacyData)
        response = parseData.childNodes
        body = response[0].childNodes  # response의 childNodes = body
        real = body[1].childNodes
        total = real[3].childNodes
        realx2 = real[0].childNodes #childNodes = 현재 요소의 자식을 배열로 표현
       # realx3 = realx2[0].childNodes



        subitems =[]
        temp = []

        for item in realx2:
            if item.nodeName == "item": #item을 찾으면
                subitems = item.childNodes

              #  print(subitems[0])

             #   print(subitems[3].firstChild.nodeValue) #firstChild: 첫번째 자식 노드 nodeValue:노드 값
                for i in range(len(subitems)):
                    '''
                    if subitems[i].nodeName == "dutyMapimg": #node이름이 dutyMapimg이면 = 간략한 주소
                        temp = subitems[1]
                        subitems[1] = subitems[i]
                        subitems[i] = temp
                    '''
                    if subitems[i].nodeName == "dutyName": #node이름이 dutyName이면 = 약국이름
                        temp = subitems[2]
                        subitems[2] = subitems[i] #2번째 칸으로 옮김
                        subitems[i] = temp

                    if subitems[i].nodeName == "dutyTel1": #node이름이 dutyTel1이면 = 전화번호
                        temp = subitems[3]
                        subitems[3] = subitems[i]   #3번째 칸으로 옮김
                        subitems[i] = temp


                # 0번 : 주소 , 2번 : 이름 , 3번 : 간략한 주소 , 4번 : 전화번호
                DataList.append((subitems[2].firstChild.nodeValue,subitems[0].firstChild.nodeValue,str(subitems[3].firstChild.nodeValue)))

        return DataList



bot.message_loop(handle)

while status ==True:
    time.sleep(10)