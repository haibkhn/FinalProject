import numpy as np
from matplotlib import pyplot as plt
# target = np.array((0.75, 0.75))

def objective(k):
    x, y = k
    # return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

# print(evaluate(np.array((0,0))))
# print(data)

bounds = np.asarray([[-100.0, 100.0], [-100.0, 100.0]])
start = np.random.rand(len(bounds))


best_score = 100
population = list()
iter = 1
for _ in range(10000):
    
    population = list()
    # plt.plot(start[0], start[1], marker = "o", color = 'r')

    for i in range(100):
        candidate = start + np.random.randn(len(bounds)) * 0.25
        population.append(candidate)
    # print(population)
    for i in population:
        if objective(i) < best_score:
            best_score = objective(i)
            start = i 
    print(iter)
    iter = iter + 1
    print(best_score)
    print(i)
    # print()
    

    # plt.scatter(*zip(*population))
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.plot(target[0], target[1], marker = "o", color = 'k')
    # plt.show()

# scores = [objective(c) for c in population]
# print(scores)




