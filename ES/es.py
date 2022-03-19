import numpy as np
from matplotlib import pyplot as plt
target = np.array((0.75, 0.75))

def objective(point):
    return np.sqrt(((point-target)**2).sum())

# print(evaluate(np.array((0,0))))
# print(data)

bounds = np.asarray([[-1.0, 1.0], [-1.0, 1.0]])
start = np.random.rand(len(bounds))


best_score = 1
population = list()

while best_score > 0.05:
    population = list()
    plt.plot(start[0], start[1], marker = "o", color = 'r')

    for i in range(5):
        candidate = start + np.random.randn(len(bounds)) * 0.3
        population.append(candidate)
    # print(population)
    for i in population:
        if objective(i) < best_score:
            best_score = objective(i)
            start = i 
    print(best_score)
    plt.scatter(*zip(*population))
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.plot(target[0], target[1], marker = "o", color = 'k')
    plt.show()

# scores = [objective(c) for c in population]
# print(scores)




