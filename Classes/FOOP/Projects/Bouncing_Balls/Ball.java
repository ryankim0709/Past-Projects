package Classes.FOOP.Projects.Bouncing_Balls;

/*
 * You will need to alter code in this class!
 * First, make sure a single ball bounces 
 * around the screen correctly.
 * Add collisions between the multiple objects.
 */

import java.awt.*;
import java.awt.geom.Rectangle2D;
import java.util.Formatter;

public class Ball {
    public double x, y; // Ball's center x and y
    public double speedX, speedY; // Ball's speed per step in x and y
    public double radius;
    private Color color;

    /**
     * Constructor to create the ball and it's attributes.
     * 
     * @param x             : x coordinate of the center of the ball
     * @param y             : y coordinate of the center of the ball
     * @param radius        : radius of the ball
     * @param speed         : speed the ball will move (converted to x and y
     *                      components later)
     * @param angleInDegree : direction ball will initially move
     * @param color         : color of the ball
     */
    public Ball(double x, double y, double radius, double speed, double angleInDegree, Color color) {
        // Notice the 'global' variables have the same name as the parameters.
        // Use the .this keyword to signify the 'global' variable
        this.x = x;
        this.y = y;
        // Convert (speed, angle) to (x, y)
        this.speedX = (speed * Math.cos(Math.toRadians(angleInDegree)));
        this.speedY = (-speed * Math.sin(Math.toRadians(angleInDegree)));
        this.radius = radius;
        this.color = color;
    }

    /**
     * Update the graphics on the screen
     * 
     * @param g: Graphics object
     */
    public void draw(Graphics g) {
        g.setColor(color);
        g.fillOval((int) x, (int) y, (int) (2 * radius), (int) (2 * radius));
    }

    /**
     * Move, check for collisions and react accordingly if collision occurs.
     * 
     * @param box: the container (obstacle) for this ball.
     */
    // Used to determine how to reflect off the walls of the screen
    public void moveOneStepWithCollisionDetection(ContainerBox box) {
        // Use the variable box to get the max/min x/y values of the screen

        // Next step
        this.x += speedX;
        this.y += speedY;

        if (this.x <= box.minX || this.x >= box.maxX) {
            this.speedX = -1 * this.speedX;
        }
        if (this.y <= box.minY || this.y >= box.maxY) {
            this.speedY = -1 * this.speedY;
        }
    } 

    public void collides(Ball b2) {
        // Use this classes x, y, and radius
        // Compare versus the b2.x, b2.y, and b2.radius
        // Determine if they collide and have them bounce off each other
        double distance = Math.sqrt((this.x - b2.x) * (this.x - b2.x) + (this.y - b2.y) * (this.y - b2.y));
        if (distance <= this.radius + b2.radius) {
            this.speedX = -1 * this.speedX;
            this.speedY = -1 * this.speedY;
            b2.speedX = -1 * b2.speedX;
            b2.speedY = -1 * b2.speedY;
        }
    }

    /** Return the magnitude of speed. */
    public double getSpeed() {
        return Math.sqrt(speedX * speedX + speedY * speedY);
    }

    /** Return the direction of movement in degrees (counter-clockwise). */
    public double getMoveAngle() {
        return Math.toDegrees(Math.atan2(-speedY, speedX));
    }
}
