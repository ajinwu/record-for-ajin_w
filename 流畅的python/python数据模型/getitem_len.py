import collections
# 创建具名元组, 生成具名对象
Card = collections.namedtuple("card",["rank","suit"])

class FrenchDeck:
    ranks = [ str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    # 这里返回的是一个列表, 即init对象返回的是一个列表
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)
    
    # 因为返回的是列表对象, 所以可以使用getitem魔法方法可以返回固定位置的数值
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
# print(len(deck))
# print(deck[-1])
# from random import choice
# print(choice(deck))
# print(deck[:3])
for i in range(0,3):
    print(deck[i])

print(Card("A", "heart") in deck)
print(Card("A", "hearts") in deck)

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print(card)