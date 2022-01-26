from colorama import init
from colorama import Fore, Back, Style
import inspect

class Card:
    def __init__(self, city, color):
        self.city = city
        self.color = []
        match color:
            case 'r': self.color = Fore.RED
            case 'y': self.color = Fore.YELLOW
            case 'b': self.color = Fore.BLUE
            case 'k': self.color = Fore.BLACK+Back.WHITE

    def __str__(self):
        return f'{self.color}{self.city}'

class Deck:
    santiago = Card('Santiago', 'y')
    lima = Card('Lima', 'y')
    essen = Card('Essen', 'b')
    atlanta = Card('Atlanta', 'b')
    seoul = Card('Seoul', 'r')
    osaka = Card('Osaka', 'r')
    algiers = Card('Algiers', 'k')
    moscow = Card('Moscow', 'k')

class Sets:
    all = [x[1] for x in inspect.getmembers(Deck, lambda a:type(a)==type(Deck.seoul))]
    yellow = [x[1] for x in inspect.getmembers(Deck, lambda a:(type(a)==type(Deck.seoul) and a.color == Deck.santiago.color))]
    blue = [x[1] for x in inspect.getmembers(Deck, lambda a:(type(a)==type(Deck.seoul) and a.color == Deck.essen.color))]
    red = [x[1] for x in inspect.getmembers(Deck, lambda a:(type(a)==type(Deck.seoul) and a.color == Deck.seoul.color))]
    black = [x[1] for x in inspect.getmembers(Deck, lambda a:(type(a)==type(Deck.seoul) and a.color == Deck.algiers.color))]

if __name__ == '__main__':
    init(autoreset=True)

    # test code
    c1 = Card('Santiago', 'y')
    c2 = Card('Essen', 'b')
    c3 = Card('Seoul', 'r')
    c4 = Card('Algiers', 'k')
    test_deck = [c1, c2, c3, c4]
    for card in test_deck: print(card, end=' ')
    print()

    draw_pile = Sets.all

    for card in draw_pile: print(card, end=' ')
    print()
    for card in Sets.yellow: print(card, end=' ')

    print('done')




