# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# a = [1, 2, 3]
# b = [3]

# prod = product(a, b, repeat=2)
# print(list(prod))  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# a = [1, 2, 3]
# perm = permutations(a, 2)
# print(list(perm))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] 

# a = [1, 2, 3, 4]
# comb = combinations(a, 2) # here 2 is the length of each combination
# print(list(comb))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# comb_wr = combinations_with_replacement(a, 2) # here 2 is the length of each combination
# print(list(comb_wr))  # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# a = [1, 2, 3, 4]
# acc = accumulate(a, func=operator.mul) # here 2 is the length of each combination
# print(list(acc))  # Output: [1, 2, 6, 24], prints accumulated products of the list elements


# acc2= accumulate(a, func=max) # here 2 is the length of each combination

# print(list(acc2))  # Output: [1, 2, 3, 4], prints accumulated maximum of the list elements


def smaller_than_3(x):
    return x < 3


# a = [1, 2, 3, 4]


# persons = [{'name': 'Alice', 'age': 30},
#            {'name': 'Bob', 'age': 25},
#            {'name': 'Charlie', 'age': 35},
#            {'name': 'David', 'age': 30}]
# group_obj = groupby(persons, key=lambda x:x['age']<30)  # here 2 is the length of each combination
# for key, value in group_obj:
#     print(key, list(value))  # Output: True [1, 2] False [3, 4], groups elements based on the key function


a =[1, 2,3 ]
for i in repeat(1, times=4):  # infinite iterator starting from 10
    print(i)

