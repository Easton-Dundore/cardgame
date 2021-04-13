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
        self.cards = []

    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))


deck_of_cards = Deck()
player_one = Player("John")
player_two = Player("Harrry")
new_game = Game([player_one, player_two], deck_of_cards)
new_game.deal()
print(player_one, player_two)
print(new_game.deck)
new_game.restart_game()
print(player_one, player_two)
print(new_game.deck)
