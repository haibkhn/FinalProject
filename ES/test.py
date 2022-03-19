import numpy as np
from matplotlib import pyplot as plt

# bounds = np.asarray([[-1.0, 1.0], [-1.0, 1.0]])

mean = [0,0]
cov = [[1, 0], [0, 1]]

list = list()
for _ in range(10000):
    list.append(np.random.multivariate_normal(mean, cov))
    # list.append(np.random.randn(2))

plt.scatter(*zip(*list))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

# def objective(k):
#     x, y = k
#     return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

# population = list()
# population_score = list()

# for i in range(5):
#     candidate = [0,0] + np.random.multivariate_normal(mean, cov) * 2
#     population.append(candidate)
#     population_score.append(objective(candidate))

# print(population_score)
# print(np.argsort(population_score))
