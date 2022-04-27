from cmath import inf
from shapely.geometry import Point, Polygon, MultiPoint
from shapely.ops import voronoi_diagram

from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np


def inputObs(obstacle_list):
    f = open("obs/input2.txt", "r")
    # f = open("obs/obstacles.txt", "r")
    obstacle = []
    for line in f:
        if line == '-1' or line == "-1\n":
            obstacle_list.append(obstacle)
            obstacle = []
        else:
            point = line.split()
            # obstacle.append(Point(float(point[0])/10, float(point[1])/10))
            obstacle.append(Point(float(point[0]), float(point[1])))
    return obstacle_list


def inputTarget(target_list):
    f = open("target/target.txt", "r")
    for line in f:
        point = line.split()
        target_list.append(Point(float(point[0]), float(point[1])))
    return target_list


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def shapelyPoint(p):
    return Point(p[0], p[1])


def getEquidistantPoints(p1, p2):
    parts = int(distance(p1, p2)*10)
    x = np.linspace(p1[0], p2[0], parts, endpoint=False)
    x = x[1:]
    y = np.linspace(p1[1], p2[1], parts, endpoint=False)
    y = y[1:]
    return zip(x, y)


def is_in_list(list_np_arrays, array_to_check):
    return np.any(np.all(array_to_check == list_np_arrays, axis=1))


if __name__ == "__main__":
    obstacle_list = []  # Read points from input.txt, return list of obs
    inputObs(obstacle_list)
    target_list = []
    inputTarget(target_list)

    xs = [point.x for point in target_list]
    ys = [point.y for point in target_list]

    vor_points = []
    coords = []  # Store coord in a polygon
    poly_list = []  # Store all polygons

    for obstacle in obstacle_list:
        for point in obstacle:
            vor_points.append((point.x, point.y))
            coords.append((point.x, point.y))

        poly_list.append(Polygon(coords))  # Turn list of coords into polygon
        coords = []
        n = len(obstacle)
        for i in range(n-1):
            vor_points += getEquidistantPoints(
                ((obstacle[i].x, obstacle[i].y)), ((obstacle[i+1].x, obstacle[i+1].y)))
        vor_points += getEquidistantPoints(
            ((obstacle[0].x, obstacle[0].y)), ((obstacle[n-1].x, obstacle[n-1].y)))
    poly_list.pop()  # Pop last index, because we don't want to treat it like a polygon

    vor = Voronoi(vor_points)
    vor_vertice = vor.vertices
    vor_check = np.hstack((vor_vertice, np.zeros(
        (vor_vertice.shape[0], 1), dtype=vor_vertice.dtype)))  # Make new col from vor_vertice, if inside -> make value of new col = 1
    for polygon in poly_list:
        for p in vor_check:
            if shapelyPoint([p[0], p[1]]).within(polygon):
                p[2] = 1

    target_list_closest_index = [0] * len(target_list)
    i = 0
    for target in target_list:
        min_distance = inf
        j = 0
        for pts in vor_vertice:
            if vor_check[j][2] != 1 and target.distance(Point(pts)) < min_distance:
                # If element min, store the index
                target_list_closest_index[i] = vor_vertice[j]
                min_distance = target.distance(Point(pts))
            j += 1
        i += 1

    fig = voronoi_plot_2d(vor)
    plt.scatter(xs, ys, c="r")
    for i in range(len(target_list)):
        plt.plot([target_list[i].x, target_list_closest_index[i][0]], [
            target_list[i].y, target_list_closest_index[i][1]], color="red", linewidth=3)
    plt.axis([0, 12, 0, 12])
    plt.show()
