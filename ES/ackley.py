import numpy as np

def objective(k):
    x, y = k
    # return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

bounds = np.asarray([[-5.0, 5.0], [-5.0, 5.0]])
start = np.random.rand(len(bounds))
mean = [0,0]
cov = [[1, 0], [0, 1]]
best, best_eval = None, 1e+10
child = 100 #So con sinh ra trong 1 the he
mu = 20 #So con tot nhat duoc chon
# best_score = 100
population = list()
population_score = list()
iter = 1
standard_devi = 0.25
for _ in range(1000):
    population = list() 
    population_score = list() #Tinh fitness tung ca the
    selected = list()
    for i in range(child):
        #generate candidate base on start point, append to population, then select mu best child
        candidate = start + np.random.multivariate_normal(mean, cov) * standard_devi
        population.append(candidate)
        population_score.append(objective(candidate))

    population_score_sorted = np.argsort(population_score)

    #Select mu best children
    for i in range(mu):
        selected.append(population[population_score_sorted[i]])

    # for i in selected:
        # Check if this parent is the best solution ever seen
    if objective(selected[0]) < best_eval:
        best, best_eval = selected[0], objective(selected[0])
        print('%d, Best: f(%s) = %.5f' % (iter, best, best_eval))

    start = np.mean(selected, axis=0)

    iter = iter + 1