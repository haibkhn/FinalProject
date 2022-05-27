from shapely.geometry import LineString
import matplotlib.pyplot as plt
import numpy as np

line = LineString([(0, 0), (1, 1)])
print(line.boundary[0])
line2 = LineString([(0, 1), (0, 2)])
# print(line2.intersects(line))
paral1 = line.parallel_offset(5, 'left')
paral2 = line.parallel_offset(5, 'right')
# print(paral)
testlinestring = LineString([(-2, 2), (0, 0), (2, 2)])


def getperpen(line):
    paral1 = line.parallel_offset(1, 'left')
    paral2 = line.parallel_offset(1, 'right')
    # print(paral)
    perpen = LineString([paral1.boundary[1], paral2.boundary[0]])
    return perpen


def getvector(line):
    return [line.boundary[0].x-line.boundary[1].x, line.boundary[0].y-line.boundary[1].y]


def angle(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    print(angle)


def plotline(line):
    point1 = line.boundary[0]
    point2 = line.boundary[1]
    x_values = [point1.x, point2.x]
    y_values = [point1.y, point2.y]
    plt.plot(x_values, y_values)


perpen = getperpen(line)

angle(getvector(line), getvector(perpen))
# plotline(line)
# plotline(line2)
# plotline(perpen)

start = [-4, 0]
end = [4, 0]
start_end = LineString([start, end])
plotline(start_end)
middlepoint = []
middlepoint.append(start)
n = 7
for i in range(n):
    x = start[0] + (i+1)/(n+1)*(end[0]-start[0])
    y = start[1] + (i+1)/(n+1)*(end[1]-start[1])
    middlepoint.append([x, y])
middlepoint.append(end)

for i in range(n):
    line = LineString([middlepoint[i], middlepoint[i+1]])
    perpen = getperpen(line)
    print(perpen.intersects(testlinestring))
    print(perpen.intersection(testlinestring))
    # angle(getvector(line), getvector(perpen))

    plotline(perpen)

print(middlepoint)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
