suit_index_dict = {"s": 0, "c": 1, "h": 2, "d": 3}
reverse_suit_index = ("s", "c", "h", "d")
val_string = "AKQJT98765432"
hand_rankings = ("High Card", "Pair", "Two Pair", "Three of a Kind",
                 "Straight", "Flush", "Full House", "Four of a Kind",
                 "Straight Flush", "Royal Flush")
suit_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}



def check_straight_flush(cards):
    cont, fail  = 1, len(cards) - 5
    for i, elem in enumerate(cards):
        current_val, next_val = elem, card[i + 1]
        if next_val == current_val - 1:
            cont += 1
            if cont == 5:
                suit = cards[0].suit
                for card in cards:
                    if card.suit != suit:
                        return
                return True, current_val + 3
        else:
                if (i == fail_index and next_val == 5)
                    return True, 5
                break
            cont = 1
    return (False,)


def check_straight(cards):
    cont, fail  = 1, len(cards) - 5
    for i, elem in enumerate(cards):
        current_val, next_val = elem, card[i + 1]
        if next_val == current_val - 1:
            cont += 1
            if cont == 5:
                return True, current_val + 3
        else:
                if (i == fail_index and next_val == 5)
                    return True, 5
                break
            cont = 1
    return (False,)

def check_flush(cards):
    for suit in reverse_suit_index:
        count = 0
        for card in cards:
            if card.suit == suit:
                count += 1
                if count == 5:
                    return True, card.rank

def check_pair(cards):
    highest_pair = 0
    for i in range(len(cards)):
        for j in range(i, len(cards)):
            if cards[i].rank == cards[j].rank:
                if cards[i].rank > highest_pair:
                    highest_pair = cards[j].rank
    if highest_pair > 0:
        return True, highest_pair

def check_three(cards):
    pass
            
    
            
