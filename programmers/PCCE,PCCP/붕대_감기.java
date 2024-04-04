import java.util.Arrays;

class Solution {
    public static int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;

        int length = attacks[attacks.length - 1][0];
        // System.out.println("length = " + length);

        int[] h = new int[length + 1];
        h[0] = health;
        // System.out.println("h = " + Arrays.toString(h));

        int addRecovery = 0;
        for (int i = 1; i < length + 1; i++) {

            int attackTime = 0, hurt = 0;
            for (int j = 0; j < attacks.length; j++) {
                if (attacks[j][0] == i) {
                    attackTime = attacks[j][0];
                    hurt = attacks[j][1];
                    break;
                }
            }
            // System.out.println("attackTime hurt= " + attackTime + " " + hurt);

            if (attackTime == 0) {
                h[i] = h[i - 1] + bandage[1];
                addRecovery += 1;
            } else {
                h[i] = h[i - 1] - hurt;
                addRecovery = 0;
            }

            if (addRecovery == bandage[0]) {
                h[i] += bandage[2];
                addRecovery = 0;
            }

            if (h[i] > health) {
                h[i] = health;
            }

            if (h[i] <= 0) {
                return -1;
            }


        }
        // System.out.println("h = " + Arrays.toString(h));

        answer = h[length];
        return answer;
    }
}