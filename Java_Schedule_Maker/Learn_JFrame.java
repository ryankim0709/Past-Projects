package Java_Schedule_Maker;

import javax.swing.*;
import java.util.*;

public class Learn_JFrame {
    public static void main(String[] args) {
        JDialog dialog = new JDialog();
        dialog.setSize(200, 200);
        String p1 = (String) JOptionPane.showInputDialog(dialog, "What is your period one class");
        System.out.println(p1);
        String p2 = (String) JOptionPane.showInputDialog(dialog, "What is your period two class");
    }
}
