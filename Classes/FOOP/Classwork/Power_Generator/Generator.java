package Classes.FOOP.Classwork.Power_Generator;
import java.lang.Math;

public class Generator {
    private double num;
    private int raised;

    public Generator(double num) {
        this.num = num;
        this.raised = -1;
    }

    public double next() {
        raised++;
        return Math.pow(num, raised);
    }
}
