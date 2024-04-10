import java.util.*;

class Solution {
    public static long solution(int n, int[] works) {
        long answer = 0;

        PriorityQueue<Integer> worksHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int work : works) {
            worksHeap.add(work);
        }
        // System.out.println("worksHeap = " + worksHeap);

        for (int i = 0; i < n; i++) {
            Integer poll = worksHeap.poll() - 1;
            worksHeap.add(poll);
        }
        if (worksHeap.peek() <= 0) {
            return 0;
        }

        // System.out.println("worksHeap = " + worksHeap);
        for (Integer work : worksHeap) {
            answer += Math.pow(work, 2);
        }

        return answer;
    }
}