public class Main {
    public static void main(String[] args) {
        StepTracker tr = new StepTracker(10000);
        System.out.println(tr.activeDays());
        System.out.println(tr.averageSteps());
        tr.addDailySteps(9000);
        tr.addDailySteps(1111);
        tr.addDailySteps(12000);
        System.out.println(tr.activeDays());
        System.out.println(tr.averageSteps());
        
    }
}
