from collections import deque
import random



class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __repr__(self):
        return '<{} {}>'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = deque()
        self.build()

    def build(self):
        self.cards.clear()
        for i in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for j in range(1, 14):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def length(self):
        return len(self.cards)

    def get_card(self):
        return self.cards.popleft()

    def __repr__(self):
        return 'Deck: [{} Cards]'.format(self.length())


class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self):
        for player in self.players:
            for i in range(3):
                player.give_card(self.draw_card())

    def draw_card(self):
        return self.deck.get_card()

    def restart_game(self):
        self.deck.build()
        for player in self.players:
            player.return_cards()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def give_card(self, card):
        self.cards.append(card)

    def return_cards(self):
        return self.cards

    def discard_cards(self):
        self.cards = []

    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))


    #def compare_hands(list1, list2):
    # compare the contents of two lists
    # at the end, return which hand won

    

def compare_two_lists(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    v11 = list1[0].value
    v12 = list1[1].value
    v13 = list1[2].value
    v21 = list2[0].value
    v22 = list2[1].value
    v23 = list2[2].value
   
    hv1 = sum(v11, v12, v13)
    hv2 = sum(v21, v22, v23)

    

def check_pair(hand):
    v0 = hand[0].value
    v1 = hand[1].value
    v2 = hand[2].value
    if v0 == v1 or v0 == v2:
        has_pair = True
        pair_val = v0
    elif v1 == v2:
        has_pair = True
        pair_val = v1
    else:
        has_pair = False
        pair_val = 0
    return [has_pair, pair_val]

def check_triplet(hand):
    v0 = hand[0].value
    v1 = hand[1].value
    v2 = hand[2].value
    if v0 == v1 and v1 == v2:
        has_triplet = True
        pair_val = v0
    else:
        has_triplet = False
        pair_val = 0
    return [has_triplet, pair_val]


def check_high_card(hand):
    v0 = hand[0].value
    v1 = hand[1].value
    v2 = hand[2].value
    # return max(v0, v1)  # returns high card
    return v0 + v1 + v2       # returns sum of card values


name1 = 'Tom' 
name2 = 'Harry'

'''
name1 = input('Enter the name of player one: ')
name2 = input('Enter the name of player two: ')
'''

deck_of_cards = Deck()
player_one = Player(name1)
player_two = Player(name2)

'''
test_card11 = Card("Hearts", 8)
test_card12 = Card("Clubs", 9)
test_card13 = Card("Diamonds", 8)
player_one.give_card(test_card11)
player_one.give_card(test_card12)
player_one.give_card(test_card13)
test_card21 = Card("Hearts", 11)
test_card22 = Card("Clubs", 11)
test_card23 = Card("Diamonds", 8)
player_two.give_card(test_card21)
player_two.give_card(test_card22)
player_two.give_card(test_card23)
'''

new_game = Game([player_one, player_two], deck_of_cards)
new_game.deal()
print(player_one, player_two)
hand_one = player_one.return_cards()
hand_two = player_two.return_cards()


hand_one_score = check_pair(hand_one)
hand_two_score = check_pair(hand_two)
hand_one_score_two = check_triplet(hand_one)
hand_two_score_two = check_triplet(hand_two)
hand_one_high = check_high_card(hand_one)
hand_two_high = check_high_card(hand_two)
'''
if hand_one_score_two[0] == True and hand_two_score_two[0] == False:
    print (hand_one_score_two + ' has three ' + pair_val + ' s')
'''
if hand_one_score_two[0] == True and hand_two_score_two[0] == True:
    if hand_one_score_two[1] > hand_two_score_two[1]:
        print (name1 + ' has three ' + str(hand_one_score_two[1]) + 's and wins!')
    elif hand_two_score_two[1] > hand_one_score_two[1]:
        print (name2 + ' has three ' + str(hand_two_score_two[1]) + 's and wins!')
    else:
        print (' Wow this is amazing, both players have three of a kind, its a tie!!!')
elif hand_one_score_two[0] == True:
     print (name1 + ' has three ' + str(hand_one_score_two[1]) + 's and wins!')

elif hand_two_score_two[0] == True:
    print (name2 + ' has three ' + str(hand_two_score_two[1]) + 's and wins')

else:
    if hand_one_score[0] == True and hand_two_score[0] == True:
        if hand_one_score[1] > hand_two_score[1]:
            print(name1 + ' has a pair of ' + str(hand_one_score[1]) + 's and wins!')
        elif hand_one_score[1] < hand_two_score[1]:
            print(name2 + ' has a pair of ' + str(hand_two_score[1]) + 's and wins!')
        else:
            print(name1 + ' and ' + name2 + ' both have pairs of ' + str(hand_one_score[0]) + ': it is a draw!')
        print ()
    else:
        if hand_one_score[0] == True:
            print(name1 + ' has a pair of ' + str(hand_one_score[1]) + 's and wins!')
        elif hand_two_score[0] == True:
            print(name2 + ' has a pair of ' + str(hand_two_score[1]) + 's and wins!')
        else:
            if hand_one_high > hand_two_high:
                print(name1 + ' has a higher total of ' + str(hand_one_high) + ' and wins!')
            elif hand_one_high < hand_two_high:
                print(name2 + ' has a higher total of ' + str(hand_two_high) + ' and wins!')
            else:
                print(name1 + ' and ' + name2 + ' have the same total of ' + str(hand_one_high) + ': it is a draw!')

'''
#name1 = input('Enter the name of player one: ')
#name2 = input('Enter the name of player two: ')
deck_of_cards = Deck()
player_one = Player(name1)
player_two = Player(name2)
new_game = Game([player_one, player_two], deck_of_cards)
new_game.deal()
print(player_one, player_two)
hand_one = player_one.return_cards()
hand_two = player_two.return_cards()
#print(hand_one)
#print(hand_two)
#print(compare_two_lists(hand_one, hand_two))
(total_score(hand_one, hand_two))

# winner = compare_hands(hand_one, hand_two)

#print(new_game.deck)
#new_game.restart_game()
#print(player_one, player_two)
#print(new_game.deck)
'''