import numpy as np
from matplotlib import pyplot as plt
from sqlalchemy import true
target = np.array((0.75, 0.75))

def objective(point):
    return np.sqrt(((point-target)**2).sum())

# print(evaluate(np.array((0,0))))
# print(data)

bounds = np.asarray([[-1.0, 1.0], [-1.0, 1.0]])
start = np.random.rand(len(bounds))

fig, axs = plt.subplots(4,4,sharex=True,sharey=True)

best_score = 1
population = list()

for k in range(16):
    population = list()
    plt.plot(start[0], start[1], marker = "o", color = 'r')

    for i in range(5):
        candidate = start + np.random.randn(len(bounds)) * 0.05
        population.append(candidate)
    # print(population)
    for i in population:
        if objective(i) < best_score:
            best_score = objective(i)
            start = i 
    # print(best_score)

    ax = axs[k//4, k%4]
    ax.scatter(*zip(*population), c = 'b')
    ax.scatter(*target, c = 'r')
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])

    # plt.plot(target[0], target[1], marker = "o", color = 'k')

# scores = [objective(c) for c in population]
# print(scores)
plt.show()




