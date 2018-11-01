from user import *
from card import Card


def main():
    card1 = Card("红桃", "A")
    card2 = Card("黑桃", "K")
    zhou = User("zhou")
    zhou.hand.hold("left", card1)
    zhou.hand.hold("right", card2)
    zhou.display()
    zhou.exchange()
    zhou.display()
if __name__ == '__main__':
    main()
