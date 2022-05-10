package Classes.FOOP.Classwork;

import java.io.*;

public class generateCross {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("How wid should your cross be?");
        int length = Integer.parseInt(br.readLine());

        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < length; j++) {
                System.out.print("#");
            }
            for (int j = 0; j < length; j++) {
                System.out.print(" ");
            }
            System.out.println();
        }
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < 3 * length; j++) {
                System.out.print("#");
            }

            System.out.println();
        }
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < length; j++) {
                System.out.print("#");
            }
            for (int j = 0; j < length; j++) {
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
