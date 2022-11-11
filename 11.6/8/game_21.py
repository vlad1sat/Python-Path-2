import random


class Card:

    def __init__(self, suit: int, rank):
        self.suit = suit
        self.rank = rank


class Deck:

    def __init__(self):
        self.cards = self.create_cards()

    @staticmethod
    def create_cards():
        return [[Card(index_card, 'Черви'),
                 Card(index_card, 'Крести'),
                 Card(index_card, 'Буби'),
                 Card(index_card, 'Пики')] for index_card in range(2, 16)]


class Player:

    def __init__(self, name, deck: Deck):
        self.name = name
        self.player_cards = list()
        self.deck = deck
        self.get_cards()

    def get_cards(self):
        for _ in range(2):
            self.take_card()

    def take_card(self):
        while True:
            index_card = random.randint(0, 13)
            if len(self.deck.cards) <= index_card:
                continue
            if len(self.deck.cards[index_card]) == 0:
                continue
            suit_card = random.randint(0, 3)
            if len(self.deck.cards[index_card]) <= suit_card:
                continue
            self.player_cards.append(self.deck.cards[index_card][suit_card])
            self.deck.cards[index_card].pop(suit_card)
            break

    def get_sum_cards(self):
        sum_cards = 0
        for card in self.player_cards:
            if card.suit < 11:
                sum_cards += card.suit
                continue
            elif 11 <= card.suit <= 14:
                sum_cards += 10
            else:
                if sum_cards < 21:
                    sum_cards += 1
                else:
                    sum_cards += 11
        return sum_cards

    def show_cards(self):
        str_cards = None
        for card in self.player_cards:
            if str_cards is None:
                str_cards = ''.join('({} {})'.format(card.rank, card.suit))
                continue
            str_cards = ', '.join([str_cards, '({}, {})'.format(card.rank, card.suit)])
        return str_cards
