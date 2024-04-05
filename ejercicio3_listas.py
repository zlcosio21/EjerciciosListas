# Given a list of 10 integers,
# show the original list
# and the inverse of this

import random

def reverse_list():
    list_ = list(random.randint(1, 100) for i in range(0, 10))

    return list_, list(reversed(list_))
