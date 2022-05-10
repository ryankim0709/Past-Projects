package Classes.FOOP.Classwork.Week_Day;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            System.out.println("Enter a number from 1 - 7 for the day and 8 for quit");
            int option = Integer.parseInt(br.readLine());

            if (option == 8) {
                System.out.println("Thank you for visiting");
                break;
            } else if (option > 8 || option < 1) {
                System.out.println("Sorry, that is not a valid option");
            } else {
                Day day = new Day(option);
                System.out.println(day.toString());
            }
        }
    }
}