package Classes.FOOP.Classwork.Star_Class;

public class Star {
    private int num;

    // Create a constructor with no input value
    // set the defualt value for num to be whatever you want
    public Star() {
        this.num = 2;

    }

    public Star(int num) {
        // set the private num = to the given num
        this.num = num;
    }

    /*
     * done in week 18
     * ex. num = 5
     *****
     */
    public void printStars() {
        System.out.println("Printing printStars:");
        for (int i = 0; i < this.num; i++) {
            System.out.print("*");
        }
        System.out.println();
    }

    /*
     * done in week 18
     * ex. num = 5
     *
     **
     ***
     ****
     *****
     */
    public void printRowsOfStars() {
        System.out.println("Printing printRowsOfStars:");
        for (int i = 1; i <= this.num; i++) {
            for (int j = 0; j < 1; j++) {
                System.out.print("*".repeat(i));
            }
            System.out.println();
        }
    }

    /*
     * done in week 18
     * ex. num = 2
     **
     **
     ******
     ******
     **
     **
     */
    public void cross() {
        System.out.println("Printing Cross:");
        int length = this.num;
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

    /*
     * new
     * ex. num = 4
     *
     ***
     *****
     *******
     *****
     ***
     * 
     */
    public void printSolidDiamond() {
        System.out.println("Printing printSolidDiamond:");
        // Create a solid diamond = notice how many spaces we start with befor you print
        // out a star
        int maxlen = 1 + 2 * (num - 1);
        int line = -1;
        for (int i = 0; i < this.num - 1; i++) {
            line += 2;
            System.out.println(" ".repeat((maxlen - line) / 2) + "*".repeat(line) + " ".repeat((maxlen - line) / 2));
        }
        line += 2;
        System.out.println("*".repeat(line));
        for (int i = this.num - 1; i > 0; i--) {
            line -= 2;
            System.out.println(" ".repeat((maxlen - line) / 2) + "*".repeat(line) + " ".repeat((maxlen - line) / 2));
        }
    }
}
