import java.util.*;
import java.io.*;

public class prob15 {
    static HashMap<String, Integer> gems = new HashMap<>();
    static class Pony implements Comparable<Pony> {
        String name;
        public Pony(String name) {
            this.name = name;
        }

        public int compareTo(Pony a) {
            // Case one: One has gemstone while another does not
            boolean oneHas = false;
            boolean twoHas = false;
            
            return 1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Pony> ponies = new ArrayList<>();

        String line = "";
        while(true) {
            line = br.readLine();
            if(line == "END") break;
            else ponies.add(new Pony(line));
        }

        gems.put("Garnet", 0);
        gems.put("Amethyst", 1);
        gems.put("Aquamarine", 2);
        gems.put("Diamond", 3);
        gems.put("Emerald", 4);
        gems.put("Pearl", 5);
        gems.put("Ruby", 6);
        gems.put("Peridot", 7);
        gems.put("Sapphire", 8);
        gems.put("Tourmaline", 9);
        gems.put("Topaz", 10);
        gems.put("Lapis", 11);

        Collections.sort(ponies);
    }
}