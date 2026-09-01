import numpy as np

N = 100000

x = np.random.uniform(0,1,N)
y = np.random.uniform(0,1,N)

inside = x**2 + y**2 <= 1

pi_estimate = 4 * np.sum(inside) / N

print(f"pi_estimate = {pi_estimate}")