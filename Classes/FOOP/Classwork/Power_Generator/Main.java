package Classes.FOOP.Classwork.Power_Generator;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("What number would you like to raise");
        double num = Double.parseDouble(br.readLine());

        Generator generator = new Generator(num);
        for (int i = 0; i < 10; i++) {
            System.out.println(generator.next());
        }
    }
}
