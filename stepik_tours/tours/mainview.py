import random

from .data import tours

masiv = []
kol = 0
while len(masiv) <= 5:
    a = random.randint(1, 16)
    for i in masiv:
        if i != a:
            kol += 1
    if len(masiv) == kol:
        masiv.append(a)
    kol = 0

new_dict = {}
for key, value in tours.items():
    for i in masiv:
        if key == i:
            new_dict.update({key: value})
