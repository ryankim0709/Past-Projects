package Classwork.FOOP.Temp_Converter;

public class Converter {
    private double temp;
    private char unit;

    public Converter(double temp, char unit) {
        this.temp = temp;
        this.unit = unit;
    }

    public String toF() {
        if (unit == 'F') {
            return "Already in F";
        }
        this.unit = 'C';
        return Double.toString(temp) + "F is " + Double.toString(temp * 1.8 + 32.0) + "C";
    }

    public String toC() {
        if (unit == 'C') {
            return "Already in C";
        }
        this.unit = 'F';
        return Double.toString(temp) + "C is " + Double.toString((temp - 32.0) / 1.8) + "C";
    }
    
    public String convert() {
        if (this.unit == 'C') {
            return toF();
        }
        return toC();
    }
}
