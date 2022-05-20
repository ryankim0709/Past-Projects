package Classes.FOOP.Projects.Java_Turtle;

import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;
import java.io.*;

public class SnowFlake {
    static Color penColor;
    static Turtle turtle;
    static int colorInd = -1;
    static String[] colors;

    public static void main(String[] args) throws IOException {
        World world = new World(1000, 1000);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("How many sides you want on your snowflake?");
        int sides = Integer.parseInt(br.readLine());
        System.out.println("Please input a list of colors in (R G B) form. ex (225, 50, 100)/(200, 100, 75)");
        // RGB values can range from 0 to 225

        colors = br.readLine().split("/");
        turtle = new Turtle(world);
        drawSnowFlake(sides);
        world.setVisible(true);
    }
    
    public static void drawSnowFlake(int sides) {
        turtle.moveTo(500, 500);
        for (int i = 0; i < sides; i++) {
            updateColor();
            drawSquares();
            turtle.turn(360.0/(sides));
        }
    }

    public static void drawSquares() {
        // Offset
        turtle.penUp();
        turtle.forward(5);
        turtle.turnRight();
        turtle.forward(5);
        turtle.turnLeft();
        turtle.penDown();

        // Draw Squares
        for (int i = 0; i < 4; i++) {
            drawSquare();
            turtle.penUp();
            turtle.forward(10);
            turtle.penDown();
        }

        // Return Offset
        turtle.penUp();
        turtle.moveTo(500, 500);
        turtle.penDown();
    }

    public static void drawSquare() {
        for (int i = 0; i < 4; i++) {
            turtle.forward(300);
            turtle.turnRight();
        }
        turtle.turnLeft();
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
