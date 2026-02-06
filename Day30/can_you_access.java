import java.io.*;
import java.util.*;

public class Solution {

    class Inner {
        private class Private {
            private boolean powerof2(int num) {
                return ((num & (num - 1)) == 0);
            }
        }
    }

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        Solution solution = new Solution();
        Solution.Inner inner = solution.new Inner();
        Solution.Inner.Private obj = inner.new Private();

        System.out.println(num + " is " + (obj.powerof2(num) ? "power of 2" : "not a power of 2"));
        System.out.println("An instance of class: Solution.Inner.Private has been created");

        sc.close();
    }
}