# lambda (arg): expression , is a single line nameless function that can take any number of arguments, but can only have one expression. It is used to create small, throwaway functions without having to formally define them using the def keyword.

# add10 = lambda x:x + 10
# print(add10(5))  # Output: 15


# mult = lambda x, y: x * y

# print(mult(3, 4))  # Output: 12


# points2d = [(1, 2), (3, 1), (5, -1), (2, 4)]
# points_2d_sorted = sorted(points2d,key=lambda point: point[1])  # Sort by y-coordinate, sorted also if provided key sorts the list based on the return value of the key function, which is a lambda function in this case that returns the y-coordinate of each point.
# print(points_2d_sorted)  # Output: [(5, -1), (3, 1), (1, 2), (2, 4)]



# map func

# a = [1, 2, 3, 4, 5]

# b = map(lambda x:x*2, a)  # map applies the lambda function to each element of the iterable a and returns an iterator of the results.
# print(list(b))  # Output: [2, 4, 6, 8, 10]



# c  = [x*2 for x in a] # list comprehension is a more pythonic way to achieve the same result as the map function, it creates a new list by applying the expression x*2 to each element x in the iterable a.
# print(c)

'''
filter(func, seq or iterable) -> filter object 

'''

# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x:x%2 ==0 , a)  # filter applies the lambda function to each element of the iterable a and returns an iterator of the elements for which the lambda function returns True.
# print(list(b))  # Output: [2, 4, 6]


# c = [ x for x in a if x%2==0]  # list comprehension is a more pythonic way to achieve the same result as the filter function, it creates a new list by including only the elements x in the iterable a for which the condition x%2==0 is True.
# print(c)  # Output: [2, 4, 6]



'''
    Reduce(func, seq or iterable) -> value
    Applies the function func to the first two elements of the sequence seq, then applies it to the result and the third element, and so on, until a single value is obtained.

'''


a = [1, 2, 3, 4]
from functools import reduce

pa = reduce(lambda x, y: x*y, a)  
print(pa) # Output: 24, reduces the list a by multiplying its elements together, resulting in a single value of 24.