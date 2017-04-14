# Coin tosses
#
# The PC will toss the coin and count how many times
# head or tail was obtained.
# by mj.c

import random

print ("""
Welcome! Your PC will toss the coin defined times and count it.
""")
decision = int(input("How many times I have to toss the coin?: "))
print("\n")

head = 0
tail = 0

for i in range (1,decision+1):
    coin = random.randint(0,1)
    if coin == 0:
        head += 1
        print (coin, " ")
    elif coin == 1:
        tail += 1
        print (" ", coin)
print ("heads: ",head, "\ttails: ", tail)

if head < tail:
    dif = tail - head
    print ("\nThere are more tails: ", dif)
else:
    dif = head - tail
    print ("\nThere are more heads: ", dif)
