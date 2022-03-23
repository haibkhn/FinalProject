package algorithm;

import java.util.LinkedList;
import java.util.Random;

import util.Graph;
import util.Path;
import util.Point;

public class ES {
    public final int NP = 100; // population size
    public Path particles[] = new Path[NP];

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
        this.R = AB / numR;
    }

    public void initialize(int numR) {
        for (int i = 0; i < NP; i++) {
            double pointy[] = new double[numR];
            Point points[] = new Point[numR];
            for (int j = 0; j < numR; j++) {
                do {
                    pointy[j] = random.nextDouble() * (maxPointy - minPointy) + minPointy;
                    points[j] = Path.convertPointToPoint(pointy[j], (j + 1) * R, startPoint, endPoint);
                } while (!points[j].inCoordinate());
            }
            particles[i] = new Path(numR, R, pointy, points);
            particles[i].distance();
            // System.out.println(particles[i].distance);
        }
    }

    public void run() {
        initialize(numR);
        result.add(startPoint);
        for (int i = 0; i < numR; i++) {
            result.add(particles[1].points[i]);

        }
        result.add(endPoint);
        result.removeLast();
        result.removeFirst();
    }
}
