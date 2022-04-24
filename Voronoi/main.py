from shapely.geometry import Point, Polygon
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import false


def input(obstacle_list):
    f = open("input.txt", "r")
    obstacle = []
    for line in f:
        if line == '-1' or line == "-1\n":
            obstacle_list.append(obstacle)
            obstacle = []
        else:
            point = line.split()
            # print(type(float(point[0])))
            obstacle.append(Point(float(point[0]), float(point[1])))
    return obstacle_list


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def shapelyPoint(p):
    return Point(p[0], p[1])


def getEquidistantPoints(p1, p2):
    parts = int(distance(p1, p2)) * 10
    return zip(np.linspace(p1[0], p2[0], parts),
               np.linspace(p1[1], p2[1], parts))


def is_in_list(list_np_arrays, array_to_check):
    return np.any(np.all(array_to_check == list_np_arrays, axis=1))


def getPointInside(polygon, vor_vertice, vor_vertice_inside):
    for p in vor_vertice:
        # print(p)
        if shapelyPoint(p).within(polygon):
            vor_vertice_inside = np.append(vor_vertice_inside, [p], axis=0)
        # if (shapelyPoint(p).within(polygon)):
        #     vor_vertice_outside.append(p)
    return vor_vertice_inside


if __name__ == "__main__":
    obstacle_list = []  # Read points from input.txt, return list of obs
    input(obstacle_list)

    vor_points = []
    coords = []  # Store coord in a polygon
    poly_list = []  # Store all polygons
    vor_vertice_inside = np.array([[-1, -1]])
    # vor_vertice_inside = []

    for obstacle in obstacle_list:
        for point in obstacle:
            vor_points.append((point.x, point.y))
            coords.append((point.x, point.y))

        poly_list.append(Polygon(coords))
        coords = []
        n = len(obstacle)
        for i in range(n - 1):
            vor_points += getEquidistantPoints(
                ((obstacle[i].x, obstacle[i].y)), ((obstacle[i+1].x, obstacle[i+1].y)))
        vor_points += getEquidistantPoints(
            ((obstacle[0].x, obstacle[0].y)), ((obstacle[n-1].x, obstacle[n-1].y)))

    vor = Voronoi(vor_points)
    poly_list.pop()  # Pop last index, because we don't want to treat it like a polygon
    vor_vertice = vor.vertices
    # print(poly_list)
    # for polygon in poly_list:
    #     if Point(2, 2).within(polygon):
    #         print(polygon)
    fig = voronoi_plot_2d(vor)
    plt.show()
    for polygon in poly_list:
        # vor_vertice_inside += getPointOutside(
        #     polygon, vor_vertice, vor_vertice_inside)
        vor_vertice_inside = np.append(vor_vertice_inside, getPointInside(
            polygon, vor_vertice, vor_vertice_inside), axis=0)
    print(len(vor_vertice))
    print(len(vor_vertice_inside))
    # # print(vor_vertice_outside)
    # print(not Point(10, 2).within(poly_list[0]))
