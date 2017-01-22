from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from functools import partial
from datetime import datetime

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.clock import _hash
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import *
from kivy.properties import BooleanProperty, StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import kivy.graphics.vertex_instructions


Window.size = (1200, 700)



# Declare both screens
class TitlePage(Widget):
    def __init__(self, *args):
        super(TitlePage, self).__init__(*args)
        self.playai = Button(text = "Play with AI", size = (300, 80),
                        pos=(Window.width/2 + 75, Window.height/2-10), font_size = 32)
        self.playfriends = Button(text = "Play with Friends", size = (300, 80),
                             pos = (Window.width/2 + 450, Window.height/2-10), font_size = 32)
        self.playai.bind(on_press= self.transition)
        self.add_widget(self.playai)
        self.add_widget(self.playfriends)

    

    def transition(self, *args):
        """https://github.com/Zogg/FishLife"""
        self.fader = ScreenFader(size = Window.size)
        Window.add_widget(self.fader)
        anim = Animation(alpha = 1.0, d= 0.6)
        anim.bind(on_complete=self.login)
        anim.start(self.fader)

   
    def login(self, *args):
        self.remove_widget(self.playai)
        self.remove_widget(self.playfriends)
        self.root = LoginPage()
        Window.add_widget(self.root)
        Window.remove_widget(self.fader)
        Window.add_widget(self.fader)
        anim = Animation(alpha = 0.0, d=0.8)
        anim.bind(on_complete=lambda instance, value: Window.remove_widget(self.fader))
        anim.start(self.fader)

class LoginPage(Widget):
    def __init__(self, *args):
        super(LoginPage, self).__init__(*args)
        self.txt = TextInput(hint_text = "username", multiline = False, pos = (Window.width/2 - 100, Window.height/2 - 30))
        self.txt.background_color = [0, 0, 0, 0.4]
        self.txt.hint_text = "username"
        self.txt.hint_text_color = [1,1, 1, 1]
        self.txt.size = (200, 40)
        self.txt.font_size = 18
        self.add_widget(self.txt)
        self.go = Button(text = "Start Game",size = (200, 40),
                        pos=(Window.width/2-100, Window.height/2 - 100), font_size = 24)
        self.add_widget(self.go)
        self.go.bind(on_press=self.transition)

    def transition(self, *args):
        self.fader = ScreenFader(size = Window.size)
        Window.add_widget(self.fader)
        anim = Animation(alpha = 1.0, d= 0.6)
        anim.bind(on_complete=self.play)
        anim.start(self.fader)

    def play(self, *args):
        self.remove_widget(self.txt)
        self.remove_widget(self.go)
        self.root = PlayGame()
        Window.add_widget(self.root)
        Window.remove_widget(self.fader)
        Window.add_widget(self.fader)
        anim = Animation(alpha = 0.0, d=0.8)
        anim.bind(on_complete=lambda instance, value: Window.remove_widget(self.fader))
        anim.start(self.fader)

class Card(object):

    numberNames = [None, "ace", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "jack", "queen", "king"]
    suitNames = ["clubs", "diamonds", "hearts", "spades"]

    @staticmethod
    def Deck():
        deck = []
        for suit in range(4):
            for rank in range(1, 14):
                deck.append(Card(rank, suit))
        random.shuffle(deck)
        return deck
                

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.source = Card.numberNames[self.rank] + "_of_" + Card.suitNames[self.suit] + ".png"

    def __eq__(self, other):
        if type(other) == Card:
            if self.rank == other.rank:
                return True
        return False

    def __repr__(self):
        return Card.numberNames[self.rank] + " of " + Card.suitNames[self.suit] 
        
    
    def getHashables(self):
        return (self.rank, self.suit)

    def __hash__(self):
        return hash(getHashables(self))

class Player(object):
    def __init__(self, name, value = 1000):
        self.name = name
        self.hand = []
        self.value = value
        self.pos = Window.width/2, 20
        

    def getAction(self):
        return action

class AI(object):
    def __init__(self, value = 1000):
        self.hand = []
        self.value = value
        self.pos = Window.width/2 - 600, Window.height - 200


class PlayGame(Widget):
    def __init__(self, *args):
        super(PlayGame, self).__init__(*args)
        self.playerName = "Aditya"
        self.player = Player(self.playerName)
        self.AI = AI()
        self.makePlayers()
        self.addChips()
        self.dealHand()

    def makePlayers(self, *args):
        with self.canvas:
            Color(0, 0, 0, 0.4)
            Rectangle(pos = (self.AI.pos[0] + 150, self.AI.pos[1]-150), size = (300, 300))
            Ellipse(pos = self.AI.pos ,size = (200, 200))

            


            #Rectangle(pos = , size = (300, 100))
        

    def addChips(self):
        """chips = Image(source = "oie_transparent.png", pos = (Window.width/2 - 170, Window.height/2 - 230), size = (450/3, 326/3))
        self.add_widget(chips)
        chips = Image(source = "oie_transparent.png", pos = (Window.width/2 - 170, Window.height/2 + 170))
        self.add_widget(chips)"""
        

    def dealHand(self):
        self.deal = Button(text= "Deal", size = (250, 60),
                        pos=(Window.width/2-700, Window.height/2), font_size = 42)
        self.add_widget(self.deal)
        self.deal.bind(on_press=self.animateCards)
        
        self.pot = 0
        self.deck = Card.Deck()
        print self.deck
        self.table = []
        """for i in range(2):
            self.player.hand.append(self.deck.pop())
        for i in range(2):
            self.AI.hand.append(self.deck.pop())"""

    def animateCards(self, *args):
        self.remove_widget(self.deal)
        for i in range(2):
            print i 
            self.player.hand.append(self.deck.pop())
            img = Image(source = self.player.hand[i].source, size = (100, 72.6*2), x = Window.width/2 - 400, y = Window.height/2)
            img.y -= 20
            img.x -= 20
            self.add_widget(img)
            anim = Animation(y = (Window.height/2 - 360), x = Window.width/2 + (i*72.6*1.5) - 30, duration = 0.2)
            anim.start(img)
            """for i in range(len(self.player.hand)):
                print self.player.hand[i]
                if i == 0:
                    img = Image(source = self.player.hand[i].source, size = (50, 100), x = Window.width/2 - 50, y = Window.height + 20)
                    img.y -= 100
                    self.add_widget(img)
            for i in range(len(self.
                if i == 1:
                    img = Image(source = self.player.hand[i].source, size = (50, 100), x = Window.width/2, y = Window.height + 20)
                    img.y -= 100
                    self.add_widget(img)"""
            self.AI.hand.append(self.deck.pop())
            img = Image(source = self.AI.hand[i].source, size = (100, 72.6*2), x = Window.width/2 - 400, y = Window.height/2)
            img.y += 30
            img.x += 20
            self.add_widget(img)
            anim = Animation(y = (Window.height/2 + 270), x = Window.width/2 + (i*72.6*1.5) - 30, duration = 0.2)
            anim.start(img)
        anim.bind(on_complete = self.flop)
    def flop(self, *args):
        print "hi"
        for card in range(3):
            self.table.append(self.deck.pop())
        for i in range(len(self.table)):
            img = Image(source = self.table[i].source, size = (100, 72.6*2), pos = (Window.width/2 - 300, Window.height/2))
            img.x += 20
            self.add_widget(img)
            anim = Animation(x = Window.width/2 - (125 - (125*i)), duration = 0.8)
            anim.start(img)
        print self.deck
        self.turn()

    def turn(self,*args):
        self.table.append(self.deck.pop())
        img = Image(source = self.table[-1].source, size = (100, 72.6*2), pos = (Window.width/2 - 300, Window.height/2))
        img.x += 20
        self.add_widget(img)
        anim = Animation(x = Window.width/2 + (250), duration = 0.8)
        anim.start(img)
        print self.deck
        self.river()

    def river(self, *args):
        print len(self.deck)
        x = self.deck.pop()
        self.table.append(x)
        
        img = Image(source = self.table[-1].source, size = (100, 72.6*2), pos = (Window.width/2 - 300, Window.height/2))
        img.x += 20
        self.add_widget(img)
        anim = Animation(x = Window.width/2 + (375), duration = 0.8)
        anim.start(img)

    def betting(self):
        pass

                
class ScreenFader(Widget):
    # taken from fishLife, github

    alpha = NumericProperty(0.0)
    
    def __init__(self, alpha=0, **kwargs):
        super(ScreenFader, self).__init__(**kwargs)
        self.bind(alpha=self.on_alpha)
        self.alpha = alpha
            
    def on_alpha(self, instance, value):
        self.canvas.clear()
        with self.canvas:
            Color(0,0,0, value)
            Rectangle(pos=self.pos, size=self.size)
            
            


class GraphicsApp(App):
    def build(self):
        self.intro = TitlePage()
        return self.intro

if __name__ == '__main__':
    GraphicsApp().run()
