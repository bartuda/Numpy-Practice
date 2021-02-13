# Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np
x = np.array([1, 2, 3, 4])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

x = np.array([0, 1, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

# Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np
x = np.array([1, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))

x = np.array([0, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))