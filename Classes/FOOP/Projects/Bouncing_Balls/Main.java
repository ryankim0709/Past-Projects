package Classes.FOOP.Projects.Bouncing_Balls;

/*
 *You do not need to alter anything in this Class.
 *
 *This is the main file used to run the program.
 *If you want to adjust the size of the screen, you can do so here 
 *Thank you to the 'local' University that provided us with a template to alter
 */
import javax.swing.JFrame;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("How many balls in the world?");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numBalls = Integer.parseInt(br.readLine());
        JFrame frame = new JFrame("Bouncing Ball");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        BallWorld size = new BallWorld(640, 480, numBalls);
        frame.setContentPane(size);
        frame.pack();
        frame.setVisible(true);
    }
}
