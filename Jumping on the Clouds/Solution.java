import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the jumpingOnClouds function below.
    static int jumpingOnClouds(int[] c) {
        int steps = 0;
        int position = 0;
        while (position < c.length - 1) {
            if (position <= c.length - 3 && c[position+2] != 1) {
                position += 2;
            }
            else {
                position += 1;
            }
            steps += 1;
        }
        return steps;
    }

    // private static final Scanner scanner = new Scanner(System.in); 

    public static void main(String[] args) throws IOException {
        int[] c = new int[] {0, 0, 0, 1, 0, 0};
        System.out.println(jumpingOnClouds(c));
        // BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        // int n = scanner.nextInt();
        // scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // int[] c = new int[n];

        // String[] cItems = scanner.nextLine().split(" ");
        // scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // for (int i = 0; i < n; i++) {
        //     int cItem = Integer.parseInt(cItems[i]);
        //     c[i] = cItem;
        // }

        // int result = jumpingOnClouds(c);

        // bufferedWriter.write(String.valueOf(result));
        // bufferedWriter.newLine();

        // bufferedWriter.close();

        // scanner.close();
    }
}
