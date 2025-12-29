import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        int max = 0;

        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            deque.addLast(num);
            map.put(num, map.getOrDefault(num, 0) + 1);

            if (deque.size() == m) {
                max = Math.max(max, map.size());

                int removed = deque.removeFirst();
                if (map.get(removed) == 1) {
                    map.remove(removed);
                } else {
                    map.put(removed, map.get(removed) - 1);
                }
            }
        }

        System.out.println(max);
    }
}