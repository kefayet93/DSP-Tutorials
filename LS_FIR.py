import numpy as np
import matplotlib.pyplot as plt

# Creating input
x = np.array([1, 2, 3, 4, 5, 6]) # Transmtted input signl (1D array)
y = np.array([2.9, 6.0, 9.1, 12.2]) # Received ouput signal (1D array)
L = 3; # Filter length

def estimate_fir_ls(x,y,L):
    x = np.asarray(x).flatten() # np.asarraay() ensures "x" is a NumPy array,
    # and .flatten() makes them 1D)
    y = np.asarray(y).flatten() # np.asarraay() ensures "y" is a NumPy array,
    # and .flatten() makes them 1D)
    N = len(x) # totlal number of samples in the input signal "x"

    if len(y)!=N:
        raise ValueError("x and y must be the same length")
    # Ensures "x" and "y" have the same number of samples and raises an 
    # error if they don't.

    # Creating the input matrix X
    num_rows = N - L + 1 # Number of rows in the input matrix
    X = np.zeros((num_rows,L))

    for i in range(num_rows):
        X[i,:] = x[i+L-1:i-1:-1] # flipped window
        
    y_trunc = y[L-1:] # Truncated output signal to match the input matrix size

h = estimate_fir_ls(x,y,L)