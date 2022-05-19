package Classes.FOOP.Classwork.Star_Class;

import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        // create a new star object with a starting value of 5
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("How many lines for your star?");
        Star star1 = new Star(Integer.parseInt(br.readLine()));
        // create a new star object wth a default starting value
        Star star2 = new Star();
        // method calls for star1
        star1.printStars();
        star1.printRowsOfStars();
        star1.cross();
        star1.printSolidDiamond();
        // create method calls for star2
        star2.printStars();
        star2.printRowsOfStars();
        star2.cross();
        star2.printSolidDiamond();
    }
}