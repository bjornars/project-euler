from operator import itemgetter
#from lib import trace

# constants for hand-types
SF = 9
FK = 8
FH = 7
FL = 6
ST = 5
TK = 4
TP = 3
OP = 2
NN = 1

def is_straight(cards):
    cards = sorted(map(itemgetter(0), cards))
    if len(set(cards)) == 5:
        if (cards[-1] - cards[0] == 4):
            return True, cards[-1]
        elif cards == [2,3,4,5,14]:
            return True, 5

    return False, 0

def is_flush(cards):
    return len(set(map(itemgetter(1), cards))) == 1, sorted(map(itemgetter(0), cards), reverse=True)

def is_n_like(cards, n):
    cards = sorted(map(itemgetter(0), cards))
    likes = sorted(set(cards), key=cards.count)
    top = likes[-1]
    if cards.count(top) == n:
        likes.sort(reverse=True)
        likes.sort(key=cards.count, reverse=True)
        return True, likes

    return False, 1

def is_full_house(cards):
    cards = sorted(map(itemgetter(0), cards))
    return len(set(cards)) == 2, sorted(set(cards), key=cards.count, reverse=True)

#@trace
def is_two_pairs(cards):
    cards = sorted(map(itemgetter(0), cards))
    cards = sorted(cards, key=cards.count, reverse=True)
    return cards.count(cards[0]) == 2 and cards.count(cards[2]) == 2, \
           sorted(sorted(set(cards), reverse=True), key=cards.count, reverse=True)

#@trace
def get_hand(*cards):
    # NB: Some of the functions for figuring out hands only work when called in order
    straight, sm = is_straight(cards)
    flush, fm = is_flush(cards)

    if straight:
        if flush:
            return SF, sm
        else:
            return ST, sm

    if flush: # flush
        return (FL, ) + tuple(fm)

    four_kind, m = is_n_like(cards, 4)
    if four_kind:
        return (FK, ) + tuple(m)

    full_house, m = is_full_house(cards)
    if full_house:
        return (FH, ) + tuple(m)

    three_kind, m = is_n_like(cards, 3)
    if three_kind:
        return (TK, ) + tuple(m)

    two_pairs, m = is_two_pairs(cards)
    if two_pairs:
        return (TP, ) + tuple(m)

    pair, m = is_n_like(cards, 2)
    if pair:
        return (OP, ) + tuple(m)

    return (NN, ) + tuple(sorted(map(itemgetter(0), cards), reverse=True))

def winner(a, b):
    if a[0] == b[0]:
        assert len(a) == len(b)

    for x, y in zip(a, b):
        if x > y: return True
        if x < y: return False
    assert False

def make_card(s):
    v = s[:-1]
    pictures = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    v = pictures.get(v) or int(v)
    return (v, s[-1])

# tests!
assert make_card('14S') == (14, 'S')

def _get_hand(*cards): return get_hand(*map(make_card, cards))

assert _get_hand('14S', '13S', '12S', '11S', '10S') == (SF, 14)
assert _get_hand('14S', '2S', '3S', '4S', '5S') == (SF, 5)
assert _get_hand('14S', '13D', '12S', '11S', '10S') == (ST, 14)
assert _get_hand('14S', '2D', '3S', '4S', '5S') == (ST, 5)
assert _get_hand('14S', '13S', '12S', '11S', '9S') == (FL, 14, 13, 12, 11, 9)
assert _get_hand('14S', '6S', '3S', '4S', '5S') == (FL, 14, 6, 5, 4, 3)
assert _get_hand('14S', '14D', '14C', '14H', '5S') == (FK, 14, 5)
assert _get_hand('14S', '14D', '14C', '5D', '5S') == (FH, 14, 5)
assert _get_hand('14S', '14D', '5C', '5D', '5S') == (FH, 5, 14)
assert _get_hand('14S', '13D', '5C', '5D', '5S') == (TK, 5, 14, 13)
assert _get_hand('14S', '14D', '14C', '6D', '5S') == (TK, 14, 6, 5)
assert _get_hand('14S', '14D', '5C', '5D', '5S') == (FH, 5, 14)
assert _get_hand('14S', '14D', '5C', '5D', '6D') == (TP, 14, 5, 6)
assert _get_hand('14S', '6D', '5C', '6C', '5S') == (TP, 6, 5, 14)
assert _get_hand('14S', '14D', '5C', '13D', '6D') == (OP, 14, 13, 6, 5)
assert _get_hand('14S', '6D', '13C', '6C', '5S') == (OP, 6, 14, 13, 5)
assert _get_hand('14S', '4D', '13C', '6C', '5S') == (NN, 14, 13, 6, 5, 4)

assert not winner(_get_hand('14S', '4D', '13C', '6C', '5S'), _get_hand('14S', '6D', '5C', '6C', '5S'))
assert winner(_get_hand('14S', '13S', '12S', '11S', '10S'), _get_hand('14S', '6D', '5C', '6C', '5S'))
assert winner(_get_hand('14S', '13S', '12S', '11S', '10S'), _get_hand('14S', '2S', '3S', '4S', '5S'))

# actual problem
w = 0
for x in open('54.txt'):
    hands = map(make_card, x.split())
    h1, h2 = hands[0:5], hands[5:10]
    if winner(get_hand(*h1), get_hand(*h2)):
        w += 1

print w
