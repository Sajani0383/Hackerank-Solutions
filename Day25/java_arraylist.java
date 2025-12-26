import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().trim().split(" ");
            int d = Integer.parseInt(parts[0]);

            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 1; j <= d; j++) {
                row.add(Integer.parseInt(parts[j]));
            }
            list.add(row);
        }

        int q = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < q; i++) {
            String[] query = br.readLine().trim().split(" ");
            int x = Integer.parseInt(query[0]) - 1;
            int y = Integer.parseInt(query[1]) - 1;

            if (x < list.size() && y < list.get(x).size()) {
                System.out.println(list.get(x).get(y));
            } else {
                System.out.println("ERROR!");
            }
        }

        br.close();
    }
}