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
            for i in range(2):
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


def total_score(list1, list2):
    v11 = list1[0].value
    v12 = list1[1].value
    v21 = list2[0].value
    v22 = list2[1].value
    three = v11 + v12
    four = v21 + v22
    if v11 == v12 and v21 == v22:
        if three > four:
            print ('Player one has a total score of ' + (str(three)) + ',' + 'and player two has ' + (str(four)) + ' player one wins!!!')
        elif four > three:
            print ('Player two has a total score of ' + (str(four)) + ',' + 'and player one has ' + (str(three)) + ' player two wins!!!')
    
    elif v11 == v12:
        print (' Player one has equal cards, they win!')
    elif v21 == v22:
        print (' Player two has equal cards, they win!')

    else:
        if three > four:
            print ('Player one has a total score of ' + (str(three)) + ',' + 'and player two has ' + (str(four)) + ' player one wins!!!')
        elif four > three:
            print ('Player two has a total score of ' + (str(four)) + ',' + 'and player one has ' + (str(three)) + ' player two wins!!!')
        else:
            print ('Both players have the same total number, it is a tie!!!')

    

    #def compare_hands(list1, list2):
    # compare the contents of two lists
    # at the end, return which hand won

def compare_two_lists(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    v11 = list1[0].value
    v12 = list1[1].value
    v21 = list2[0].value
    v22 = list2[0].value
    
    hv1 = max(v11, v12)
    hv2 = max(v21, v22)
    print('highest card in list 1 has value ' + str(hv1))
    print(' The highest card in list 2 has value ' + str(hv2))
    retlist = []
    if n1 > n2:
        print('list 1 has more elements (' + str(n1) + ') than list 2 (' + str(n2) + ')')
        retlist = list1
    elif n2 > n1:
        print('list 2 has more elements (' + str(n2) + ') than list 1 (' + str(n1) + ')')
        retlist = list2
    else:
        print('list 1 has the same number of elements (' + str(n1) + ') as list 2')
        retlist = list1
    return retlist


deck_of_cards = Deck()
player_one = Player("John")
player_two = Player("Harrry")
new_game = Game([player_one, player_two], deck_of_cards)
new_game.deal()
print(player_one, player_two)
hand_one = player_one.return_cards()
hand_two = player_two.return_cards()
#print(hand_one)
#print(hand_two)
print(compare_two_lists(hand_one, hand_two))
print(total_score(hand_one, hand_two))

# winner = compare_hands(hand_one, hand_two)

#print(new_game.deck)
#new_game.restart_game()
#print(player_one, player_two)
#print(new_game.deck)