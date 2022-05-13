package Classes.FOOP.Classwork;

public class may12 {
    public static void main(String[] args) {
        System.out.println(printChars('R', 10));
        System.out.println(printStarts(10));
        System.out.println(numLeapYears(2000, 2020));
        System.out.println(printRowOfStarts(10));
    }

    public static String printChars(char character, int times) {
        return String.valueOf(character).repeat(times);
    }

    public static String printStarts(int times) {
        return "*".repeat(times);
    }

    public static int numLeapYears(int year1, int year2) {
        int count = 0;
        for (int i = year1; i <= year2; i++) {
            count += (((i % 4 == 0) && (i % 100 != 0)) || (i % 400 == 0)) ? 1 : 0;
        }
        return count;
    }

    public static String printRowOfStarts(int rows) {
        String pyramid = "";
        for (int i = 1; i <= rows; i++) {
            pyramid += "*".repeat(i) + "\n";
        }
        return pyramid;
    }
}
