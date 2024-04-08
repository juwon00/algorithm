class Solution {
    public static int solution(int n) {
        int answer = 0;

        int[] dp = new int[60001];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i < n+1; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;
        }
        answer = dp[n] % 1000000007;

        return answer;

//        List로 푸니까 시간초과가 걸림 - int[]보다 오래걸리는듯?
//        List<Integer> dp = new ArrayList<>();
//        dp.add(1);
//        dp.add(1);
//
//
//        for (int i = 2; i < n + 1; i++) {
//            System.out.println("i = " + i);
//            System.out.println("dp = " + dp);
//            dp.add(dp.get(i - 1) + dp.get(i - 2));
//        }
//        System.out.println();
//        System.out.println("dp = " + dp);
//        answer = dp.get(n);
    }
}