# Given two lists of characters,
# counting differences is required
# between them and display said count.
# ○ Example: If you have the lists
# [“A”, “B”, “C”] and [“A”, “E”, “H”],
# then the count would be 2 since
# there are two differences.
# Note: The lists must be of equal
# length and this must be validated.

import random
import string

def differences(range_lists):
    list_1 = [random.choice(string.ascii_uppercase) for i in range(0, range_lists)]
    list_2 = [random.choice(string.ascii_uppercase) for i in range(0, range_lists)]
    count = sum([1 for i in list_1 if list_1[list_1.index(i)] != list_2[list_1.index(i)]])

    return list_1, list_2, count
