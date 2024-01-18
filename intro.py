import numpy as np

# Create a simple 1-dimensional array
my_array = np.array([1, 2, 3, 4, 5])

print("Original array:", my_array)

# Shuffle the array in-place
np.random.shuffle(my_array)

print("Shuffled array:", my_array)
