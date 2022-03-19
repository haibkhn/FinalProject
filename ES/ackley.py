import numpy as np

def objective(k):
    x, y = k
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

bounds = np.asarray([[-5.0, 5.0], [-5.0, 5.0]])
start = np.random.rand(len(bounds))


best_score = 100
population = list()
iter = 1
for _ in range(10000):
    
    population = list()
    for i in range(100):
        candidate = start + np.random.randn(len(bounds)) * 0.15
        population.append(candidate)
    for i in population:
        if objective(i) < best_score:
            best_score = objective(i)
            start = i 
    print(iter)
    iter = iter + 1
    print(best_score)
    print(i)




