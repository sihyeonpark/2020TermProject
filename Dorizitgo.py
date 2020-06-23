from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random



class Dorizitgo:

    dealnum=0
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("900x600")
        self.window.configure(bg ='green')
        #wall = PhotoImage(file="cards/tablereal.gif")
        #self.wall_label = Label(image=wall)
        #self.wall_label.place(x=0,y=0)
        #self.wall_label.pack()
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")
        #self.dealer = Player("dealer")
        self.main = Player("main")

        self.betMoney = 0
        self.totalMoney = 1000
        self.player1Money = 0
        self.player2Money = 0
        self.player3Money = 0
        self.nCardsDealer = 0
        self.nCardsPlayer = 0
        self.nCardsMain =0
        self.playerScore =0
        self.dealerScore =0
        self.LcardsP1Point=[]
        self.LcardsPlayer1 = [] #라벨카드플레이어
        self.LcardsPlayer2 = []  # 라벨카드플레이어
        self.LcardsPlayer3 = []  # 라벨카드플레이어
        self.Lp1Point = []
        self.Lp2Point = []
        self.Lp3Point=[]
        self.LmPoint=[]
        self.LcardsP1Point =[]
        self.LcardsP2Point = []
        self.LcardsP3Point = []
        self.LcardsMPoint = []
        #self.LcardsDealer = [] #라벨카드딜러
        self.LcardsMain=[] #메인화면에 둘 카드
        self.deckN = 0  #52장 중 첫번째
       # self.imageE = PhotoImage(file="cards/green.png")
        self.setupLabel()
        self.setupButton()

        self.window.mainloop()

    def setupLabel(self):
        self.LtotalMoney = Label(text="1000만원", width=7, height=1, bg='green', font=self.fontstyle, fg="blue")
        self.LtotalMoney.place(x=740, y=460)

        self.Lplayer1Money = Label(text="0만", width=6, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.Lplayer1Money.place(x=85, y=480)

        self.Lplayer2Money = Label(text="0만", width=6, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.Lplayer2Money.place(x=295, y=480)

        self.Lplayer3Money = Label(text="0만", width=6, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.Lplayer3Money.place(x=505, y=480)

        self.Lplayer1Status = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.Lplayer1Status.place(x=20, y=280)

        self.Lplayer2Status = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.Lplayer2Status.place(x=250, y=280)

        self.Lplayer3Status = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.Lplayer3Status.place(x=470, y=280)

        self.LmainStatus = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.LmainStatus.place(x=170, y=70)

        self.Lplayer1wlStatus = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer1wlStatus.place(x=20, y=250)

        self.Lplayer2wlStatus = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer2wlStatus.place(x=250, y=250)

        self.Lplayer3wlStatus = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lplayer3wlStatus.place(x=470, y=250)


    def setupButton(self):
        self.p1_5 = Button(self.window, text="5만", width=3, height=1, font=self.fontstyle2, command=self.p1Bet_5)
        self.p1_5.place(x=90,y=540)
        self.p1_1 = Button(self.window, text="1만", width=3, height=1, font=self.fontstyle2, command=self.p1Bet_1)
        self.p1_1.place(x=150, y=540)

        self.p2_5 = Button(self.window, text="5만", width=3, height=1, font=self.fontstyle2, command=self.p2Bet_5)
        self.p2_5.place(x=300, y=540)
        self.p2_1 = Button(self.window, text="1만", width=3, height=1, font=self.fontstyle2, command=self.p2Bet_1)
        self.p2_1.place(x=360, y=540)

        self.p3_5 = Button(self.window, text="5만", width=3, height=1, font=self.fontstyle2, command=self.p3Bet_5)
        self.p3_5.place(x=510, y=540)
        self.p3_1 = Button(self.window, text="1만", width=3, height=1, font=self.fontstyle2, command=self.p3Bet_1)
        self.p3_1.place(x=570, y=540)

        self.Deal = Button(self.window, text="Deal", width=4, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=730, y=540)
        self.Again = Button(self.window, text="Again", width=5, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=800, y=540)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def p1Bet_5(self):

        self.player1Money += 5
        self.Lplayer1Money.configure(text=str(self.player1Money)+"만")

        self.totalMoney -= 5
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def p2Bet_5(self):

        self.player2Money += 5
        self.Lplayer2Money.configure(text=str(self.player2Money)+"만")

        self.totalMoney -= 5
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def p3Bet_5(self):

        self.player3Money += 5
        self.Lplayer3Money.configure(text=str(self.player3Money)+"만")

        self.totalMoney -= 5
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def p1Bet_1(self):

        self.player1Money += 1
        self.Lplayer1Money.configure(text=str(self.player1Money)+"만")

        self.totalMoney -= 1
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def p2Bet_1(self):

        self.player2Money += 1
        self.Lplayer2Money.configure(text=str(self.player2Money)+"만")

        self.totalMoney -= 1
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def p3Bet_1(self):

        self.player3Money += 1
        self.Lplayer3Money.configure(text=str(self.player3Money)+"만")

        self.totalMoney -= 1
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")

        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"

    def pressedDeal(self):
        if (self.dealnum == 0):
            self.player1.reset()  # 가진 카드 리스트 클리어, 카드 갯수 0
            self.player2.reset()
            self.player3.reset()
            self.main.reset()
            self.cardDeck = [i for i in range(48)]
            random.shuffle(self.cardDeck)
            self.deckN = 0

            self.p1Card(0)
            self.p2Card(0)
            self.p3Card(0)
            self.mCard(0)

        elif (self.dealnum == 1):
            for i in range(1,4):
                self.p1Card(i)
                self.p2Card(i)
                self.p3Card(i)
                self.mCard(i)
        else:
            self.p1Card(4)
            self.p2Card(4)
            self.p3Card(4)
            self.mCard(4)
            self.checkWinner()

        self.dealnum += 1

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'



    def p1Card(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer1.append(Label(self.window, bd=0, image=p))

        self.LcardsPlayer1[self.player1.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p
        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + n * 32, y=350)

        self.LcardsP1Point.append(newCard.getValue())

        self.Lp1Point.append(Label(self.window, width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white"))
        self.Lp1Point[n].config(text=self.LcardsP1Point[n])
        self.Lp1Point[n].place(x=60 + n * 32, y=320)

    def p2Card(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer2.append(Label(self.window, bd=0, image=p))

        self.LcardsPlayer2[self.player2.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p
        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=260 + n * 32, y=350)

        self.LcardsP2Point.append(newCard.getValue())

        self.Lp2Point.append(Label(self.window, width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white"))
        self.Lp2Point[n].config(text=self.LcardsP2Point[n])
        self.Lp2Point[n].place(x=270 + n * 32, y=320)


    def p3Card(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer3.append(Label(self.window, bd=0, image=p))

        self.LcardsPlayer3[self.player3.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p
        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=470 + n * 32, y=350)

        self.LcardsP3Point.append(newCard.getValue())

        self.Lp3Point.append(Label(self.window, width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white"))
        self.Lp3Point[n].config(text=self.LcardsP3Point[n])
        self.Lp3Point[n].place(x=480 + n * 32, y=320)

    #    self.P3PointLabel.configure(text=self.LcardsP3Point[n])
    #    self.P3PointLabel.place(x=480 + n * 32, y=320)




    def mCard(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.main.addCard(newCard)

        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.LcardsMain.append(Label(self.window, bd=0, image=p))

        self.LcardsMain[self.main.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsMain[self.main.inHand() - 1].image = p
        self.LcardsMain[self.main.inHand() - 1].place(x=170 + n * 32, y=140)

        self.LcardsMPoint.append(newCard.getValue())

        self.LmPoint.append(Label(self.window, width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white"))

        self.LmPoint[n].config(text=self.LcardsMPoint[n])

    def scoreCheck(self,status,point):
        plusStatus = "하이"


        self.tempNumList = [0 for _ in range(12)]

        for i in range(1,len(point)+1):
            num = point[i-1]
            self.tempNumList[num-1] = point.count(num)

        for i in range(5):
            for j in range(5):
                if i!=j:
                    if point[i] == 8 and point[j] == 3:
                        plusStatus = "38광땡"
                        self.playerScore = 21
                    elif (point[i] == 1 and point[j] == 3) or (point[i] == 1 and point[i] == 8):
                        plusStatus = "광땡"
                        self.playerScore = 20
                    elif point[i] == 10 and point[j] == 10:
                        plusStatus = "장땡"
                        self.playerScore = 19
                    elif point[i] == 9 and point[j] == 9:
                        plusStatus = "구땡"
                        self.playerScore = 18
                    elif point[i] == 8 and point[j] == 8:
                        plusStatus = "팔땡"
                        self.playerScore = 17
                    elif point[i] == 7 and point[j] == 7:
                        plusStatus = "칠땡"
                        self.playerScore = 16
                    elif point[i] == 6 and point[j] == 6:
                        plusStatus = "육땡"
                        self.playerScore = 15
                    elif point[i] == 5 and point[j] == 5:
                        plusStatus = "오땡"
                        self.playerScore = 14
                    elif point[i] == 4 and point[j] == 4:
                        plusStatus = "사땡"
                        self.playerScore = 13
                    elif point[i] == 3 and point[j] == 3:
                        plusStatus = "삼땡"
                        self.playerScore = 12
                    elif point[i] == 2 and point[j] == 2:
                        plusStatus = "이땡"
                        self.playerScore = 11
                    elif point[i] == 1 and point[j] == 1:
                        plusStatus = "삥땡"
                        self.playerScore = 10

                    elif point[i]+point[j] == 8 or point[i]+point[j]==18:
                        plusStatus = "여덟끗"
                        self.playerScore = 9
                    elif point[i] + point[j] == 7 or point[i]+point[j]==17:
                        plusStatus = "일곱끗"
                        self.playerScore = 8
                    elif point[i]+point[j] == 6 or point[i]+point[j]==16:
                        plusStatus = "여섯끗"
                        self.playerScore = 7
                    elif point[i]+point[j] == 5 or point[i]+point[j]==15:
                        plusStatus = "다섯끗"
                        self.playerScore = 6
                    elif point[i]+point[j] == 4 or point[i]+point[j]==14:
                        plusStatus = "네끗"
                        self.playerScore = 5
                    elif point[i]+point[j] == 3 or point[i]+point[j]==13:
                        plusStatus = "세끗"
                        self.playerScore = 4
                    elif point[i]+point[j] == 2 or point[i]+point[j]==12:
                        plusStatus = "두끗"
                        self.playerScore = 3
                    elif point[i]+point[j] == 1 or point[i]+point[j]==11:
                        plusStatus = "한끗"
                        self.playerScore = 2
                    elif (point[i]==2 and point[j] == 8) or (point[i]==8 and point[j]==2):
                        plusStatus = "망통"
                        self.playerScore = 1
                    elif (point[i]==3 and point[j] == 7) or (point[i]==7 and point[j]==3):
                        plusStatus = "망통"
                        self.playerScore = 1
        if self.tempNumList[8]==2 and self.tempNumList[1]==1:
            status.configure(text="구구리(9,9,2)"+plusStatus)
        elif self.tempNumList[7]==2 and self.tempNumList[3]==1:
            status.configure(text="팍팍싸(8,8,4)"+plusStatus)
        elif self.tempNumList[6]==2 and self.tempNumList[5]==1:
            status.configure(text="철철육(7,7,6)"+plusStatus)
        elif self.tempNumList[5]==2 and self.tempNumList[7]==1:
            status.configure(text="쭉쭉팔(6,6,8)"+plusStatus)
        elif self.tempNumList[4]==1 and self.tempNumList[6]==1 and self.tempNumList[7]==1:
            status.configure(text="오리발(5,7,8)"+plusStatus)
        elif self.tempNumList[4]==1 and self.tempNumList[5]==1 and self.tempNumList[8]==1:
            status.configure(text="오륙구(5,6,9)"+plusStatus)
        elif self.tempNumList[4]==2 and self.tempNumList[9]==1:
            status.configure(text="꼬꼬장(5,5,10)"+plusStatus)
        elif self.tempNumList[3]==1 and self.tempNumList[6]==1 and self.tempNumList[8]==1:
            status.configure(text="사칠구(4,7,9)"+plusStatus)
        elif self.tempNumList[3]==1 and self.tempNumList[5]==1 and self.tempNumList[10] == 1:
            status.configure(text="사륙장(4,6,10)"+plusStatus)
        elif self.tempNumList[3] == 2 and self.tempNumList[1]==1:
            status.configure(text="샅샅이(4,4,2)"+plusStatus)
        elif self.tempNumList[2]==1 and self.tempNumList[7] == 1 and self.tempNumList[8]==1:
            status.configure(text="삼빡구(3,8,9)"+plusStatus)
        elif self.tempNumList[2] == 1 and self.tempNumList[6]==1 and self.tempNumList[9]==1:
            status.configure(text="삼칠장(3,7,10)"+plusStatus)
        elif self.tempNumList[2]==2 and self.tempNumList[3]==1:
            status.configure(text="심심새(3,3,4)"+plusStatus)
        elif self.tempNumList[1]==1 and self.tempNumList[7]==1 and self.tempNumList[9]==1:
            status.configure(text="이판장(2,8,10)"+plusStatus)
        elif self.tempNumList[1]==1 and self.tempNumList[2]==1 and self.tempNumList[4]==1:
            status.configure(text="이삼오(2,3,5)"+plusStatus)
        elif self.tempNumList[1]==2 and self.tempNumList[5]==1:
            status.configure(text="니니육(2,2,6)"+plusStatus)
        elif self.tempNumList[0]==1 and self.tempNumList[8]==1 and self.tempNumList[9]==1:
            status.configure(text="삥구장(1,9,10)"+plusStatus)
        elif self.tempNumList[0]==1 and self.tempNumList[3]==1 and self.tempNumList[4]==1:
            status.configure(text="빽새오(1,4,5)"+plusStatus)
        elif self.tempNumList[0]==1 and self.tempNumList[2]==1 and self.tempNumList[5]==1:
            status.configure(text="물삼육(1,3,6)"+plusStatus)
        elif (self.tempNumList[0] == 1 and self.tempNumList[1] == 1 and self.tempNumList[6] == 1):
            status.configure(text="삐리칠(1,2,7)"+plusStatus)
        elif (self.tempNumList[0]==2 and self.tempNumList[7]==1):
            status.configure(text="콩콩팔(1,1,8)"+plusStatus)
        else:
            status.configure(text="노메이드")
            self.playerScore = 0


        return self.playerScore

        point.clear()
        self.tempNumList.clear()

    def whoisWinner(self,p1,p2,p3,m):
        if p1>m:
            self.Lplayer1wlStatus.configure(text = "승")
        else:
            self.Lplayer1wlStatus.configure(text="패")
        if p2>m:
            self.Lplayer2wlStatus.configure(text="승")
        else:
            self.Lplayer2wlStatus.configure(text="패")
        if p3>m:
            self.Lplayer3wlStatus.configure(text="승")
        else:
            self.Lplayer3wlStatus.configure(text="패")

    def checkWinner(self):
        self.p1_5["state"] = "disabled"
        self.p1_5["bg"] = "gray"
        self.p1_1["state"] = "disabled"
        self.p1_1["bg"] = "gray"
        self.p2_5["state"] = "disabled"
        self.p2_5["bg"] = "gray"
        self.p2_1["state"] = "disabled"
        self.p2_1["bg"] = "gray"
        self.p3_5["state"] = "disabled"
        self.p3_5["bg"] = "gray"
        self.p3_1["state"] = "disabled"
        self.p3_1["bg"] = "gray"
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

        for i in range(5):
            p = PhotoImage(file="GodoriCards/" + self.main.cards[i].filename())
            self.LcardsMain[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsMain[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

            self.LmPoint[i].place(x=170 + i * 32, y=100)



        self.whoisWinner(self.scoreCheck(self.Lplayer1Status,self.LcardsP1Point),self.scoreCheck(self.Lplayer2Status,self.LcardsP2Point)
                         ,self.scoreCheck(self.Lplayer3Status,self.LcardsP3Point),self.scoreCheck(self.LmainStatus, self.LcardsMPoint))

    def pressedAgain(self):
        empty = PhotoImage(file="GodoriCards/green.gif")
        #       self.LcardsPlayer[1].configure = Label(self.window,image=empty)
        for i in range(len(self.LcardsPlayer1)):
            self.LcardsPlayer1[i].config(image=empty)  # 이미지 레퍼런스 변경
            self.LcardsPlayer1[i].image = empty
            self.LcardsPlayer1[i].place(x=50 + i * 32, y=850)

        for i in range(len(self.LcardsPlayer2)):
            self.LcardsPlayer2[i].config(image=empty)  # 이미지 레퍼런스 변경
            self.LcardsPlayer2[i].image = empty
            self.LcardsPlayer2[i].place(x=260 + i * 32, y=850)

        for i in range(len(self.LcardsPlayer3)):
            self.LcardsPlayer3[i].config(image=empty)  # 이미지 레퍼런스 변경
            self.LcardsPlayer3[i].image = empty
            self.LcardsPlayer3[i].place(x=470 + i * 32, y=850)

        for i in range(len(self.LcardsMain)):
            self.LcardsMain[i].config(image=empty)
            self.LcardsMain[i].image = empty
            self.LcardsMain[i].place(x=170 + i * 32, y=840)

        self.Lplayer1Status.configure(text="")
        self.Lplayer2Status.configure(text="")
        self.Lplayer3Status.configure(text="")
        self.LmainStatus.configure(text="")
        self.Lplayer1wlStatus.configure(text="")
        self.Lplayer2wlStatus.configure(text="")
        self.Lplayer3wlStatus.configure(text="")


        for j in range(5):
            self.Lp1Point[j].configure(text="")
            self.Lp2Point[j].configure(text="")
            self.Lp3Point[j].configure(text="")
            self.LmPoint[j].configure(text="")

        self.LcardsP1Point.clear()
        self.LcardsP2Point.clear()
        self.LcardsP3Point.clear()
        self.LcardsMPoint.clear()
        self.player1Money = 0
        self.player2Money = 0
        self.player3Money = 0
        self.Lplayer1Money.configure(text=str(self.player3Money) + "만")
        self.Lplayer2Money.configure(text=str(self.player3Money) + "만")
        self.Lplayer3Money.configure(text=str(self.player3Money) + "만")
        self.dealnum = 0

        self.p1_5["state"] = 'active'
        self.p1_5["bg"] = 'white'
        self.p1_1["state"] = 'active'
        self.p1_1["bg"] = 'white'
        self.p2_5["state"] = 'active'
        self.p2_5["bg"] = 'white'
        self.p2_1["state"] = 'active'
        self.p2_1["bg"] = 'white'
        self.p3_5["state"] = 'active'
        self.p3_5["bg"] = 'white'
        self.p3_1["state"] = 'active'
        self.p3_1["bg"] = 'white'
        self.Deal["state"] = 'active'
        self.Deal["bg"] = 'white'
        self.Again['state'] = "disabled"
        self.Again['bg'] = 'gray'


Dorizitgo()