import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))
#########################################################################
height_in = [69, 74, 72, 72, 73, 69, 69, 71, 76, 71]
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180]

np_height_in = np.array(height_in)
np_weight_lb = np.array(weight_lb)
print(np_height_in)
print(np_weight_lb)

# Convert np_height_in to m: np_height_m
np_height_m = (np_height_in * 0.0254)

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2
print(bmi)

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
