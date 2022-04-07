package algorithm;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Random;
import org.apache.commons.math3.distribution.MultivariateNormalDistribution;
import util.Graph;
import util.Path;
import util.Point;

public class ES {

    public final int NP = 500; // population size
    public int elite = 20;
    public final int children = 100;
    public Path particles[] = new Path[children];
    public Path gBest;
    public double startPopulation[];
    public double candidate[];
    public int rank;
    public Path initialCandidate;
    public Graph graph;
    public double R; // radius
    public double maxPointy = 10;
    public double minPointy = -10;
    public double maxVariance = 6;
    public double minVariance = -6;
    public double mean[];
    public static Point startPoint;
    public static Point endPoint;
    public int numR; // number of R in map
    Random random = new Random();
    public double identityMatrix[][];
    public double[] standardDevi;

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
        standardDevi = new double[numR];
        mean = new double[numR];

        do {
            double pointy[] = new double[numR];
            Point points[] = new Point[numR];
            for (int j = 0; j < numR; j++) {
                standardDevi[j] = random.nextDouble() * (maxVariance - minVariance) + minVariance;
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
        gBest = initialCandidate;
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

    public static double[] minusSquare(double[] first, double[] second) {
        int length = first.length < second.length ? first.length : second.length;
        double[] result = new double[length];
        for (int i = 0; i < length; i++) {
            result[i] = (first[i] - second[i]) * (first[i] - second[i]);
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

    public void bubbleSort(Path arr[], int n) {
        // int n = children;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j].distance > arr[j + 1].distance) {
                    // swap arr[j+1] and arr[j]
                    Path temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }

    public boolean checkDominate(Path particle1, Path particle2) {
        if ((particle1.distance <= particle2.distance
                && particle1.pathSafety(graph) <= particle2.pathSafety(graph)
                && particle1.pathSmooth() <= particle2.pathSmooth())
                && (particle1.distance < particle2.distance
                        && particle1.pathSafety(graph) < particle2.pathSafety(graph)
                        && particle1.pathSmooth() < particle2.pathSmooth())) {
            return true;
        } else
            return false;
    }

    public boolean checkRank(Path[] particle) {
        for (int i = 0; i < particle.length; i++) {
            if (particle[i].rank == -1)
                return false;
        }
        return true;
    }

    public void run() {
        initialize(numR);

        MultivariateNormalDistribution mnd = new MultivariateNormalDistribution(mean, identityMatrix);
        startPopulation = initialCandidate.pointy;

        // Run NP generation
        for (int iter = 0; iter < NP; iter++) {
            // Generate n children in 1 generation, only generate child that doesnt collide
            // ArrayList<Path> particlesArrayList = new ArrayList<>();
            for (int i = 0; i < children; i++) {
                do {
                    double pointy[] = new double[numR];
                    Point points[] = new Point[numR];
                    pointy = add(startPopulation, multiple(standardDevi, mnd.sample()));
                    for (int j = 0; j < numR; j++) {
                        points[j] = Path.convertPointToPoint(pointy[j], (j + 1) * R, startPoint, endPoint);
                    }
                    particles[i] = new Path(numR, R, pointy, points);
                    particles[i].distance();
                } while (pathCollision(particles[i]) == true);
                // particlesArrayList.add(particles[i]);
            }

            // Begin multi-objective
            ArrayList<Integer> chosenParticleIndex = new ArrayList<Integer>();
            rank = 0;

            while (checkRank(particles) == false) {
                ArrayList<Path> chosenArrayList = new ArrayList<Path>();
                int i1 = 0;
                //
                while (i1 < particles.length) {
                    if (chosenParticleIndex.contains(i1)) {
                        i1++;
                        // System.out.println("contain");
                    } else {
                        // System.out.println("not contain");
                        int i2 = 0;
                        boolean cont = true;
                        while (i2 < particles.length && cont == true) {
                            if (i2 == (particles.length) - 1) {
                                // chosenArrayList.add(particles[i1]);
                                chosenParticleIndex.add(i1);
                                particles[i1].rank = rank;
                            }
                            if (chosenParticleIndex.contains(i2)) {
                                i2++;
                            } else {
                                if (checkDominate(particles[i2], particles[i1])) {
                                    cont = false;
                                }
                                i2++;
                            }
                        }
                        i1++;
                    }
                }
                rank++;

                System.out.println("rank " + rank);
                System.out.println("num " + chosenParticleIndex.size());
                for (int i = 0; i < chosenParticleIndex.size(); i++) {
                    System.out.print(chosenParticleIndex.get(i) + " ");
                }
                System.out.println();
            }
            // End multiobjective

            // System.out.println("num of chosen path: " + chosenArrayList.size());
            // for (int i = 0; i < 3; i++) {
            // System.out
            // .println(chosenArrayList.get(i).distance + " " +
            // chosenArrayList.get(i).pathSafety(graph) + " "
            // + chosenArrayList.get(i).pathSmooth());
            // }

            // Thu sua multiobjective
            // elite = chosenParticleIndex.size();

            // Path particlesTMP[] = new Path[elite];
            // for (int i = 0; i < elite; i++) {
            // particlesTMP[i] = particles[chosenParticleIndex.get(i)];
            // }
            // bubbleSort(particlesTMP, elite);

            // // Calculate new standard deviation
            // standardDevi = new double[numR];
            // for (int i = 0; i < elite; i++) {
            // standardDevi = add(standardDevi, minusSquare(particles[i].pointy,
            // startPopulation));
            // }
            // for (int i = 0; i < numR; i++) {
            // standardDevi[i] = standardDevi[i] / elite;
            // standardDevi[i] = Math.sqrt(standardDevi[i]);
            // }

            // // Calculate new mean
            // startPopulation = new double[numR];
            // for (int i = 0; i < elite; i++) {
            // startPopulation = add(startPopulation, particles[i].pointy);
            // }
            // for (int i = 0; i < numR; i++) {
            // startPopulation[i] = startPopulation[i] / elite;
            // }
            // if (particles[0].distance < gBest.distance) {
            // System.out.println("Iter: " + iter + " Best distance: " +
            // particles[0].distance);
            // gBest = particles[0];
            // }

            // // Ket thuc

            bubbleSort(particles, children);

            // Calculate new standard deviation
            standardDevi = new double[numR];
            for (int i = 0; i < elite; i++) {
                standardDevi = add(standardDevi, minusSquare(particles[i].pointy,
                        startPopulation));
            }
            for (int i = 0; i < numR; i++) {
                standardDevi[i] = standardDevi[i] / elite;
                standardDevi[i] = Math.sqrt(standardDevi[i]);
            }

            // Calculate new mean
            startPopulation = new double[numR];
            for (int i = 0; i < elite; i++) {
                startPopulation = add(startPopulation, particles[i].pointy);
            }
            for (int i = 0; i < numR; i++) {
                startPopulation[i] = startPopulation[i] / elite;
            }
            if (particles[0].distance < gBest.distance) {
                System.out.println("Iter: " + iter + " Best distance: " +
                        particles[0].distance);
                gBest = particles[0];
            }
        }

        result.add(startPoint);
        for (int i = 0; i < numR; i++) {
            result.add(gBest.points[i]);
        }
        result.add(endPoint);
        result.removeLast();
        result.removeFirst();
    }
}
