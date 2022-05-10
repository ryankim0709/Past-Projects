package Classes.FOOP.Classwork.Valid_Date_Checker;

public class DateChecker {
    int month, day, year;

    public DateChecker(String date) {
        String[] info = date.split("/");
        month = Integer.parseInt(info[0]);
        day = Integer.parseInt(info[1]);
        year = Integer.parseInt(info[2]);
    }
    
    public void checkDate() {
        int[] days = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        boolean leap = (((this.year % 4 == 0) && (this.year % 100 != 0)) || (this.year % 400 == 0)) ? true : false;
        if (leap) {
            days[2] += 1;
        }

        if (month < 1 || month > 12) {
            System.out.println("That is not a valid month");
            return;
        }
        if (day < 1 || day > days[month]) {
            System.out.println("That is not a valid day");
            return;
        }
        System.out.println("That is a valid day!");
    }
}
