import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int line = 1;
        while (sc.hasNextLine()) {
            System.out.println(line + " " + sc.nextLine());
            line++;
        }
        sc.close();
    }
}