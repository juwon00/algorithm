import java.util.*;

class Solution {
    public static int[] solution(String[] gems) {
        int[] answer = new int[2];

        // System.out.println("gems = " + Arrays.toString(gems));
        HashMap<String, Integer> hash = new HashMap<>();

        int left = 0;
        int right = 0;
        int size = 0;

        for (int i = 0; i < gems.length; i++) {
            // System.out.println(gems[i] + " " + i);

            hash.put(gems[i], i);
            right = i;

            if (gems[right].equals(gems[left])) {
                // System.out.println("find");
                left = Collections.min(hash.values());
                if (answer[1] - answer[0] > right - left) {
                    // System.out.println("new");
                    answer = new int[] { left + 1, right + 1 };
                }
            }

            if (size != hash.size()) {
                // System.out.println("size change");
                size = hash.size();
                answer = new int[] { left + 1, right + 1 };
            }

            // System.out.println("left right = " + left + " " + right);
            // System.out.println("hash = " + hash);
            // System.out.println();
        }

        return answer;
    }
}