import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the sherlockAndAnagrams function below.
    static int sherlockAndAnagrams(String s) {
        // Can add this map into an integer later for full map 

        HashMap<int[], HashMap<Character, Integer>> masterMap= new HashMap<>();
        HashMap<Integer, HashMap<int[], HashMap<Character, Integer>>>  finalMap= new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                HashMap<Character, Integer> mapToAdd = new HashMap<>();
                for (int k = i; k <= j; k++) {
                    char character = s.charAt(k);
                    if (mapToAdd.containsKey(character)) {
                        mapToAdd.put(character, mapToAdd.get(character) + 1);
                    }
                    else{
                        mapToAdd.put(character, 1);
                    }
                }
                int[] keyToAdd = new int[]{i,j};
                
                int length = (j+1-1);

                masterMap.put(keyToAdd,mapToAdd);

                finalMap.put(length, masterMap);
            }
        }

        // Print out the table 
        for (Map.)

        for (Map.Entry<int[], HashMap<Character, Integer>> entry : masterMap.entrySet()) {
            int[] range = entry.getKey();
            System.out.println("(" + Integer.toString(range[0]) + "," + Integer.toString(range[1]) + ")");
 
            HashMap<Character, Integer> innerMap = entry.getValue();

            for (Map.Entry<Character, Integer> innerEntry : innerMap.entrySet()) {
                System.out.println("Letter " + innerEntry.getKey() + " Count " + Integer.toString(innerEntry.getValue()));
            }
        }

        return 2;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        sherlockAndAnagrams("cdcd");
        // BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        // int q = scanner.nextInt();
        // scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // for (int qItr = 0; qItr < q; qItr++) {
        //     String s = scanner.nextLine();

        //     int result = sherlockAndAnagrams(s);

        //     bufferedWriter.write(String.valueOf(result));
        //     bufferedWriter.newLine();
        // }

        // bufferedWriter.close();

        // scanner.close();
    }
}
