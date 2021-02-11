# python program to create
# Empty and Full Numpy arrays

import numpy as np


# Create an empty array
empa = np.empty((3, 4), dtype=int)
print("Empty Array")
print(empa)

# Create a full array
flla = np.full([3, 3], 55, dtype=int)
print("\n Full Array")
print(flla)




# Create an empty array
empa = np.empty([4, 2])
print("Empty Array")
print(empa)

# Create a full array
flla = np.full([4, 3], 95)
print("\n Full Array")
print(flla)



import numpy as np

# Create an empty array
empa = np.empty([3,3])
print("Empty Array")
print(empa)

# Create a full array
flla = np.full([5,3], 9.9)
print("\n Full Array")
print(flla)


# Python Program to create array with all zeros
import numpy as geek

a = geek.zeros(3, dtype = int)
print("Matrix a : \n", a)

b = geek.zeros([3, 3], dtype = int)
print("\nMatrix b : \n", b)

c = geek.zeros([5, 3])
print("\nMatrix c : \n", c)

d = geek.zeros([5, 2], dtype=float)
print("\nMatrix d : \n", d)

# Python Program to create array with all ones
import numpy as geek

a = geek.ones(3, dtype = int)
print("Matrix a : \n", a)

b = geek.ones([3, 3], dtype = int)
print("\nMatrix b : \n", b)

#Check whether a Numpy array contains a specified row# importing package

import numpy

# create numpy array
arr = numpy.array([[1, 2, 3, 4, 5],
				[6, 7, 8, 9, 10],
				[11, 12, 13, 14, 15],
				[16, 17, 18, 19, 20]
				])

# view array
print(arr)

# check for some lists
print([1, 2, 3, 4, 5] in arr.tolist())              #True
print([16, 17, 20, 19, 18] in arr.tolist())         #False
print([3, 2, 5, -4, 5] in arr.tolist())             #False
print([11, 12, 13, 14, 15] in arr.tolist())         #True
