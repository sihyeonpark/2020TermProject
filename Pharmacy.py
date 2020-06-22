from tkinter import *
from tkinter import font
from tkinter import ttk
from io import BytesIO
import urllib.request
from PIL import  Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import folium
import webbrowser
from folium.plugins import MarkerCluster

window = Tk()
window.title("약국검색 프로그램")
DataList = []
StarList =[]
StarNum = []


window.geometry("800x600") #윈도우 창 크기
import smtplib
window.configure(bg='PaleGreen3')
        #폰트가 함수보다 위에 있어야 적용 (family:폰트이름)
fontstyle = font.Font(window, size=24, weight='bold', family='맑은 고딕')
fontstyle2 = font.Font(window, size=11, family='맑은 고딕')


noteBook = ttk.Notebook(window, width = 375, height=400)
noteBook.place(x=20,y=145)





def InitTopText():
    #Title=Label(window,text="약국검색 프로그램",font=fontstyle)
    #Title.configure(bg='light blue')
    #Title.place(x=25, y=12)

    img = PhotoImage(file='Logo.png')
    lbl = Label(image=img)
    lbl.image = img  # 레퍼런스 추가
    lbl.place(x=0, y=10)


def InputLabel():
    nameL = Label(window,text="약국명", font=fontstyle2)
    nameL.configure(bg='PaleGreen3')
    nameL.place(x=430, y=88)
    L1 = Label(window,text="시/도", font=fontstyle2)
    L1.configure(bg='PaleGreen3')
    L1.place(x=20, y=88)
    L2 = Label(window,text="시/구/군", font=fontstyle2)
    L2.configure(bg='PaleGreen3')
    L2.place(x=210, y=88)



def InitQ0():   #시/도
    global InitQ0
    TempFont = font.Font(window, size=11, family="맑은 고딕")
    InitQ0 = Entry(window, font=TempFont, width=11, relief='ridge')
    InitQ0.pack()
    InitQ0.place(x=70, y=90)

def InitQ1():   #시/구/군
    global InitQ1
    TempFont = font.Font(window, size=11, family="맑은 고딕")
    InitQ1 = Entry(window, font=TempFont, width=11, relief='ridge')
    InitQ1.pack()
    InitQ1.place(x=280, y=90)

def InitPharmacyName():
    global InitPharmacyName
    TempFont = font.Font(window, size=11,  family="맑은 고딕")
    InitPharmacyName = Entry(window, font=TempFont, width=11,  relief='ridge')
    InitPharmacyName.pack()
    InitPharmacyName.place(x=490, y=90)


def InitSearchButton():
    TempFont = font.Font(window, size=10,weight='bold', family="맑은 고딕")
    SearchButton = Button(window, bg='white', font=TempFont, width=7, text="검색", command=SearchButtonAction)

    SearchButton.place(x=630, y=88)
#    SearchButton.pack()

def SearchButtonAction():
    #RenderText.configure(state='normal')
    #RenderText.delete(0.0, END)
    listBox.configure(state='normal')
    listBox.delete(0,END)
    SearchPharmacy()
    #RenderText.configure(state='disabled')

def SearchPharmacy():
    import urllib
    import http.client
    from xml.dom.minidom import parse, parseString



    q0 = urllib.parse.quote(InitQ0.get())

    pharmacyName = urllib.parse.quote(InitPharmacyName.get())

    q1 = urllib.parse.quote(InitQ1.get())


    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET",
                 "/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=8XK%2Bij2DKNI36pf9ut8UMhJv3qdDqq8FbA8cZpBvnRFxFYUGAztnNNXsa2mCM%2B2Pf40yOmEqxvtmeUW7LzAmTQ%3D%3D&Q0="+q0+"&Q1="+q1+"&QN="+pharmacyName+"&numOfRows=5000")
                #  "/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=8XK%2Bij2DKNI36pf9ut8UMhJv3qdDqq8FbA8cZpBvnRFxFYUGAztnNNXsa2mCM%2B2Pf40yOmEqxvtmeUW7LzAmTQ%3D%3D&Q0="+address1+"&Q1="+address2+"&pageNo=1&numOfRows=1")
    req = conn.getresponse()
    global DataList
    global listBox
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

                    if subitems[i].nodeName == "wgs84Lat":
                        temp = subitems[4]
                        subitems[4] = subitems[i]
                        subitems[i] = temp

                    if subitems[i].nodeName == "wgs84Lon":
                        temp = subitems[5]
                        subitems[5] = subitems[i]
                        subitems[i] = temp

                # 0번 : 주소 , 2번 : 이름 , 3번 : 간략한 주소 , 4번 : 전화번호
                DataList.append((subitems[2].firstChild.nodeValue,subitems[0].firstChild.nodeValue,str(subitems[3].firstChild.nodeValue),subitems[4].firstChild.nodeValue,subitems[5].firstChild.nodeValue))



        for i in range(len(DataList)):
            listBox.insert(i,DataList[i][1])



def InitListBox():

    global listBox

    flag=0

    frame1 = Frame(window)
    noteBook.add(frame1, text="약국 목록")
    listScrollbar = Scrollbar(frame1)
    listBox = Listbox(frame1, width=65, height=75 , yscrollcommand = listScrollbar.set)
    listScrollbar.config(command=listBox.yview)
    listScrollbar.pack(side="right", fill="y")
    listBox.bind('<Double-1>',loadDetail)
    listBox.pack()

   # frame1.place()



def InitRenderText():
    global RenderText


    RenderText = Text(window, width=50, height=11, bg='white', relief='ridge', )

    RenderText.place(x=430, y=145)

def loadDetail(event):   #상세정보창
    global indexNum


    RenderText.delete(0.0, END)
    print(listBox.curselection()[0])
    indexNum = listBox.curselection()[0]



    RenderText.insert(INSERT, "\n\n")
    RenderText.insert(INSERT, " 약국명:\t")
    RenderText.insert(INSERT, DataList[indexNum][0])
    RenderText.insert(INSERT, "\n\n\n")

    RenderText.insert(INSERT, " 주소:\t")
    RenderText.insert(INSERT, DataList[indexNum][1])
    RenderText.insert(INSERT, "\n\n\n")
    '''
    RenderText.insert(INSERT, "\t☞ ")
    RenderText.insert(INSERT, DataList[indexNum][2])
    RenderText.insert(INSERT, "\n\n")
    '''
    RenderText.insert(INSERT, " 전화:\t")
    RenderText.insert(INSERT, DataList[indexNum][2])
    RenderText.insert(INSERT, "\n\n")


def starButton():   #즐겨찾기 버튼
    TempFont = font.Font(window, size=11, family='Consolas')
    SearchButton = Button(window, font=TempFont, bg='white',width=7, text="즐겨찾기", command=inStar)

    SearchButton.place(x=430, y=340)
#    SearchButton.pack()

def InitStar(): #리스트박스랑 스크롤바 frame2에
    global listBox2 #즐겨찾기 list

    frame2 = Frame(window)
    noteBook.add(frame2, text="즐겨찾기")
    listScrollbar = Scrollbar(frame2)
    listBox2 = Listbox(frame2, width=65, height=75 , yscrollcommand = listScrollbar.set)
    listScrollbar.config(command=listBox.yview)
    listScrollbar.pack(side="right", fill="y")

    listBox2.bind('<Double-1>',loadDetail2)
    listBox2.pack()




def inStar():   #즐겨찾기에 넣기
    global StarList
    global StarNum

    listBox2.insert(indexNum, DataList[indexNum][0])
    StarList.append((DataList[indexNum][0], DataList[indexNum][1], DataList[indexNum][2]))

def loadDetail2(event):   #상세정보창
    global indexNum


    RenderText.delete(0.0, END)
    indexNum = listBox2.curselection()[0]



    RenderText.insert(INSERT, "\n\n\n")
    RenderText.insert(INSERT, " 약국명:\t")
    RenderText.insert(INSERT, StarList[indexNum][0])
    RenderText.insert(INSERT, "\n\n")

    RenderText.insert(INSERT, " 주소:\t")
    RenderText.insert(INSERT, StarList[indexNum][1])
    RenderText.insert(INSERT, "\n\n")
    '''
    RenderText.insert(INSERT, "\t☞ ")
    RenderText.insert(INSERT, DataList[indexNum][2])
    RenderText.insert(INSERT, "\n\n")
    '''
    RenderText.insert(INSERT, " 전화:\t")
    RenderText.insert(INSERT, StarList[indexNum][2])
    RenderText.insert(INSERT, "\n\n")

def mapButton():
    TempFont = font.Font(window, size=11, family='Consolas')
    MapButton = Button(window, font=TempFont, width=7, bg='white',text="지도보기", command=openMap)
    MapButton.place(x=520, y=340)

def openMap():
    map_osm = folium.Map(location=[DataList[indexNum][3],DataList[indexNum][4]], zoom_start=13)
 #   folium.Marker([DataList[indexNum][3],DataList[indexNum][4]],popup=DataList[indexNum][0]).add_to(map_osm)
    folium.Marker([DataList[indexNum][3],DataList[indexNum][4]]).add_to(map_osm)
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')


def emailButton():
    TempFont = font.Font(window, size=10,weight='bold', family="맑은 고딕")
    SearchButton = Button(window, font=TempFont, width=7, bg='white', text="메일전송", command=sendInfo)

    SearchButton.place(x=620, y=383)

def emailLabel():   #시/구/군
    global emailL
    TempFont = font.Font(window, size=13, family="맑은 고딕")
    infoFont = font.Font(window, size=9,  family="맑은 고딕")
    emailL = Entry(window, font=TempFont, width=20, relief='ridge')
    emailL.pack()
    emailL.place(x=430, y=384)
    infoL = Label(window, text="* 메일주소를 입력하세요", font = infoFont,  fg="white")
    infoL.configure(bg='PaleGreen3')
    infoL.place(x=430, y=412)

def sendInfo():
    sendEmail = "qkrtlgus123@gmail.com"
    recvEmail = emailL.get()
    password = "psh9806142"


    msg = MIMEMultipart()
    msg['Subject'] = '<Pharmacy Search Program> '+DataList[indexNum][0]+" 정보입니다."
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    msg.attach(MIMEText("약국명 : "+ DataList[indexNum][0]+'\n주소 : '+DataList[indexNum][1] + '\n전화번호 : ' + DataList[indexNum][2], 'plain'))


  #  text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendEmail, password)

    server.sendmail(sendEmail,recvEmail, msg.as_string())
    server.quit()

    print("메일 전송 성공")


InitTopText()
InputLabel()
InitListBox()
InitRenderText()
InitPharmacyName()
InitQ0()
InitQ1()
InitSearchButton()
starButton()
InitStar()
emailButton()
mapButton()
#loadMap()
#SearchPharmacy()
emailLabel()


window.mainloop()