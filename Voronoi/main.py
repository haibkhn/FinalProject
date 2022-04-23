from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


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
            obstacle.append(Point(point[0], point[1]))


if __name__ == "__main__":
    input()
    print(obstacle_list)
    # p = Point(5, 5)
    # obstacle = []
    # obstacle.append(p)
    # print(obstacle[0].x)
