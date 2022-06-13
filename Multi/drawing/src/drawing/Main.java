package drawing;

import java.awt.Color;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

import algorithm.ES;
// import algorithm.PSO;
// import algorithm.PSOES;
import gui.GUIRobotics;
import util.Graph;
import util.Path;
import util.Point;

public class Main {
    public static void main(String[] args) throws IOException {

        String numberTeString = "16";
        // Tao moi truong
        GUIRobotics gui = new GUIRobotics(600, 100, 10);
        gui.generateEnvironment("input/obstacle_" + numberTeString + ".txt", 0.8, false);

        // Doc du lieu dau vao
        LinkedList<Point> pointsToVisit = readPointData("input/input_" + numberTeString + ".txt");

        ArrayList<Point> pointsToDraw = readPointDataDrawing("testing/moes_test_point_" + numberTeString + ".txt");

        ArrayList<Point> resultMOES = new ArrayList<Point>();
        ArrayList<Point> resultSafety = new ArrayList<Point>();
        ArrayList<Point> resultSmooth = new ArrayList<Point>();

        // ArrayList<Point> resultPareto = new ArrayList<Point>();

        try {
            // es.run();
            resultMOES.add(pointsToVisit.get(0));
            for (int j = 0; j < pointsToDraw.size(); j++) {
                resultMOES.add(pointsToDraw.get(j));
            }
            resultMOES.add(pointsToVisit.get(1));
            gui.canvas.drawLines(resultMOES, pointsToVisit, Color.GREEN);

            // resultSafety.add(pointsToVisit.get(0));
            // for (int j = 0; j < es.resultSafety.size(); j++) {
            // resultSafety.add(es.resultSafety.get(j));
            // }
            // resultSafety.add(pointsToVisit.get(1));
            // gui.canvas.drawLines(resultSafety, pointsToVisit, Color.RED);

            // resultSmooth.add(pointsToVisit.get(0));
            // for (int j = 0; j < es.resultSmooth.size(); j++) {
            // resultSmooth.add(es.resultSmooth.get(j));
            // }
            // resultSmooth.add(pointsToVisit.get(1));
            // gui.canvas.drawLines(resultSmooth, pointsToVisit, Color.BLACK);

            // for (int i = 0; i < es.resultPareto.size(); i++) {
            // ArrayList<Point> resultPareto = new ArrayList<Point>();

            // resultPareto.add(pointsToVisit.get(0));
            // for (int j = 0; j < es.resultPareto.get(i).size(); j++) {
            // resultPareto.add(es.resultPareto.get(i).get(j));
            // }
            // resultPareto.add(pointsToVisit.get(1));
            // gui.canvas.drawLines(resultPareto, pointsToVisit, Color.ORANGE);
            // }
        }

        catch (Exception e) {
            System.out.println("Something went wrong!");
            e.printStackTrace();
        }
    }

    public static LinkedList<Point> readPointData(String filename) throws FileNotFoundException {
        Scanner scan = new Scanner(new File(filename));
        LinkedList<Point> pointsToVisit = new LinkedList<Point>();
        double x = scan.nextDouble();
        while (x != -1) {
            double y = scan.nextDouble();
            pointsToVisit.addLast(new Point(x, y));
            x = scan.nextDouble();
        }
        scan.close();

        return pointsToVisit;
    }

    public static ArrayList<Point> readPointDataDrawing(String filename) throws FileNotFoundException {
        Scanner scan = new Scanner(new File(filename));
        ArrayList<Point> pointsToVisit = new ArrayList<Point>();
        double x = scan.nextDouble();
        while (x != -1) {
            double y = scan.nextDouble();
            pointsToVisit.add(new Point(x, y));
            x = scan.nextDouble();
        }
        scan.close();

        return pointsToVisit;
    }
}
