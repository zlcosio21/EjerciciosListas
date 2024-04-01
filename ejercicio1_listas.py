# Given two lists
# (list1 and list2),
# return
# the sum of list1 and list2,
# and another one for the subtraction.

def operations_list(list1, list2):
    sum_result = sum(list1) + sum(list2)
    sub_result = sum(list1) - sum(list2)
    return sum_result, sub_result
