// package graph;

// import java.io.FileInputStream;
// import java.io.FileNotFoundException;
// import java.util.ArrayList;
// import java.util.Scanner;

// import util.Point;

// public class ObstaclesGraph {

// 	public ArrayList<Point> points;

// 	public ObstaclesGraph(ArrayList<Point> points) {
// 		this.points = points;
// 	}

// 	public static ArrayList<ObstaclesGraph> getObstacles(String path_file) {
// 		ArrayList<ObstaclesGraph> obstacles = new ArrayList<ObstaclesGraph>();

// 		try {
// 			System.setIn(new FileInputStream(path_file));
// 		} catch (FileNotFoundException e) {
// 			System.err.println("File " + path_file + " Not Found");
// 			return null;
// 		}

// 		Scanner sc = new Scanner(System.in);
// 		ArrayList<Point> points = null;

// 		while (sc.hasNext()) {
// 			String s = sc.nextLine();
// 			if (s.equals("-1")) {
// 				if (points != null && points.size() != 0)
// 					obstacles.add(new ObstaclesGraph(points));
// 				points = new ArrayList<>();
// 				continue;
// 			}

// 			String temp[] = s.split("\\s+");
// 			points.add(new Point(Double.parseDouble(temp[0]), Double.parseDouble(temp[1])));
// 		}
// 		sc.close();
// 		return obstacles;
// 	}

// 	public static void main(String[] args) {
// 		ArrayList<ObstaclesGraph> obstacles = ObstaclesGraph.getObstacles("MOES/obstacles.txt");
// 		for (ObstaclesGraph obstacle : obstacles) {
// 			for (Point point : obstacle.points) {
// 				System.out.print("(" + point.x + ", " + point.y + ")\t");
// 			}
// 			System.out.println();
// 		}
// 	}
// }
package graph;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class ObstaclesGraph {
	public static class Point {
		public double x;
		public double y;

		public Point(double x, double y) {
			this.x = x;
			this.y = y;
		}
	}

	public ArrayList<Point> points = new ArrayList<Point>();
	public ArrayList<Point> borders = new ArrayList<Point>();
	double ratio;

	public ObstaclesGraph(ArrayList<Point> points, double ratio) {
		this.borders = points;
		this.ratio = ratio;
		calculateObstacles(this.borders, ratio);
	}

	public void calculateObstacles(ArrayList<Point> borders, double ratio) {
		double x = 0;
		double y = 0;
		for (Point vertex : borders) {
			x += vertex.x;
			y += vertex.y;
		}
		Point pt = new Point(x / borders.size(), y / borders.size());
		for (Point vertex : borders) {
			double new_x = ratio * (vertex.x - pt.x) + pt.x;
			double new_y = ratio * (vertex.y - pt.y) + pt.y;
			this.points.add(new Point(new_x, new_y));
		}

	}

	public static ArrayList<ObstaclesGraph> getObstacles(String path_file, double ratio) {
		ArrayList<ObstaclesGraph> obstacles = new ArrayList<ObstaclesGraph>();

		try {
			System.setIn(new FileInputStream(path_file));
		} catch (FileNotFoundException e) {
			System.err.println("File " + path_file + " Not Found");
			return null;
		}

		Scanner sc = new Scanner(System.in);
		ArrayList<Point> points = null;

		while (sc.hasNext()) {
			String s = sc.nextLine();
			if (s.equals("-1")) {
				if (points != null && points.size() != 0)
					obstacles.add(new ObstaclesGraph(points, ratio));
				points = new ArrayList<>();
				continue;
			}

			String temp[] = s.split("\\s+");
			points.add(new Point(Double.parseDouble(temp[0]), Double.parseDouble(temp[1])));
		}
		sc.close();
		return obstacles;
	}

	public static void main(String[] args) {
		double ratio = 0.9;

		ArrayList<ObstaclesGraph> obstacles = ObstaclesGraph.getObstacles("obstacles.txt", ratio);
		for (ObstaclesGraph obstacle : obstacles) {
			for (Point point : obstacle.points) {
				System.out.print("(" + point.x + ", " + point.y + ")\t");
			}
			System.out.println();
		}
	}
}
