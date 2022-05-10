package Classes.FOOP.Classwork.Week_Day;

public class Day {
    int day;

    public Day(int day) {
        this.day = day;
    }
    
    public String toString() {
        String[] days = { "Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday", "Sunday" };
        return days[this.day - 1];
    }
}
