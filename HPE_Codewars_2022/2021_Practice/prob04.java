import java.io.*;

public class prob04 {
    public static void main(String[] args) throws IOException {
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new FileReader("/Users/Ryan/Desktop/judge_datasets_2/prob04-2-in.txt"));
        int size = Integer.parseInt(br.readLine());

        char[][] wave = new char[size][80];

        int max = 0;
        for(int x = 0; x < size; x++) {
            String line = br.readLine();
            max = Math.max(max, line.length());
            for(int y = 0; y < line.length(); y ++) {
                wave[x][y] = line.charAt(y);
            }
        }
        br.close();
        for(int x = size - 1; x >= 0; x--) {
            for(int y = 0; y < max; y++) {
                if(wave[x][y] == '#') {
                    System.out.print("#");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}