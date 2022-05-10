package Classes.FOOP.Classwork.Temp_Converter;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Enter the temperature you want to convert");
        double temp = Double.parseDouble(br.readLine());
        System.out.println("What is the unit (F or C)");
        char unit = br.readLine().charAt(0);

        Converter convert = new Converter(temp, unit);

        while (true) {
            System.out.println("Do you want to\n1. Convert to F\nConvert to C\nConvert to other unit");
            int option = Integer.parseInt(br.readLine());

            if (option == 1) {
                System.out.println(convert.toF());
            } else if (option == 2) {
                System.out.println(convert.toC());
            } else if (option == 3) {
                System.out.println(convert.convert());
            } else {
                System.out.println("Thank you for visiting");
                break;
            }
        }
    }
}
