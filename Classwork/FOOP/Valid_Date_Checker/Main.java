package Classwork.FOOP.Valid_Date_Checker;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            System.out.print("Enter a date in mm/dd/yyyy format (empty to quit): ");
            String date = br.readLine();
            if (date == "") {
                break;
            }
            DateChecker checker = new DateChecker(date);
            checker.checkDate();
        }
    }
}
