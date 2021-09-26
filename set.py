#!/usr/bin/env python3

import sys

class Card:
    """ quick card description
    number: 1 2 3
    form: s o(val) l(osange)
    color: r(ouge) v(ert) m(mauve)
    filling: t(ransparent) h(achure) p(lein)
    """

    color = ""
    form = ""
    number = ""
    filling = ""

    def __init__(self, short):
        if len(short) == 4:
            if short[0] in "123":
                self.number = short[0]
            else:
                raise Exception("invalid number " + short[0])
            if short[1] in "sol":
                self.form = short[1]
            else:
                raise Exception("invalid form " + short[1])
            if short[2] in "rvm":
                self.color = short[2]
            else:
                raise Exception("invalid color " + short[2])
            if short[3] in "thp":
                self.filling = short[3]
            else:
                raise Exception("invalid filling " + short[3])
        else:
            raise Exception("not a valid card representation " + short)

    def __str__(self):
        return self.number + self.form + self.color + self.filling

    def __repr__(self):
        return self.number + self.form + self.color + self.filling


def is_prop_valid(prop1, prop2, prop3):
    if prop1 == prop2:
        if prop1 == prop3:
            return True
        else:
            return False
    else:
        if prop1 == prop3:
            return False
        elif prop2 == prop3:
            return False
        else:
            return True


def is_valid(card1, card2, card3):
    return is_prop_valid(card1.color, card2.color, card3.color) \
            and is_prop_valid(card1.form, card2.form, card3.form) \
            and is_prop_valid(card1.number, card2.number, card3.number) \
            and is_prop_valid(card1.filling, card2.filling, card3.filling)


def string_to_cards(card_desc):
    return [Card(x) for x in card_desc]


def find_triplet_in_cards(cards):
    if len(cards) < 3:
        print("Not enough cards: " + str(len(cards)))
        return False

    found = False
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) -1):
            for k in range(j + 1, len(cards)):
                if test_3_cards(cards[i], cards[j], cards[k]):
                    print(cards[i], cards[j], cards[k])
                    found = True

    if not found:
        print("no triplet found")
        return False


def test_3_cards(card1, card2, card3):
    return is_valid(card1, card2, card3)


if __name__ == "__main__":
    cards = string_to_cards(sys.argv[1:])
    find_triplet_in_cards(cards)
