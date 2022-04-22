package Java_ATM;

import java.util.*;
import java.io.*;

public class Main_Accountant {
    // Users
    static HashMap<Integer, Account> users = new HashMap<>();
    // More efficient than scanner
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        setup(); // Add some users for testing
        boolean quit = false;
        while (!quit) {
            displayWelcome(); // Display the welcome message
            int option = Integer.parseInt(br.readLine());

            if (option == 1) // Create account
                makeAccount();
            else if (option == 2) // Withdraw money
                withdraw();
            else if (option == 3) // Deposit money
                deposit();
            else if (option == 4) // Apply for a loan
                applyLoan();
            else if (option == 5) // View someone's account
                viewAcc();
            else if(option == 6) // Delete an account
                deleteAccount();
            else if (option == 7) { // Display the statistics for all users
                System.out.println("List of customers");
                for (Account i : users.values()) {
                    System.out.println("Name: " + i.getFullName() + " Balance: " + i.getBalance() + " APR: "
                            + i.getApr() + " Loans: " + i.getLonas() + " ID: " + i.getId());
                }
            }
            else if (option == 8) { // Quit with inspiring message
                quit = true;
                System.out.println("Good work today! Let's work harder tomorrow!");
            } else
                System.out.println("Sorry! That is not a valid option");
            System.out.println("--------------------------------------------------------------"); // Default deliminator for readablity
        }
    }

    public static void displayWelcome() {
        // Welcome message broke into two for readability purposes
        String message = "Welcome employee! What does our customer want help with today!?\n";
        String options = "1.Create new account\n2.Withdraw\n3.Deposit\n4.Apply for loan\n5.View Account\n6.Delete Account\n7.Display Users\n8.Quit";
        System.out.println(message + options);
    }

    public static void setup() {
        // Create 5 random users for testing
        Random rd = new Random();
        int id;
        id = Math.abs(rd.nextInt());
        users.put(id, new Account("Bob", id, 200, 19));
        id = Math.abs(rd.nextInt());
        users.put(id, new Account("Joe", id, 300, 19));
        id = Math.abs(rd.nextInt());
        users.put(id, new Account("Billy", id, 20298, 19));
        id = Math.abs(rd.nextInt());
        users.put(id, new Account("James", id, 120, 19));
        id = Math.abs(rd.nextInt());
        users.put(id, new Account("Jacob", id, 300, 19));
    }

    public static void makeAccount() throws IOException {
        // Creating an account 
        System.out.println("Let's help them create an account!");
        System.out.println("What is their name?");
        String name = br.readLine();
        System.out.println("How much will you deposit? (No $ sign)");
        String am = br.readLine();
        if (am == null || am.length() == 0) { // Default money if the accountant didn't input anything
            System.out.println(
                    "Defaulting to $5000. If they don't have this much remember to remove this account and create a new one");
            am = "5000";
        }
        long amount = Long.parseLong(am);
        System.out.println("What is their APR(annual percent rate)?");
        String aprString = br.readLine();
        if (aprString == null || aprString.length() == 0) { // Default APR if the accountant didn't input anything
            System.out.println("Defaulting to 19%");
            aprString = "19";
        }
        double apr = Double.parseDouble(aprString);
        Random rd = new Random();
        int id = Math.abs(rd.nextInt());
        users.put(id, new Account(name, id, amount, apr)); // Add account
        System.out.println("They are registered! Their id is " + id);
    }

    public static void withdraw() throws IOException {
        // Withdrawing
        int id = checkUser(); // Check the user via pin
        if (id == -1)
            return;
        Account user = users.get(id);
        System.out.println("The customers name is " + user.getFullName() + "! Their current balance is " + user.getBalance()
                + ". How much would they like to withdraw?");
        long amount = Long.parseLong(br.readLine()); // Ask for how much money they would like to withdraw

        if (amount > user.getBalance()) { // Check against balance 
            System.out.println("Sorry! They don't have enough money... Their current balance is " + user.getBalance());
            return;
        }
        System.out.println("The transaction was complete! Their new balance is now " + (user.getBalance() - amount));
        user.withdraw(amount); // Withdraw money after transaction
    }

    public static void deposit() throws IOException {
        int id = checkUser(); // Check the user via pin
        if (id == -1)
            return;
        Account user = users.get(id);
        System.out.println("The customers name is " + user.getFullName() + "! Their current balance is " + user.getBalance()
                + ". How much would you they like to deposit?");
        long amount = Long.parseLong(br.readLine()); // Ask how much they would like to deposit
        System.out.println("The transaction was complete! Their new balance is now " + (user.getBalance() + amount));
        user.deposit(amount); // Deposit the amount
    }

    public static void applyLoan() throws IOException {
        int id = checkUser(); // Check the user via id
        if (id == -1)
            return;

        System.out.println("How much money would they like to loan? ");
        long amount = Long.parseLong(br.readLine()); // Ask for amount they would like to loan
        System.out.println("How many days old is the loan?");
        int time = Integer.parseInt(br.readLine()); // Ask for how long the loan has been
        double rate = (Math.random() * (7 - 3)) + 3; // Generate random rate between 7 and 3
        rate = Math.round(rate * 100.0) / 100.0; // Round rate to 2 decimal places
        System.out.println("Their annual rate will be " + rate + "%");
        Account user = users.get(id);
        // Add loan to the user's profile
        ArrayList<Loan> loans = user.getLonas();
        loans.add(new Loan(amount, time, rate));
        user.setLonas(loans);
    }

    public static void viewAcc() throws IOException {
        int id = checkUser(); // Check user via pin
        if (id == -1)
            return;

        Account user = users.get(id);
        System.out.println("The customers name is " + user.getFullName());
        while (true) {
            System.out.println("What would you they to see?\n1.Account name\n2.Balance\n3.APR\n4.Loans\n5.Quit"); // Ask what they would like to view
            int choice = Integer.parseInt(br.readLine());
            if (choice == 1)
                System.out.println("Their account name is " + user.getFullName());
            else if (choice == 2)
                System.out.println("Their account balance is " + user.getBalance());
            else if (choice == 3)
                System.out.println("Their account APR(annual percentage rate) is " + user.getApr());
            else if (choice == 4) {
                if (user.getLonas().size() == 0) {
                    System.out.println("They have no loans!");
                } else {
                    int counter = 1;
                    System.out.println("Here is a list of their loans");
                    for (Loan i : user.getLonas()) {
                        System.out.println(counter + " " + i.getAmount() + " at " + i.getRate() + "% / year. It has been "
                                + i.getTimeInDays() + " days. Total owe: "
                                + (Math.round((i.getAmount() + (i.getTimeInDays() / 365) * i.getRate()) * 100.0)
                                        / 100.0));
                        counter++;
                    }
                }
            } else if (choice == 5) {
                return;
            } else {
                System.out.println("Sorry! That is not a valid option!");
            }
        }
    }

    public static void deleteAccount() throws IOException {
        // Deleting a user via pin. If valid, then remove from the dynamic array of users
        System.out.println("Which account would you like to delete(enter their pin) ");
        int id = Integer.parseInt(br.readLine());

        if (users.keySet().contains(id) == false) {
            System.out.println("Sorry! This user is not available, please try again!");
            return;
        }
        users.remove(id);
        System.out.println("Their profile has been removed!");
    }

    public static int checkUser() throws IOException {
        // Check if pin is in the dynamic array and display message accordingly
        System.out.println("What is their bank account ID?");
        int id = Integer.parseInt(br.readLine());

        if (users.keySet().contains(id) == false) {
            System.out.println("Their ID is not registered in the system!");
            return -1;
        }
        return id;
    }
}