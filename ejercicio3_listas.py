# Given a list of 10 integers,
# it is required to print those numbers
# in reverse order to which they were entered.

import random

def reverse_list():
    reverse_list = []

    for i in range(0, 10):
        reverse_list.append(random.randint(1, 1000))

    return list(reversed(reverse_list))
