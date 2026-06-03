import numpy as np
import matplotlib.pyplot as plt

time_horizon = 252
n_paths = 10
mu = 0.05
sigma = 0.20
initial_price = 152
dt = 1/252

y = np.zeros((time_horizon, n_paths))
y[0, :] = initial_price

for t in range(1, time_horizon):
    random_shocks = np.random.normal(0, 1, n_paths)
    y[t, :] = y[t - 1, :] * np.exp((mu - 0.5*sigma**2)*dt + np.sqrt(dt)*sigma*random_shocks)

plt.figure(figsize=(10, 6))
plt.plot(y)
plt.title(f"Geometric Brownian Motion: {n_paths} Simulated Paths")
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.grid(True)
plt.savefig('Geometric_brownian_motion.png', dpi=300)
plt.show()