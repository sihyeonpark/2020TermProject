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
        self.LcardsPlayer1 = [] #라벨카드플레이어
        self.LcardsPlayer2 = []  # 라벨카드플레이어
        self.LcardsPlayer3 = []  # 라벨카드플레이어
        self.LcardsP1Point =[]
        self.LcardsP2Point = []
        self.LcardsP3Point = []
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
            self.cardDeck = [i for i in range(48)]
            random.shuffle(self.cardDeck)
            self.deckN = 0

            self.p1Card(0)
            self.p2Card(0)
            self.p3Card(0)

        else:
            for i in range(1,4):
                self.p1Card(i)
                self.p2Card(i)
                self.p3Card(i)

        self.dealnum += 1

    def p1Card(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer1.append(Label(self.window, bd=0, image=p))
        self.LcardsPlayer1[self.player1.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p
        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + n * 35, y=350)

    def p2Card(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer2.append(Label(self.window, bd=0, image=p))

        self.LcardsPlayer2[self.player2.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p
        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=260 + n * 35, y=350)

    def p3Card(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)

        p = PhotoImage(file="GodoriCards/" + newCard.filename())
        self.LcardsPlayer3.append(Label(self.window, bd=0, image=p))

        self.LcardsPlayer3[self.player3.inHand() - 1].config(image=p)  # 가지고있는 카드갯수 -1 인덱스는 0이 시작
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p
        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=470 + n * 35, y=350)

    def pressedAgain(self):
       pass



Dorizitgo()