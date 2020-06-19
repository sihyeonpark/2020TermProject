from tkinter import *
from tkinter import font
from tkinter import ttk
from io import BytesIO
import urllib.request
from PIL import  Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





window = Tk()
window.title("약국검색 프로그램")
DataList = []
StarList =[]
window.geometry("800x600") #윈도우 창 크기
window.configure(bg='light blue')
        #폰트가 함수보다 위에 있어야 적용 (family:폰트이름)
fontstyle = font.Font(window, size=24, weight='bold', family='맑은 고딕')
fontstyle2 = font.Font(window, size=12, family='맑은 고딕')


noteBook = ttk.Notebook(window, width = 470, height=110)


frame1 = Frame(window)      #프레임 다르게 설정 - notebook용도
noteBook.place(x=310,y=360)
noteBook.add(frame1,text = "상세정보")
frame2 = Frame(window)
noteBook.add(frame2,text = "즐겨찾기")


def InitTopText():
    Title=Label(window,text="약국검색 프로그램",font=fontstyle)
    Title.configure(bg='light blue')
    Title.place(x=25, y=15)

def InputLabel():
    nameL = Label(window,text="약국명", font=fontstyle2)
    nameL.configure(bg='light blue')
    nameL.place(x=25, y=190)
    L1 = Label(window,text="시/도", font=fontstyle2)
    L1.configure(bg='light blue')
    L1.place(x=25, y=90)
    L2 = Label(window,text="시/구/군", font=fontstyle2)
    L2.configure(bg='light blue')
    L2.place(x=25, y=140)



def InitQ0():   #시/도
    global InitQ0
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    InitQ0 = Entry(window, font=TempFont, width=16, borderwidth=2, relief='ridge')
    InitQ0.pack()
    InitQ0.place(x=100, y=85)

def InitQ1():   #시/구/군
    global InitQ1
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    InitQ1 = Entry(window, font=TempFont, width=16, borderwidth=2, relief='ridge')
    InitQ1.pack()
    InitQ1.place(x=100, y=135)

def InitPharmacyName():
    global InitPharmacyName
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    InitPharmacyName = Entry(window, font=TempFont, width=16, borderwidth=2, relief='ridge')
    InitPharmacyName.pack()
    InitPharmacyName.place(x=100, y=185)


def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, width=7, text="검색", command=SearchButtonAction)

    SearchButton.place(x=208, y=235)
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





                # 0번 : 주소 , 2번 : 이름 , 3번 : 간략한 주소 , 4번 : 전화번호
                DataList.append((subitems[2].firstChild.nodeValue,subitems[0].firstChild.nodeValue,str(subitems[3].firstChild.nodeValue)))



        for i in range(len(DataList)):
            listBox.insert(i,DataList[i][1])




def InitListBox():
    global listBox
    frame = Frame(window)
    listScrollbar = Scrollbar(frame)
    listBox = Listbox(frame, width=65, height=15 , yscrollcommand = listScrollbar.set)
    listScrollbar.config(command=listBox.yview)
    listScrollbar.pack(side="right", fill="y")
    listBox.pack()
    frame.place(x=310,y=85)


def DetailSearchButton():

    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    DetailButton = Button(window, font=TempFont,  width=7,text="자세히", command=loadDetail)

    DetailButton.place(x=208, y=285)

#    SearchButton.pack()

def InitRenderText():
    global RenderText
    RenderText = Text(frame1, width=67, height=10, bg='white', relief='ridge', )
    RenderText.pack()
   # RenderText.place(x=310, y=370)

def loadDetail():   #상세정보창

    RenderText.delete(0.0, END)

    global iSearchIndex
    iSearchIndex = listBox.curselection()[0]

    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, " 약국명:\t")
    RenderText.insert(INSERT, DataList[iSearchIndex][0])
    RenderText.insert(INSERT, "\n\n")

    RenderText.insert(INSERT, " 주소:\t")
    RenderText.insert(INSERT, DataList[iSearchIndex][1])
    RenderText.insert(INSERT, "\n\n")
    '''
    RenderText.insert(INSERT, "\t☞ ")
    RenderText.insert(INSERT, DataList[iSearchIndex][2])
    RenderText.insert(INSERT, "\n\n")
    '''
    RenderText.insert(INSERT, " 전화:\t")
    RenderText.insert(INSERT, DataList[iSearchIndex][2])
    RenderText.insert(INSERT, "\n\n")

def starButton():   #즐겨찾기 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, width=7, text="즐겨찾기", command=inStar)

    SearchButton.place(x=310, y=510)
#    SearchButton.pack()

def InitStar(): #리스트박스랑 스크롤바 frame2에
    global listBox2 #즐겨찾기 list
    listScrollbar = Scrollbar(frame2)
    listBox2 = Listbox(frame2, width=65, height=15 , yscrollcommand = listScrollbar.set)
    listScrollbar.config(command=listBox.yview)
    listScrollbar.pack(side="right", fill="y")
    listBox2.pack()

def inStar():   #즐겨찾기에 넣기
    global StarList

    listBox2.insert(iSearchIndex, DataList[iSearchIndex][0])
    StarList.append((DataList[iSearchIndex][0], DataList[iSearchIndex][1], DataList[iSearchIndex][2]))


def emailButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, width=7, text="메일전송", command=sendInfo)

    SearchButton.place(x=400, y=510)

def sendInfo():

    sendEmail = "qkrtlgus123@gmail.com"
    recvEmail = "sh2joo@naver.com"
    passwoed = "psh9806142"
    msg = MIMEMultipart('alternative')


    msg = MIMEText(MailText)
    msg['Subject']='제목 : 테스트'
    msg['From']= sendEmail
    msg['To'] = recvEmail


    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset = 'UTF-8')

    msg.attach(msgPart)
    msg.attach(bookPart)

    print ("connect smtp server ... ")
    s = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("qkrtlgus123@gmail.com", "psh9806142")
    s.sendmail(sendEmail,recvEmail,msg.as_string().encode('utf-8'))
    s.quit()    #종료료
    print ("Mail sending complete!!!")


InitTopText()
InputLabel()
InitListBox()
InitRenderText()
InitPharmacyName()
InitQ0()
InitQ1()
InitSearchButton()
DetailSearchButton()
starButton()
InitStar()
emailButton()
#loadMap()
#SearchPharmacy()



window.mainloop()