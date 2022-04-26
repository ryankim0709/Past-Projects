package Classwork.FOOP;
import java.io.*;
import java.util.*;

public class eight_ball {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] responses = { "It is certain", "I don't know about that", "try asking again", "It will not", "No",
                "Yes" };
        
        while (true) {
            System.out.println("What would you like to ask? (type 'quit' to quit)");
            String question = br.readLine();
            if (question.toLowerCase() == "quit") {
                break;
            }
            int rand = (int) (Math.random() * 5);
            System.out.println(responses[rand]);
        }
    }
}
