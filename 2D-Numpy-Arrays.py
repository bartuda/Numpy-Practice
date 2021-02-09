# Import numpy
# Create baseball, a list of lists
# Create a 2D numpy array from baseball: np_baseball
# Print out the type of np_baseball
# Print out the shape of np_baseball

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.1],
            [210, 98.5],
            [204, 99.9],
            [207, 97.1],
            [201, 96.5],
            [209, 92.3],
            [202, 98.5],
            [199, 94.9],
            [210, 99.0],
            [210, 98.5],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)
print()
print(type(np_baseball))
print(np_baseball.shape)
print()

# Print out the 10th row of np_baseball
# Print out height of 4th player

print(np_baseball[9, :])
print(np_baseball[3, 0])
print()

# Create numpy array: conversion
# Print out product of np_baseball and conversion
conversion = [10, 5]
print(np_baseball * conversion)

