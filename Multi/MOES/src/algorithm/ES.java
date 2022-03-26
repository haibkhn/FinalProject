package algorithm;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Random;
import org.apache.commons.math3.distribution.MultivariateNormalDistribution;
import util.Graph;
import util.Path;
import util.Point;

public class ES {

    public final int NP = 100; // population size
    public final int elite = 5;
    public Path particles[] = new Path[NP];
    public double startPopulation[];
    public double candidate[];
    public Path initialCandidate;
    public Graph graph;
    public double R; // radius
    public double maxPointy = 10;
    public double minPointy = -10;
    public double maxVariance = 5;
    public double minVariance = -5;
    public double mean[];
    public static Point startPoint;
    public static Point endPoint;
    public int numR; // number of R in map
    Random random = new Random();
    public double identityMatrix[][];
    public double[] variance;

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
        variance = new double[numR];
        mean = new double[numR];

        do {
            double pointy[] = new double[numR];
            Point points[] = new Point[numR];
            for (int j = 0; j < numR; j++) {
                variance[j] = random.nextDouble() * (maxVariance - minVariance) + minVariance;
                do {
                    pointy[j] = random.nextDouble() * (maxPointy - minPointy) + minPointy;
                    points[j] = Path.convertPointToPoint(pointy[j], (j + 1) * R, startPoint, endPoint);
                } while (!points[j].inCoordinate());
            }
            initialCandidate = new Path(numR, R, pointy, points);

        } while (pathCollision(initialCandidate) == true);
        identityMatrix = new double[numR][numR];
        for (int i = 0; i < numR; i++) {
            identityMatrix[i][i] = 1;
        }
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

    public static double[] multiple(double[] first, double[] second) {
        int length = first.length < second.length ? first.length : second.length;
        double[] result = new double[length];
        for (int i = 0; i < length; i++) {
            result[i] = first[i] * second[i];
        }
        return result;
    }

    public void bubbleSort(Path arr[]) {
        int n = 20;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j].distance > arr[j + 1].distance) {
                    // swap arr[j+1] and arr[j]
                    Path temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }

    public void updateMean() {

    }

    public void run() {
        initialize(numR);

        MultivariateNormalDistribution mnd = new MultivariateNormalDistribution(mean, identityMatrix);
        startPopulation = initialCandidate.pointy;

        // Run NP generation
        for (int iter = 0; iter < NP; iter++) {
            // Generate 20 children in 1 generation, only generate child that doesnt collide
            // ArrayList<Path> particlesArrayList = new ArrayList<>();
            for (int i = 0; i < 20; i++) {
                do {
                    double pointy[] = new double[numR];
                    Point points[] = new Point[numR];
                    pointy = add(startPopulation, multiple(variance, mnd.sample()));
                    for (int j = 0; j < numR; j++) {
                        points[j] = Path.convertPointToPoint(pointy[j], (j + 1) * R, startPoint, endPoint);
                    }
                    particles[i] = new Path(numR, R, pointy, points);
                    particles[i].distance();
                } while (pathCollision(particles[i]) == true);
                // particlesArrayList.add(particles[i]);
            }
            bubbleSort(particles);

            // Calculate new mean
            startPopulation = new double[numR];
            for (int i = 0; i < elite; i++) {
                startPopulation = add(startPopulation, particles[i].pointy);
            }
            for (int i = 0; i < numR; i++) {
                startPopulation[i] = startPopulation[i] / elite;
            }

            // Calculate new standard deviation
            for (int i = 0; i < elite; i++) {

            }
        }

        // System.out.println(particles.length);
        // for (int i = 0; i < 20; i++) {
        // System.out.println(particlesArrayList.get(i).distance);
        // }

        for (int i = 0; i < 20; i++) {
            System.out.println(particles[i].distance);
        }

        result.add(startPoint);
        for (int i = 0; i < numR; i++) {
            result.add(initialCandidate.points[i]);
        }
        result.add(endPoint);
        result.removeLast();
        result.removeFirst();
    }
}
