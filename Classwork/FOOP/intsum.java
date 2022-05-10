package Classwork.FOOP;

import java.io.*;

public class intsum {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ans = br.readLine();
        while (ans.length() > 1) {
            ans = sumString(ans);
        }
        System.out.println(ans);
    }

    public static String sumString(String number) {
        int sum = 0;
        for (int i = 0; i < number.length(); i++) {
            sum += Character.getNumericValue(number.charAt(i));
        }
        return Integer.toString(sum);
    }
}
