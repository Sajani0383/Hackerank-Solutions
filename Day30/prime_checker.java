import java.io.*;
import java.util.*;

class Prime {
    void checkPrime(int... nums) {
        boolean printed = false;
        for (int n : nums) {
            if (isPrime(n)) {
                System.out.print(n + " ");
                printed = true;
            }
        }
        if (printed) System.out.println();
        else System.out.println();
    }

    boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int n4 = sc.nextInt();
        int n5 = sc.nextInt();

        Prime p = new Prime();
        p.checkPrime(n1);
        p.checkPrime(n1, n2);
        p.checkPrime(n1, n2, n3);
        p.checkPrime(n1, n2, n3, n4, n5);

        sc.close();
    }
}