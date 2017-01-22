
import itertools

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if type(other) == Card:
            if self.rank == other.rank:
                return True
        return False

    def getHashables(self):
        return (self.rank, self.suit)

    def __hash__(self):
        return hash(getHashables(self))



class Player(object):
    def __init__(value = 1000):
        self.hand = []
        self.value = value

    def getAction(self):
        return action

class AI(object):
    def __init__(value = 1000):
        self.hand = []
        self.value = value

    def getAction(self):
        
 

class Poker(object):
    def __init__(players):
        self.players = []
        self.table = []
        self.simTable = []
        for player in range(players):
            self.players.append(Player())
        self.deck = Deck()
        self.pot = 0
        self.bets = [0 for i in range(players)]
        self.bettingRound = False
        self.round = 0
        self.simulate = []
        

    def dealCardstoHand(self):
        for player in self.players:
            player.hand.append(self.deck.draw(2))
            self.bettingRound = True
            self.round += 1

    def dealCardstoTable(self, number):
        self.table.append(self.deck.draw(number))
        self.round += 1
        
    def bettingRound(self):
        for i in range(self.players % len(self.players)):
            player = self.player[i]
            player.action = True
            action = player.getAction
            if action == "call":
                self.bets[player] = self.bets[player - 1]
                self.pot += callAmount
            elif action == "fold":
                self.bets[player] = -1
            elif action == "raise":
                self.bets[player] = raw_input("Bet Amount = ")
                self.pot += betAmount
            player.action = False
            bets = [bet for bet in self.bets if bet != -1]
            if len(bets) == 1:
                player.hand += self.pot
                self.pot = 0
                self.bets = [0 for player in range(players)]
                self.deck = Deck()
                self.table = []
                self.bettingRound = False
            if bets == [bets[0] for i in range(len(bets))]:
                self.bettingRound = False
                return True
            else:
                continue
    def handScore(self):
        def conversionToBinary(card):

        """ http://suffe.cool/poker/evaluator.html
        I will utilize a variation of Cactus Kev's algorithm in which,
            each card is represented as 4 bytes.
            +--------+--------+--------+--------+
            |000bbbbb|bbbbbbbb|aaaarrrr|xxpppppp|
            +--------+--------+--------+--------+

            p = prime number of rank (deuce=2,trey=3,four=5,...,ace=41)
            r = rank of card (deuce=0,trey=1,four=2,five=3,...,ace=12)
            a = suit of card (bit turned on based on suit of card)
            b = bit turned on depending on rank of card
            we are not using the bits marked 0
            Also, we shift the numerical values of each of these variables
            to fit the build above.

            Rank	Deuce	Trey	Four	Five	Six	Seven	Eight	Nine	Ten	Jack	Queen	King	Ace
            Prime	2	3	5	7	11	13	17	19	23	29	31	37	41
        """
            b = 1 << (card.rank + 14) # shift depends on rank and the total ranks
            a = 1 << (card.suit + 11) # shift deends on suit and total number
            r = (card.rank - 2) << 8 # there are 8 possible ranks as mentioned above
            p = lookup.primes[card.rank - 2]
            return b|r|p|a

        # after changing each card to binary, we evaluate the rank of the entire hand
        def handRank(hand):
            binary = lookup.binary[card.rank][card.suit]
            binaryHand = [binary(card) for card in hand]

            # first we check for flush, because only for this, the suit matters
            isflush = binaryHand[0]
            for element in binaryHand[1:]:
                isflush = isflush & element # we and each element
            ranking = binaryHand[0]
            for element in binaryHand[1:]:
                ranking = ranking | element # we or each element 
            ranking = ranking >> 16
            if isflush != 0: # we have a flush
                rankFlush = lookup.flushes[ranking]
            else: # not a flush
                # we check whether we have a straight or a high Card
                # because in this case we will have all unique cards
                trial = lookup.unique[ranking]
                if trial > 0:
                    return trial
                else:
                    # now we compute the product of primes
                ranking = binaryHand[0] & 0xFF
                for card in binaryHand[1:]:
                    ranking *= card & 0xFF
                return lookup.pairs[ranking]
        def evaluate7Cards(self):
            highestRank = 10000 # there is nothing higher
            highestPlayer = None
            for player in self.players:
                allCards = player.hand + self.table
                subsets = list(itertools.combinations(allCards, 5))
                for subset in subsets:
                    rank = handRank(subset)
                    if highestRank == None or rank < highestRank:
                        highestRank = rank
                        highestPlayer = player
                    elif highestRank == rank:
                        highestPlayer = list(highestPlayer).append(player)
            value = highestRank
            if value > 6185: print "High Card"
            if (value > 3325): # pair       
            if (value > 2467) # two pair      
            if (value > 1609) # three of a kind  
            if (value > 1599) # straight         
            if (value > 322)  # flush          
            if (value > 166)  # full house      
            if (value > 10)   # four of a kind
            # if not, straight flush
            return highestPlayer

    def simulation(self, player, n=100000):
        wins = 0
        players = copy.deepcopy(self.players)
        players.remove(player)
        deck = copy.deepcoy(self.deck)
        deck.remove(player.hand[0])
        deck.remove(player.hand[1])
        for i in range(n):
            random.shuffle(deck)
            for otherPlayer in players:
                for card in range(2):
                    otherPlayer.simulate += deck.pop()
            for i in range(5):
                self.simTable.append(deck.pop())
            winner = 
            if winner == player:
                wins += 1
        return wins/n * 100


    
                    
                    
                        
                    
                    
                    

                
                
                
            
            