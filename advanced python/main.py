# collections -> Couonter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, defaultdict, deque

# my_counter = Counter("aaabbbcccc")
# print(my_counter.most_common(1))  # Output: Counter({'c': 4, 'a': 3, 'b': 3})

# print(list(my_counter.elements()))  # Output: ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']    




# Point = namedtuple('Point', 'x,y')
# pt = Point(-1, 4)
# print(pt.x, pt.y)  # Output: -1 4





# ordered dict is a dictionary subclass that maintains the order in which items are inserted. In Python 3.7 and later, the built-in dict type also maintains insertion order, so OrderedDict is less commonly used.
# but after python 3.7, the built-in dict type maintains insertion order, so OrderedDict is less commonly used.



# dict1 = defaultdict(int)

# dict1['a'] += 1
# dict1['b'] += 2


# print(dict1['a'])  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})


d = deque([1, 2, 3])
d.append(4)  # Add to the right
d.appendleft(0)  # Add to the left

print(d)  # Output: deque([0, 1, 2, 3, 4])

# popleft -> pops first element from the left


d.rotate(1)  # Rotate right by 1
print(d)  # Output: deque([4, 0, 1, 2, 3])

d.rotate(-1)  # Rotate left by 1
print(d)  # Output: deque([0, 1, 2, 3, 4])