package algorithm;

import java.util.LinkedList;
import java.util.Random;

import util.Graph;
import util.Path;
import util.Point;

public class ES {
    public final int NP = 100; // population size
    public Path particles[] = new Path[NP];
    public double startPopulation[];
    public double candidate[];
    public Path test;
    public Graph graph;
    public double R; // radius
    public double maxPointy = 10;
    public double minPointy = -10;
    public static Point startPoint;
    public static Point endPoint;
    public int numR; // number of R in map
    Random random = new Random();

    public double AB;
    public LinkedList<Point> result = new LinkedList<Point>();

    public ES(int numR, Point start, Point end, Graph graph) {
        startPoint = start;
        endPoint = end;
        this.numR = numR;
        this.graph = graph;
        this.AB = Math.hypot(end.x - start.x, end.y - start.y);
        this.R = AB / (numR + 1);
    }

    public void initialize(int numR) {
        // for (int i = 0; i < NP; i++) {
        do {
            double pointy[] = new double[numR];
            Point points[] = new Point[numR];
            for (int j = 0; j < numR; j++) {
                do {
                    pointy[j] = random.nextDouble() * (maxPointy - minPointy) + minPointy;
                    points[j] = Path.convertPointToPoint(pointy[j], (j + 1) * R, startPoint, endPoint);
                } while (!points[j].inCoordinate());
            }
            test = new Path(numR, R, pointy, points);
            // particles[0] = new Path(numR, R, pointy, points);
            // particles[0].distance();
        } while (pathCollision(test) == true);

        // System.out.println(particles[i].distance);
        // }
    }

    public boolean pathCollision(Path path) {
        for (int i = 0; i < numR; i++) {
            if (i == 0) {
                if (graph.isIntersectLine(startPoint, path.points[i])) {
                    return true;
                }
                if (numR == 1) {
                    return graph.isIntersectLine(endPoint, path.points[i]);
                }
            } else if (i == numR - 1) {
                if (graph.isIntersectLine(endPoint, path.points[i])
                        || graph.isIntersectLine(path.points[i], path.points[i - 1])) {
                    return true;
                }
            } else if (i != 0) {
                if (graph.isIntersectLine(path.points[i], path.points[i - 1])) {
                    return true;
                }
            }
        }
        return false;
    }

    public static double[] add(double[] first, double[] second) {
        int length = first.length < second.length ? first.length : second.length;
        double[] result = new double[length];
        for (int i = 0; i < length; i++) {
            result[i] = first[i] + second[i];
        }
        return result;
    }

    public void run() {
        initialize(numR);
        for (int i = 0; i < 100; i++) {
            startPopulation = test.pointy;
            do {
                // candidate = startPopulation +
            } while (pathCollision(test) == true);
            // particles[i] =

        }
        for (int i = 0; i < test.pointy.length; i++) {
            System.out.print(test.pointy[i] + " ");
        }
        for (int i = 0; i < test.points.length; i++) {
            // System.out.print(test.pointy[i] + " ");
            test.points[i].printPoint();
        }
        result.add(startPoint);
        // for (int i = 0; i < particles.length; i++) {
        // if (pathCollision(particles[i]) == false) {
        // k = i;
        // break;
        // }
        // }
        for (int i = 0; i < numR; i++) {
            result.add(test.points[i]);

        }
        result.add(endPoint);
        result.removeLast();
        result.removeFirst();
    }
}
