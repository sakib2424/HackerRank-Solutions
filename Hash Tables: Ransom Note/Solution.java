import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {
        Hashtable<String, Integer> mag = new Hashtable<>();
        for (int i = 0; i < magazine.length; i++) {
            String word = magazine[i];
            int count = mag.containsKey(word) ? mag.get(word) : 0;
            mag.put(word, count + 1);
        }

        for (int j = 0; j < note.length; j++) {
            String word = note[j];
            if (!mag.containsKey(word)) {
                System.out.printf("No");
                return;
            }
            int count = mag.get(word);
            if (count < 1) {
                System.out.printf("No");
                return;
            }
            mag.put(word, count - 1);
        }
        System.out.printf("Yes");
        return ;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] mn = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mn[0]);

        int n = Integer.parseInt(mn[1]);

        String[] magazine = new String[m];

        String[] magazineItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            String magazineItem = magazineItems[i];
            magazine[i] = magazineItem;
        }

        String[] note = new String[n];

        String[] noteItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String noteItem = noteItems[i];
            note[i] = noteItem;
        }

        checkMagazine(magazine, note);

        scanner.close();
    }
}
