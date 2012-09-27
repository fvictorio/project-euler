class Card:
    def __init__(self, value, suit, repeated = 1):
        self.sv = value
        if value >= '1' and value <= '9':
            self.value = int(value)
        elif value == 'T':
            self.value = 10
        elif value == 'J':
            self.value = 11
        elif value == 'Q':
            self.value = 12
        elif value == 'K':
            self.value = 13
        elif value == 'A':
            self.value = 14
        self.suit = suit
        self.repeated = repeated
    def __lt__(self, c):
        if self.repeated < c.repeated:
            return True
        if self.repeated > c.repeated:
            return False
        return self.value < c.value
    def __repr__(self):
        return self.sv + self.suit

class Hand:
    def __init__(self, s):
        values = [s[i] for i in range(0, 10, 2)]
        suits = [s[i] for i in range(1, 10, 2)]
        self.cards = []
        for (v, s) in zip(values, suits):
            c = Card(v, s, sum(v == vv for vv in values))
            self.cards.append(c)
        self.cards.sort()
        self.cards.reverse()


    def power(self):
        if self.cards[0].value == 13 and self.is_flush() and self.is_straight():
            return 10
        if self.is_flush() and self.is_straight():
            return 9
        if self.cards[0].repeated == 4:
            return 8
        if self.cards[0].repeated == 3 and self.cards[3].repeated == 2:
            return 7
        if self.is_flush():
            return 6
        if self.is_straight():
            return 5
        if self.cards[0].repeated == 3:
            return 4
        if self.cards[0].repeated == 2 and self.cards[2].repeated == 2:
            return 3
        if self.cards[0].repeated == 2:
            return 2
        return 1

    def __lt__(self, h):
        if self.power() < h.power():
            return True
        if self.power() > h.power():
            return False
        for (i, j) in zip(self.cards, h.cards):
            if i.value < j.value:
                return True
            if i.value > j.value:
                return False
        return False

    def __repr__(self):
        return '-'.join(str(i) for i in self.cards)

    def is_flush(self):
        return all(self.cards[i].suit == self.cards[i+1].suit for i in range(len(self.cards)-1))

    def is_straight(self):
        return all(self.cards[i].value - 1 == self.cards[i+1].value for i in range(len(self.cards)-1)) or [14, 5, 4, 3, 2] == [i.value for i in self.cards]
