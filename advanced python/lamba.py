# lambda (arg): expression , is a single line nameless function that can take any number of arguments, but can only have one expression. It is used to create small, throwaway functions without having to formally define them using the def keyword.

# add10 = lambda x:x + 10
# print(add10(5))  # Output: 15


mult = lambda x, y: x * y

# print(mult(3, 4))  # Output: 12


points2d = [(1, 2), (3, 1), (5, -1), (2, 4)]
points_2d_sorted = sorted(points2d,key=lambda point: point[1])  # Sort by y-coordinate, sorted also if provided key sorts the list based on the return value of the key function, which is a lambda function in this case that returns the y-coordinate of each point.
print(points_2d_sorted)  # Output: [(5, -1), (3, 1), (1, 2), (2, 4)]

