class Solution {
    public static String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        int[][] position = {
                {0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 1}, {1, 2}, {1, 3}, {2, 1}, {2, 2}, {2, 3}, {3, 1}, {3, 2}, {3, 3}
        };
        // System.out.println("position = " + Arrays.deepToString(position));


        int left = 10;
        int right = 12;

        for (int n : numbers) {
            if (n == 0) {
                n = 11;
            }
            // System.out.println("n = " + n);
            if (n == 1 || n == 4 || n == 7) {
                answer.append("L");
                left = n;
            } else if (n == 3 || n == 6 || n == 9) {
                answer.append("R");
                right = n;
            } else {
                int leftDistance = Math.abs(position[n][0] - position[left][0]) + Math.abs(position[n][1] - position[left][1]);
                int rightDistance = Math.abs(position[n][0] - position[right][0]) + Math.abs(position[n][1] - position[right][1]);
                // System.out.println("Distance = " + leftDistance + " " + rightDistance);
                if (leftDistance < rightDistance) {
                    answer.append("L");
                    left = n;
                } else if (leftDistance > rightDistance) {
                    answer.append("R");
                    right = n;
                } else {
                    if (hand.equals("right")) {
                        answer.append("R");
                        right = n;
                    } else if (hand.equals("left")) {
                        answer.append("L");
                        left = n;
                    }
                }
            }
            // System.out.println("left right = " + left + " " + right);
            // System.out.println();
        }

        return answer.toString();
    }
}