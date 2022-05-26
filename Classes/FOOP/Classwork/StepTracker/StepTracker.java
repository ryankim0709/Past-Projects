package Classes.FOOP.Classwork.StepTracker;

import java.util.*;

public class StepTracker {
    private ArrayList<Integer> steps = new ArrayList<>();
    private int minSteps = 0;

    public StepTracker(int minSteps) {
        this.minSteps = minSteps;
    }

    public void addDailySteps(int steps) {
        this.steps.add(steps);
    }

    public int activeDays() {
        int total = 0;
        for (int i : steps) {
            if (i >= this.minSteps)
                total++;
        }
        return total;
    }

    public double averageSteps() {
        double total = 0;
        for (int i : steps)
            total += i;
        return total / (double) steps.size();
    }
}