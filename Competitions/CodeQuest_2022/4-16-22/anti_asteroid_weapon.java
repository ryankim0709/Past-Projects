import java.util.*;
import java.io.*;

public class anti_asteroid_weapon {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++) {
            int n = Integer.parseInt(br.readLine());
            TreeMap<Double, HashSet<String>> dist = new TreeMap<>();
            for (int j = 0; j < n; j++) {
                String coord = br.readLine();
                String[] coords = coord.split(" ");
                int x = Integer.parseInt(coords[0]);
                int y = Integer.parseInt(coords[1]);
                Double distance = Math.sqrt(x * x + y * y);
                dist.putIfAbsent(distance, new HashSet<>());
                dist.get(distance).add(coord);
            }

            for (Double j : dist.keySet()) {
                for (String k : dist.get(j)) {
                    System.out.println(k);
                }
            }
        }
    }
}
