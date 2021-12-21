# shuffle deck of cards

import random, itertools

# make a deck of cards

deck = list(itertools.product(range(1,14), ['Spade', 'Heart', 'Diamond', 'Club']))

random.shuffle(deck)
for i in range(5):
	print(deck[i][0], deck[i][1])