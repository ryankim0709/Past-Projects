package Java_ATM;

public class Loan {
    // Setting up variables
    private double amount;
    private int timeInDays;
    private double rate;

    // Basic constructor
    public Loan(double amount, int timeInDays, double rate) {
        this.amount = amount;
        this.timeInDays = timeInDays;
        this.rate = rate;
    }

    // Object as a string form. Overriding the default toString function
    public String toString() {
        return this.amount + " @ " + this.rate + "% / year. Total: "+(Math.round((this.getAmount() + (this.getTimeInDays() / 365) * this.getRate()) * 100.0)/100.0);
    }

    // Getters and Setters
    public double getAmount() {
        return this.amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public int getTimeInDays() {
        return this.timeInDays;
    }

    public void setTimeInDays(int timeInDays) {
        this.timeInDays = timeInDays;
    }

    public double getRate() {
        return this.rate;
    }

    public void setRate(double rate) {
        this.rate = rate;
    }
}
