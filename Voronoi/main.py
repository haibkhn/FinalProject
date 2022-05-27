from cmath import inf
from shapely.geometry import Point, Polygon, LineString
from shapely.ops import voronoi_diagram
from dijkstar import Graph, find_path
from dijkstar.algorithm import PathInfo
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

INPUT = 27


def inputObs(obstacle_list):
    # f = open("obs/input" + str(INPUT) + ".txt", "r")
    # f = open("obs/obstacles.txt", "r")
    f = open("input/obstacle_" + str(INPUT)+".txt", "r")
    obstacle = []
    for line in f:
        if line == '-1' or line == "-1\n":
            obstacle_list.append(obstacle)
            obstacle = []
        else:
            point = line.split()
            obstacle.append(Point(float(point[0])/10, float(point[1])/10))
            # obstacle.append(Point(float(point[0]), float(point[1])))

    obstacle_list.pop(0)
    # print(obstacle_list)
    sur = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
    obstacle_list.append(sur)
    return obstacle_list


def inputTarget(target_list):
    f = open("input/input_" + str(INPUT) + ".txt", "r")
    for line in f:
        if line == '-1' or line == "-1\n":
            return target_list
        else:
            point = line.split()
            target_list.append(Point(float(point[0])/10, float(point[1])/10))
    return target_list


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def shapelyPoint(p):
    return Point(p[0], p[1])


def getEquidistantPoints(p1, p2):
    parts = int(distance(p1, p2)*12)
    x = np.linspace(p1[0], p2[0], parts, endpoint=False)
    x = x[1:]
    y = np.linspace(p1[1], p2[1], parts, endpoint=False)
    y = y[1:]
    return zip(x, y)


def is_in_list(list_np_arrays, array_to_check):
    return np.any(np.all(array_to_check == list_np_arrays, axis=1))


def getperpen(line):
    paral1 = line.parallel_offset(10, 'left')
    paral2 = line.parallel_offset(10, 'right')
    # print(paral)
    perpen = LineString([paral1.boundary[1], paral2.boundary[0]])
    return perpen


def getvector(line):
    return [line.boundary[0].x-line.boundary[1].x, line.boundary[0].y-line.boundary[1].y]


def plotline(line):
    point1 = line.boundary[0]
    point2 = line.boundary[1]
    x_values = [point1.x, point2.x]
    y_values = [point1.y, point2.y]
    plt.plot(x_values, y_values)


def plotpoint(point):
    plt.plot([point[0]], [point[1]], marker="o", markersize=10,
             markeredgecolor="red", markerfacecolor="green")


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
    fig = voronoi_plot_2d(vor)

    # Find closest points to all target
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

    def distance(v1, v2):
        return np.sqrt(np.sum((v1 - v2) ** 2))

    # khởi tạo 1 cái graph
    # kiểm tra cái ridge_vertices đều >= 0 thì thêm vào edge vào graph
    # mình phải thêm edge [0][1] và edge [1][0] để tạo thành đồ thị vô hướng
    # còn nếu chỉ thêm edge 1 lần thì nó là đồ thị có hướng
    graph = Graph()
    for vpair in vor.ridge_vertices:
        if vpair[0] >= 0 and vpair[1] >= 0 and (vor_check[vpair[0]][2] != 1) and (vor_check[vpair[1]][2] != 1):
            graph.add_edge(vpair[0], vpair[1], distance(
                vor.vertices[vpair[0]], vor.vertices[vpair[1]]))
            graph.add_edge(vpair[1], vpair[0], distance(
                vor.vertices[vpair[0]], vor.vertices[vpair[1]]))
    # điểm bắt đầu và kết thúc trong số vertices của voronoi
    # ở đây mình sẽ tìm node gần nhất với start và node gần nhất với end
    start = [target_list[0].x, target_list[0].y]
    end = [target_list[1].x, target_list[1].y]

    start_graph = 0
    end_graph = 0
    min_dist_start = 100000
    min_dist_end = 100000
    for i in range(len(vor_vertice)):
        if (distance(start, vor_vertice[i]) < min_dist_start) and (vor_check[i][2] != 1):
            min_dist_start = distance(start, vor_vertice[i])
            start_graph = i
        if (distance(end, vor_vertice[i]) < min_dist_end) and (vor_check[i][2] != 1):
            min_dist_end = distance(end, vor_vertice[i])
            end_graph = i

    # nối từ điểm start và end đến điểm gần nhất trong voronoi vertices
    plt.plot([start[0], vor_vertice[start_graph][0]], [
             start[1], vor_vertice[start_graph][1]], 'k', linewidth=2)
    plt.plot([end[0], vor_vertice[end_graph][0]], [
             end[1], vor_vertice[end_graph][1]], 'k', linewidth=2)

    # liệt kê các đỉnh đi qua từ start_graph đến end_graph
    node_list = find_path(graph, start_graph, end_graph).nodes
    print(node_list)
    print(vor_vertice[node_list[0]])
    voronoiNodeCoord = []

    # Append real coordianate to voronoiNodeCoord, not index
    for i in node_list:
        voronoiNodeCoord.append((vor.vertices[i][0], vor.vertices[i][1]))
        plt.plot([vor.vertices[i][0]], [vor.vertices[i][1]],
                 marker='o', markersize=5, color="red")

    plt.scatter(xs, ys, c="r")
    for i in range(len(target_list)):
        plt.plot([target_list[i].x, target_list_closest_index[i][0]], [
            target_list[i].y, target_list_closest_index[i][1]], color="red", linewidth=5)

    print(voronoiNodeCoord)
    # Create a linestring from start to end
    vorolinestring = LineString(voronoiNodeCoord)
    start_end = LineString([start, end])
    plotline(start_end)

    middlepoint = []
    middlepoint.append(start)

    n = 10  # Number of dimension
    for i in range(n):
        x = start[0] + (i+1)/(n+1)*(end[0]-start[0])
        y = start[1] + (i+1)/(n+1)*(end[1]-start[1])
        middlepoint.append([x, y])
    middlepoint.append(end)

    # Find point which cut between voronoi and perpencular line
    for i in range(n):
        line = LineString([middlepoint[i], middlepoint[i+1]])
        perpen = getperpen(line)
        print(perpen.intersects(vorolinestring))
        print(perpen.intersection(vorolinestring))
        # angle(getvector(line), getvector(perpen))

        plotline(perpen)
    plotpoint([2.7059261, 4.0213466])
    plotpoint([3.1084492, 4.3460963])
    plotpoint([4.4189145, 3.7629036])

    plt.axis([0, 10, 0, 10])
    plt.show()
