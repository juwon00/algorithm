import java.util.*;

class Solution {
    public static int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int length = sequence.length;


        int start = 0;
        int end = 0;
        int tmp = sequence[0];
        // System.out.println("length = " + length);

        List<List<Integer>> range = new ArrayList<>();

        while (true) {

            // System.out.println("start end = " + start + " " + end);
            // System.out.println("tmp = " + tmp);
            // System.out.println(range);

            if (tmp == k) {
                List<Integer> r = new ArrayList<>();
                r.add(start);
                r.add(end);
                range.add(r);
                tmp -= sequence[start];
                start += 1;
            } else if (tmp < k) {
                end += 1;
                if (end > length - 1) {
                    break;
                }
                tmp += sequence[end];
            } else if (tmp > k) {
                tmp -= sequence[start];
                start += 1;
            }

        }

        range.sort(Comparator.comparing(arr -> arr.get(1) - arr.get(0)));
        // System.out.println("range = " + range);
        answer[0] = range.get(0).get(0);
        answer[1] = range.get(0).get(1);

        return answer;
    }
}