package Java_ATM;
import java.util.*;

public class Account {
	// Set-up variables
    private String fullName;
    private int id;
    private Double balance;
    private double apr;
    private ArrayList<Loan> lonas;

	// Average apr = 19
	
	// Constructor 1 with balance as long
	public Account(String name, int id, long balance, double apr) {
		this.fullName = name;
		this.id = id;
		this.balance = (double) balance;
		this.apr = apr;
		this.lonas = new ArrayList<>();
	}
	
	// Constructor 2 with balance as double
	public Account(String name, int id, Double balance, double apr) {
		this.fullName = name;
		this.id = id;
		this.balance = balance;
		this.apr = apr;
		this.lonas = new ArrayList<>();
	}

	// Constructor 3 with balance as integer
	public Account(String name, int id, int balance, double apr) {
		this.fullName = name;
		this.id = id;
		this.balance = (double) balance;
		this.apr = apr;
		this.lonas = new ArrayList<>();
	}

	// Taking money out of account
	public void withdraw(long amount) {
		this.balance = this.balance - amount;
	}
	
	// Adding money to account
    public void deposit(long amount) {
        this.balance = this.balance + amount;
    }

	// Getters and Setters
	public String getFullName() {
		return this.fullName;
	}

	public void setFullName(String fullName) {
		this.fullName = fullName;
	}

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public double getBalance() {
		return this.balance;
	}

	public void setBalance(long balance) {
		this.balance = (double) balance;
	}

	public void setbalance(int balance) {
		this.balance = (double) balance;
	}

	public void setBalance(double balance) {
		this.balance = balance;
	}

	public double getApr() {
		return this.apr;
	}

	public void setApr(double apr) {
		this.apr = apr;
	}

	public ArrayList<Loan> getLonas() {
		return this.lonas;
	}

	public void setLonas(ArrayList<Loan> lonas) {
		this.lonas = lonas;
	}
}
