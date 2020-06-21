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
        self.Lplayer1Status.place(x=40, y=280)

        self.Lplayer2Status = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.Lplayer2Status.place(x=250, y=280)

        self.Lplayer3Status = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.Lplayer3Status.place(x=460, y=280)

        self.LmainStatus = Label(text="", width=17, height=1, font=self.fontstyle2, bg="green", fg="yellow")
        self.LmainStatus.place(x=100, y=80)

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

    def p1Card(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer1.append(Label(self.window, bd=0, image=p))
        self.LcardsPlayer1[self.player1.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p
        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + n * 32, y=350)
        self.LcardsP1Point.append(newCard.getValue())
        self.p1Point = [int(x) for x in self.LcardsP1Point]
        self.P1PointLabel = Label(text = self.p1Point[n],width=3, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.P1PointLabel.place(x=60 + n * 32, y=320)

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
        self.p2Point = [int(x) for x in self.LcardsP2Point]
        self.P2PointLabel = Label(text=self.p2Point[n], width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white")
        self.P2PointLabel.place(x=270 + n * 32, y=320)

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
        self.p3Point = [int(x) for x in self.LcardsP3Point]
        self.P3PointLabel = Label(text=self.p3Point[n], width=3, height=1, font=self.fontstyle2, bg="green",
                                  fg="white")
        self.P3PointLabel.place(x=480 + n * 32, y=320)

    def mCard(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.main.addCard(newCard)

        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.LcardsMain.append(Label(self.window, bd=0, image=p))

        self.LcardsMain[self.main.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsMain[self.main.inHand() - 1].image = p
        self.LcardsMain[self.main.inHand() - 1].place(x=170 + n * 32, y=140)

        self.LcardsMPoint.append(newCard.getValue())

    def scoreCheck(self,status,point):
        plusStatus = "하이"

        for i in range(5):
            lastNum = (point[i]*10)%10

        print(lastNum)

        self.tempNumList = [0 for _ in range(12)]

        iPoint = [int(x) for x in point]
        for i in range(1,len(iPoint)+1):
            num = iPoint[i-1]
            self.tempNumList[num-1] = iPoint.count(num)

        for i in range(5):
            for j in range(5):
                if i!=j:
                    if point[i] == 8.1 and point[j] == 3.1:
                        plusStatus = "38광땡"
                    elif (point[i] == 1.1 and point[j] == 3.1) or (point[i] == 1.1 and point[i] == 8.1):
                        plusStatus = "광땡"
                    elif (point[i] == 1.1 or point[i]==1.2 or point[i] == 1.3 or point[i] == 1.4) and (
                            point[j] == 1.1 or point[j]==1.2 or point[j] == 1.3 or point[j] == 1.4):
                        plusStatus = "삥땡"
                    elif (point[i] == 2.1 or point[i] == 2.2 or point[i] == 2.3 or point[i] == 2.4) and (
                            point[j] == 2.1 or point[j] == 2.2 or point[j] == 2.3 or point[j] == 24):
                        plusStatus = "이땡"
                    elif (point[i] == 3.1 or point[i] == 3.2 or point[i] == 3.3 or point[i] == 3.4) and (
                            point[j] == 3.1 or point[j] == 3.2 or point[j] == 3.3 or point[j] == 3.4):
                        plusStatus = "삼땡"
                    elif (point[i] == 4.1 or point[i] == 4.2 or point[i] == 4.3 or point[i] == 4.4) and (
                            point[j] == 4.1 or point[j] == 4.2 or point[j] == 4.3 or point[j] == 4.4):
                        plusStatus = "사땡"
                    elif (point[i] == 5.1 or point[i] == 5.2 or point[i] == 5.3 or point[i] == 5.4) and (
                            point[j] == 5.1 or point[j] == 5.2 or point[j] == 5.3 or point[j] == 5.4):
                        plusStatus = "오땡"
                    elif (point[i] == 6.1 or point[i] == 6.2 or point[i] == 6.3 or point[i] == 6.4) and (
                            point[j] == 6.1 or point[j] == 6.2 or point[j] == 6.3 or point[j] == 6.4):
                        plusStatus = "육땡"
                    elif (point[i] == 7.1 or point[i] == 7.2 or point[i] == 7.3 or point[i] == 7.4) and (
                            point[j] == 7.1 or point[j] == 7.2 or point[j] == 7.3 or point[j] == 7.4):
                        plusStatus = "칠땡"
                    elif (point[i] == 8.1 or point[i] == 8.2 or point[i] == 8.3 or point[i] == 8.4) and (
                            point[j] == 8.1 or point[j] ==8.2 or point[j] == 8.3 or point[j] == 8.4):
                        plusStatus = "팔땡"
                    elif (point[i] == 9.1 or point[i] == 9.2 or point[i] == 9.3 or point[i] == 9.4) and (
                            point[j] == 9.1 or point[j] == 9.2 or point[j] == 9.3 or point[j] == 9.4):
                        plusStatus = "구땡"
                    elif (point[i] == 10.1 or point[i] == 10.2 or point[i] == 10.3 or point[i] == 10.4) and (
                            point[j] == 10.1 or point[j] == 10.2 or point[j] == 10.3 or point[j] == 10.4):
                        plusStatus = "장땡"

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




        iPoint.clear()
        self.tempNumList.clear()

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

        for i in range(len(self.LcardsMain)):
            p = PhotoImage(file="GodoriCards/" + self.main.cards[i].filename())
            self.LcardsMain[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsMain[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.mPoint = [int(x) for x in self.LcardsMPoint]
            self.MPointLabel = Label(text=self.mPoint[i], width=3, height=1, font=self.fontstyle2, bg="green",
                                      fg="white")
            self.MPointLabel.place(x=180 + i * 32, y=110)


        self.scoreCheck(self.Lplayer1Status,self.LcardsP1Point)

        self.scoreCheck(self.Lplayer2Status,self.LcardsP2Point)

        self.scoreCheck(self.Lplayer3Status, self.LcardsP3Point)

        self.scoreCheck(self.LmainStatus, self.LcardsMPoint)


    def pressedAgain(self):
       pass



Dorizitgo()