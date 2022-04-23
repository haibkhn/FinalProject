from dis import dis
from shapely.geometry import Point
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
obstacle_list = []


def input():
    f = open("C:\Workplaec\Robot\FinalProject\Voronoi\input.txt", "r")
    obstacle = []
    for line in f:
        if line == '-1' or line == "-1\n":
            obstacle_list.append(obstacle)
            obstacle = []
        else:
            point = line.split()
            # print(type(float(point[0])))
            obstacle.append(Point(float(point[0]), float(point[1])))


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def getEquidistantPoints(p1, p2):
    parts = int(distance(p1, p2)) * 10
    return zip(np.linspace(p1[0], p2[0], parts),
               np.linspace(p1[1], p2[1], parts))


if __name__ == "__main__":
    input()

    vor_points = []
    # points = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
    #           [2, 0], [2, 1], [2, 2]]

    for obstacle in obstacle_list:
        for point in obstacle:
            vor_points.append((point.x, point.y))
            # xs.append(point.x)
            # ys.append(point.y)
        n = len(obstacle)
        for i in range(n - 1):
            vor_points += getEquidistantPoints(
                ((obstacle[i].x, obstacle[i].y)), ((obstacle[i+1].x, obstacle[i+1].y)))
        vor_points += getEquidistantPoints(
            ((obstacle[0].x, obstacle[0].y)), ((obstacle[n-1].x, obstacle[n-1].y)))
    # xs = [i[0] for i in vor_points]
    # ys = [i[1] for i in vor_points]
    # print(vor_points)
    # plt.scatter(xs, ys)
    vor = Voronoi(vor_points)
    fig = voronoi_plot_2d(vor)
    plt.show()
