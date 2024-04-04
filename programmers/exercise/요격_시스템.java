import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public static int solution(int[][] targets) {
        int answer = 0;

        Arrays.sort(targets, Comparator.comparing(arr -> arr[1]));
        // System.out.println("targets = " + Arrays.deepToString(targets));

        int length = targets.length;
        // System.out.println("length = " + length);

        boolean select = false;
        int start = 0;
        int end = 0;
        for (int i = 0; i < length; i++) {
            int s = targets[i][0];
            int e = targets[i][1];


            if (!select) {
                start = targets[i][0];
                end = targets[i][1];
                answer += 1;
                select = true;
                // System.out.println("select = " + select);
            } else {
                // System.out.println("s e= " + s + " " + e);
                if (end > s) {
                    continue;
                } else {
                    select = false;
                    i --;
                }
            }
            // System.out.println("start end = " + start + " " + end);

        }

        return answer;
    }
}