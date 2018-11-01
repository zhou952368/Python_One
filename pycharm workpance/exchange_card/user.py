class Hand:
    def __init__(self):
        self.left_hand = None
        self.right_hand = None

    def hold(self, swich_hand, something):
        if swich_hand == "left":
            self.left_hand = something
        elif swich_hand == "right":
            self.right_hand = something


class User:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def exchange(self):
        self.hand.left_hand, self.hand.right_hand = self.hand.right_hand, self.hand.left_hand

    def display(self):
        print("{0}左手里拿的是{1}，右手拿的是{2}".format(self.name, self.hand.left_hand, self.hand.right_hand))
