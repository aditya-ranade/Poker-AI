from Tkinter import *
class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank in ["jack", "king", "queen"]:
            suit = suit + "2"
        self.filename = str(rank) + "_of_" + str(suit) + ".png"

class Deck(object):
    numberNames = [None, "Ace", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jack", "Queen", "King"]
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.deck = []
        for number in range(1, 14):
            for suit in range(4):
                self.deck.append(Card(number, suit))


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 1000.00
        self.bet = 0 

    def add(self, card):
        self.hand += [card]

    def __repr__(self):
        for card in self.hand:
            return str(card.suit) + str(card.rank)
    def bet(self, bet):
        self.money -= bet
        self.bet = bet

class PokerGame(object):
    deck = Deck()
    player1 = Player("Aditya")
    def __init__(self):
        
        self.newRound = False
        self.table = []
        self.click = 0
        self.pot = 0

    def __repr__(self):
        value = ""
        for card in self.table:
            value += str(card.suit) + str(card.rank)
        return value

    def deal(self):
        if self.click == 0:
            for i in range(2):
                PokerGame.player1.hand.append(PokerGame.deck.deck[-1])
                PokerGame.deck.deck.pop()
            self.click += 1
            print PokerGame.player1
        elif self.click == 1:
            self.click += 1
            PokerGame.deck.deck.pop()
            for i in range(3):
                self.table.append(PokerGame.deck.deck[-1])
                PokerGame.deck.deck.pop()
        elif self.click == 2:
            self.click += 1
            PokerGame.deck.pop()
            for i in range(1):
                self.table.append(PokerGame.deck.deck[-1])
                PokerGame.deck.deck.pop()
        elif self.click == 3:
            self.click += 1
            PokerGame.deck.pop()
            for i in range(1):
                self.table.append(PokerGame.deck.deck[-1])
                PokerGame.deck.deck.pop()
        print self

    def pot_add(self, bet):
        for player in players:
            self.pot += player.bet

    def checkIfBetsAreEqual(self):
        for player in players:
            if player.move == False:
                return
        pot_add(self, bet)


    def redrawAll(self, canvas):
        pass

    def timerFired(self, canvas):
        pass
        
    def mousePressed(self, event):
        self.deal()

    def keyPressed(self, event):
        pass

    def run(self, width = 400, height = 400):
        def redrawAllWrapper(canvas):
            canvas.delete(ALL)
            self.redrawAll(canvas)
            canvas.update()
                
        def timerFiredWrapper(canvas):
                self.timerFired(canvas)
                redrawAllWrapper(canvas)
                canvas.after(data.timerDelay, timerFiredWrapper, canvas)

        def mousePressedWrapper(event, canvas):
                self.mousePressed(event)
                redrawAllWrapper(canvas)

        def keyPressedWrapper(event, canvas):
                self.keyPressed(event)
                redrawAllWrapper(canvas)
            
        # Set up data and call init
        class Struct(object): pass
        data = Struct()
        data.width = width
        data.height = height
        data.timerDelay = 100 # milliseconds
        # create the root and the canvas
        root = Tk()
        canvas = Canvas(root, width=data.width, height=data.height)
        canvas.pack()
        # set up events
        root.bind("<Button-1>", lambda event:
                                mousePressedWrapper(event, canvas))
        root.bind("<Key>", lambda event:
                                keyPressedWrapper(event, canvas))
        timerFiredWrapper(canvas)
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")

game = PokerGame()
game.run()
