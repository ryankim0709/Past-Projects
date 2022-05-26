package Classes.FOOP.Classwork;

import java.io.*;

public class self_divisor {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter a number to check if it a self divisor ");
        System.out.println(isSelfDivisor(br.readLine()));

    }

    public static boolean isSelfDivisor(String num) {
        for (int i = 0; i < num.length(); i++) {
            if (Integer.parseInt(num) % Character.getNumericValue(num.charAt(i)) != 0) {
                return false;
            }
        }
        return true;
    }
}