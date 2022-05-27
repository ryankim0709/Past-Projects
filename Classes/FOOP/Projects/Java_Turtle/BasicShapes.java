package Classes.FOOP.Projects.Java_Turtle;

import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;
import java.io.*;

public class BasicShapes {
    static Color penColor;
    static Turtle turtle;
    static int colorInd = -1;
    static String[] colors;

    public static void main(String[] args) throws IOException {
        World world = new World(1000, 1000);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("How many sides you want on your shapes?");
        int sides = Integer.parseInt(br.readLine());
        System.out.println("Please input a list of colors in (R G B) form. ex (225, 50, 100)/(200, 100, 75)");
        // RGB values can range from 0 to 225

        colors = br.readLine().split("/");
        double degrees = 360.0 / sides;

        turtle = new Turtle(world);
        updateColor();

        drawPolygon(degrees);
        drawPinwheel(degrees);
        drawAsterics(degrees);

        world.setVisible(true);
    }

    public static void drawPolygon(double degrees) {
        turtle.penUp();
        turtle.moveTo(300, 300);
        turtle.penDown();
        for (int i = 0; i < 360 / degrees; i++) {
            updateColor();
            turtle.forward(50);
            turtle.turn(degrees);
        }
    }

    public static void drawPinwheel(double degrees) {
        turtle.penUp();
        turtle.moveTo(600, 600);
        turtle.penDown();
        for (int i = 0; i < 360 / degrees; i++) {
            updateColor();
            turtle.forward(100);
            turtle.backward(50);
            turtle.turn(degrees);
        }
    }

    public static void drawAsterics(double degrees) {
        turtle.penUp();
        turtle.moveTo(200, 800);
        turtle.penDown();
        for (int i = 0; i < 360 / degrees; i++) {
            updateColor();
            turtle.forward(50);
            turtle.backward(50);
            turtle.turn(degrees);
        }
    }

    public static void updateColor() {
        colorInd += 1;
        colorInd = colorInd % colors.length;
        String currColor = colors[colorInd];
        currColor = currColor.replace("(", "");
        currColor = currColor.replace(")", "");
        String[] rgb = currColor.split(", ");
        turtle.setPenColor(new Color(Integer.parseInt(rgb[0]), Integer.parseInt(rgb[1]), Integer.parseInt(rgb[2])));
    }
}
