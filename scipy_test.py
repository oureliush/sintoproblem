from scipy.optimize import fsolve
import numpy as np


# Define a function to find the root of: x^2 - 4 = 0
def my_function(x):
    return x**2 - 4

# Provide an initial guess for the root
initial_guess = 1.0

# Call fsolve to find the root
root = fsolve(my_function, initial_guess)

print(f"The root found is: {root[0]}")
