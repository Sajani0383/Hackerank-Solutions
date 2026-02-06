import java.io.*;
import java.util.*;

class Add {
    void add(int... nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            System.out.print(nums[i]);
            if (i < nums.length - 1) System.out.print("+");
        }
        System.out.println("=" + sum);
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int f = sc.nextInt();

        Add obj = new Add();
        obj.add(a, b);
        obj.add(a, b, c);
        obj.add(a, b, c, d, e);
        obj.add(a, b, c, d, e, f);

        sc.close();
    }
}