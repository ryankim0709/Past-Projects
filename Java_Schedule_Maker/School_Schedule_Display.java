package Java_Schedule_Maker;

import javax.swing.*;

public class School_Schedule_Display {
    public static void main(String[] args) {
        JDialog input = new JDialog();
        input.setSize(200, 200);
        // Get the users schedule
        String[] schedule = new String[8];
        String p0 = (String) JOptionPane.showInputDialog(input, "What is your period zero class?");
        schedule[0] = p0;
        String p1 = (String) JOptionPane.showInputDialog(input, "What is your period one class?");
        schedule[1] = p1;
        String p2 = (String) JOptionPane.showInputDialog(input, "What is your period two class?");
        schedule[2] = p2;
        String p3 = (String) JOptionPane.showInputDialog(input, "What is your period three class?");
        schedule[3] = p3;
        String p4 = (String) JOptionPane.showInputDialog(input, "What is your period four class?");
        schedule[4] = p4;
        String p5 = (String) JOptionPane.showInputDialog(input, "What is your period five class?");
        schedule[5] = p5;
        String p6 = (String) JOptionPane.showInputDialog(input, "What is your period six class?");
        schedule[6] = p6;
        String p7 = (String) JOptionPane.showInputDialog(input, "What is your period seven class?");
        schedule[7] = p7;

        for (int i = 0; i < 8; i++) {
            // If the user entered nothing, assume it's a prep period
            if (schedule[i] == null) {
                schedule[i] = "Prep Period";
            }
        }
        
        // Option choice and choices user has
        String option = "";
        Object[] options = { "Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Quit" };
        while (option != "Quit") {
            // Display which day they want to look at
            // Added Paly logo :)
            option = (String) JOptionPane.showInputDialog(input, "Schedule for which day?", "Day picker",
                    JOptionPane.PLAIN_MESSAGE, new ImageIcon("Java_Schedule_Maker/img/paly_icon.png"), options,
                    "anchor");
            String message = "";
            String title = "Schedule for " + option;
            // Generate schedule using if statements
            if (option == "Monday") {
                message = "Zero Period ~ " + schedule[0] + " 7:55-8:50\n1st Period ~ " + schedule[1]
                        + " 9:00-9:45\n2nd Period ~ "
                        + schedule[2] + " 9:55-10:40\n3rd Period ~ " + schedule[3] + " 10:55-11:40\n4rth Period ~ "
                        + schedule[4] + " 11:50-12:35\nLunch ~ 12:35-1:15\n5th Period ~ " + schedule[5]
                        + " 1:15-2:00\n6th Period ~ "
                        + schedule[6] + " 2:10-2:55\n7th Period ~ " + schedule[7] + " 3:05-3:50";
            } else if (option == "Tuesday" || option == "Thursday") {
                message = "Zero Period ~ " + schedule[0] + " 7:55-8:50\n1st Period ~ " + schedule[1]
                        + " 9:00-10:35\n2nd Period ~ "
                        + schedule[2] + " 10:50-12:20\nLunch 12:20-1:00\n3rd Period ~ " + schedule[3]
                        + " 1:00-2:30\n4rth Period ~ "
                        + schedule[4] + " 2:40-4:10";
            } else if (option == "Wedensday") {
                message = "Zero Period ~ " + schedule[0] + " 7:55-8:50\n5th Period ~ " + schedule[5]
                        + " 9:00-9:45\n6th Period ~ "
                        + schedule[6] + " 9:55-10:40\nLunch 12:20-1:00\n7th Period ~ " + schedule[7]
                        + " 1:00-2:30\nPRIME "
                        + " 2:40-3:30";
            } else if (option == "Friday") {
                message = "5th Period ~ " + schedule[5]
                        + " 9:00-9:45\n6th Period ~ "
                        + schedule[6] + " 9:55-10:40\nLunch 12:20-1:00\nAdvisory 1:00-1:50\n7th Period ~ " + schedule[7]
                        + " 1:00-2:30";
            } else {
                continue;
            }
            // Display schedule
            JOptionPane.showMessageDialog(input, message, title, JOptionPane.DEFAULT_OPTION);
        }
    }
}
