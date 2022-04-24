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


def is_in_list(list_np_arrays, array_to_check):
    k = np.any(np.all(array_to_check == list_np_arrays, axis=1))
    return k


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def shapelyPoint(p):
    return Point(p[0], p[1])


def getEquidistantPoints(p1, p2):
    parts = int(distance(p1, p2)) * 10
    return zip(np.linspace(p1[0], p2[0], parts),
               np.linspace(p1[1], p2[1], parts))


def getPointOutside(polygon, vor_vertice, vor_vertice_outside):
    for p in vor_vertice:
        # print(p)
        if (not shapelyPoint(p).within(polygon)) and (is_in_list(vor_vertice_outside, p) == False):
            vor_vertice_outside = np.append(vor_vertice_outside, [p], axis=0)
        # if (not shapelyPoint(p).within(polygon)) and (not is_in_list(vor_vertice_outside, np.array(p))):
        #     vor_vertice_outside.append(p)
    return vor_vertice_outside


if __name__ == "__main__":
    obstacle_list = []  # Read points from input.txt, return list of obs
    input(obstacle_list)

    vor_points = []
    coords = []  # Store coord in a polygon
    poly_list = []  # Store all polygons
    vor_vertice_outside = np.array([[-1, -1]])

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

    vor_vertice = vor.vertices
    # for obstacle in obstacle_list:
    #     for polygon in poly_list:
    #         vor_vertice_outside = np.append(vor_vertice_outside, getPointOutside(
    #             polygon, vor_vertice, vor_vertice_outside), axis=0)
    # print(len(vor_vertice))
    # print(len(vor_vertice_outside))
    # print(vor_vertice_outside)
    print(Point(10, 2).within(poly_list[0]))
    fig = voronoi_plot_2d(vor)
    plt.show()
