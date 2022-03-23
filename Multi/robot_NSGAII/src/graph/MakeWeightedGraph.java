package graph;

import java.util.LinkedList;

import algorithm.AStar;
import util.Graph;
import util.Line;
import util.Point;

public class MakeWeightedGraph {
	LinkedList<Point> visitPoints;
	int n;
	public double[][] array;

	public MakeWeightedGraph(Graph myGraph, LinkedList<Point> visitPoints, LinkedList<Point> midPoints,
			LinkedList<Line> linesMAKLINK) {
		this.visitPoints = visitPoints;
		n = visitPoints.size();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i == j)
					array[i][j] = 0;
				else {
					AStar findPath = new AStar(myGraph, midPoints, linesMAKLINK, visitPoints.get(i),
							visitPoints.get(j));
					array[i][j] = findPath.length;
					array[j][i] = findPath.length;
				}
			}
		}
	}

}
