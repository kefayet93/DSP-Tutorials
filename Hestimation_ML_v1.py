import numpy as np
import matplotlib.pyplot as plt

def estimate_channel_ML(x,y):
    """
    Maximum Likeliood estimation of a flat fading wireless channel

    Parameters:
    x(np.ndarray): Transmitted complex baseband samples (1D array)
    y(np.ndarray): Received complex baseband samples (1D array)

    Returns:
    h_ML(complex): Estimated channel coefficient using ML method
    """

    x = np.array(x, dtype=np.complex64)
    y = np.array(y, dtype=np.complex64)
    
    # Computing ML estimate

    numerator = np.sum(np.conj(x) * y)
    denominator = np.sum(np.abs(x)**2)

    h_ML = numerator / denominator
    return h_ML

# Given complex basband samples
x = [1+1j, 1-1j, 2-1j, 1+2j]
#y = [3+5j, -5-3j, 2+3j, -3-2j]

# Defining the channel coefficient for comparison
h_true = 1.5 + 0.5j

# Generating the received samples (y) based on this true channel (h_true)
noise = 0.1 * (np.random.randn(len(x)) + 1j * np.random.randn(len(x)))
y = h_true * np.array(x) + noise


# Estimate the channel using ML method
h_est = estimate_channel_ML(x,y)


print(f"True channel coefficient h_true: {h_true:.4f}")
print(f"Estimated channel coefficient h_ML: {h_est:.4f}")
print(f"Estimated error magnitude |h_ML - h_true|: {np.abs(h_est - h_true):.4e}")