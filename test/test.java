import java.util.Random;

public class test {
    public int numR; // number of R in map

    public static double[] add(double[] first, double[] second) {
        int length = first.length < second.length ? first.length : second.length;
        double[] result = new double[length];
        for (int i = 0; i < length; i++) {
            result[i] = first[i] + second[i];
        }
        return result;
    }

    public static void main(String[] args) {
        // Random random = new Random();
        double[] x = { 1, 2 };
        double[] y = { 4, 5 };
        double[] z;
        z = add(x, y);
        // double x = random.nextDouble();
        for (int i = 0; i < z.length; i++) {
            System.out.print(z[i] + " ");
        }
        // System.out.println(x);
        // System.out.println("OK");
    }
}
