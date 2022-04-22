package Java_ATM;

import java.util.*;
import java.io.*;

public class Main_Cust {
    static HashMap<Integer, Account> users = new HashMap<>();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        boolean quit = false;
        while (!quit) {
            displayWelcome();
            int option = Integer.parseInt(br.readLine());

            if (option == 1)
                makeAccount();
            else if (option == 2)
                withdraw();
            else if (option == 3)
                deposit();
            else if (option == 4)
                applyLoan();
            else if (option == 5)
                viewAcc();
            else if (option == 6) {
                quit = true;
                System.out.println("Thank you for visiting Happy Banks! Come back next time!");
            } else
                System.out.println("Sorry! That is not a valid option");
            System.out.println("--------------------------------------------------------------");
        }
    }

    public static void displayWelcome() {
        String message = "Welcome to Happy Bank! We are glad you have chosen our bank! What would you like to do?\n";
        String options = "1.Create new account\n2.Withdraw\n3.Deposit\n4.Apply for loan\n5.View Account\n6.Quit";
        System.out.println(message + options);
    }

    public static void makeAccount() throws IOException {
        System.out.println("We are happy that you have decided to create an account!");
        System.out.println("What is your name?");
        String name = br.readLine();
        System.out.println("How much will you deposit? (No $ sign)");
        String am = br.readLine();
        if (am == null || am.length() == 0) {
            System.out.println("A default amount is needed! Please try again!");
            return;
        }
        long amount = Long.parseLong(am);
        System.out.println("What is you APR(annual percent rate)?");
        String aprString = br.readLine();
        if (aprString == null || aprString.length() == 0) {
            System.out.println("The default APR of 19% will be used");
            aprString = "19";
        }
        double apr = Double.parseDouble(aprString);
        Random rd = new Random();
        int id = Math.abs(rd.nextInt());
        users.put(id, new Account(name, id, amount, apr));
        System.out.println("You are registered! Your bank account id is " + id);
    }

    public static void withdraw() throws IOException {
        int id = checkUser();
        if (id == -1)
            return;
        Account user = users.get(id);
        System.out.println("Welcome " + user.getFullName() + "! Your current balance is " + user.getBalance()
                + ". How much would you like to withdraw?");
        long amount = Long.parseLong(br.readLine());

        if (amount > user.getBalance()) {
            System.out.println("Sorry! You don't have enough money... Your current balance is " + user.getBalance());
            return;
        }
        System.out.println("The transaction was complete! Your new balance is now " + (user.getBalance() - amount));
        user.withdraw(amount);
    }

    public static void deposit() throws IOException {
        int id = checkUser();
        if (id == -1)
            return;
        Account user = users.get(id);
        System.out.println("Welcome " + user.getFullName() + "! Your current balance is " + user.getBalance()
                + ". How much would you like to deposit?");
        long amount = Long.parseLong(br.readLine());
        System.out.println("The transaction was complete! Your new balance is now " + (user.getBalance() + amount));
        user.deposit(amount);
    }

    public static void applyLoan() throws IOException {
        int id = checkUser();
        if (id == -1)
            return;
        Account user = users.get(id);
        System.out.println("Hello "+user.getFullName()+"! How much money would you like to loan? ");
        long amount = Long.parseLong(br.readLine());
        System.out.println("How many days old is this loan?");
        int time = Integer.parseInt(br.readLine());
        double rate = (Math.random() * (7 - 3)) + 3;
        rate = Math.round(rate * 100.0)/100.0;
        System.out.println("Your annual rate will be " + rate + "%");
        ArrayList<Loan> loans = user.getLonas();
        loans.add(new Loan(amount, time, rate));
        user.setLonas(loans);
    }

    public static void viewAcc() throws IOException {
        int id = checkUser();
        if (id == -1)
            return;

        Account user = users.get(id);
        System.out.println("Welcome " + user.getFullName());
        while (true) {
            System.out.println("What would you like to see?\n1.Account name\n2.Balance\n3.APR\n4.Loans\n5.Quit");
            int choice = Integer.parseInt(br.readLine());
            if (choice == 1)
                System.out.println("Your account name is " + user.getFullName());
            else if (choice == 2)
                System.out.println("Your account balance is " + user.getBalance());
            else if (choice == 3)
                System.out.println("Your account APR(annual percentage rate) is " + user.getApr());
            else if (choice == 4) {
                if (user.getLonas().size() == 0) {
                    System.out.println("You have no loans!");
                } else {
                    int counter = 1;
                    System.out.println("Here is a list of your loans");
                    for (Loan i : user.getLonas()) {
                        System.out.println(counter + " " + i.getAmount() + " at " + i.getRate() + "% / year. It has been "
                                + i.getTimeInDays() + " days. Total owe: "
                                + (Math.round((i.getAmount() + (i.getTimeInDays() / 365) * i.getRate()) * 100.0)/100.0));
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

    public static int checkUser() throws IOException {
        System.out.println("What is your bank account ID?");
        int id = Integer.parseInt(br.readLine());

        if (users.keySet().contains(id) == false) {
            System.out.println("Your ID is not registered in the system!");
            return -1;
        }
        return id;
    }
}