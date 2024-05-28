import numpy as np

a = np.random.rand(2, 3)  # Generates a 2x3 array of random numbers
print(a)
b = np.random.randn(3, 3)  # Generates a 3x3 array of random numbers from a standard normal distribution
print(b)
c = np.random.randint(1, 10,size=(2,5))  # Generates a 2x3 array of random integers between 1 and 10
print(c)
d = np.random.random_sample((2, 3))  # Generates a 2x3 array of random numbers
print(d)
e = np.random.choice([1, 2, 3, 4, 5], size=(2, 3))  # Generates a 2x3 array by randomly sampling from the provided list
print(e)

# f = np.random.choice([1, 2, 3, 4, 5])  # Generates a 2x3 array by randomly sampling from the provided list
f = np.random.choice([1,4,3,5])  # Generates a 2x3 array by randomly sampling from the provided list
print(f)
