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

# Create np_height_cm from np_baseball
# Print out the mean of np_height_cm
# Print out the median of np_height_cm
np_height_cm = np.array(np_baseball[:, 0])
print(np.mean(np_height_cm))
print(np.median(np_height_cm))
print()

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:,1])
print("Correlation: " + str(corr))
print()

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