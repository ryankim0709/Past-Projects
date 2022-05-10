package Classes.FOOP.Classwork;
import java.io.*;

public class isLeap {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            System.out.println("Enter a year to check if it is a leap year(-1 to quit) ");
            int year = Integer.parseInt(br.readLine());
            if (year == -1) {
                break;
            }
            System.out.println((((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) ? "Leap" : "Non-leap");
        }
    }
}
