import java.util.Arrays;

class Solution
{
    public static int solution(int[][] board) {
        int answer = 0;

        int n = board.length;
        int m = board[0].length;

        int[][] newBoard = new int[n + 1][m + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < m + 1; j++) {
                if (i == 0 || j == 0) {
                    newBoard[i][j] = 0;
                } else {
                    newBoard[i][j] = board[i - 1][j - 1];
                }
            }
        }


        int[][] dp = new int[n + 1][m + 1];

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                dp[i][j] = newBoard[i][j];
                if (newBoard[i][j] == 1) {
                    int tmp = Math.min(dp[i][j - 1], dp[i - 1][j]);
                    int min = Math.min(tmp, dp[i - 1][j - 1]);
                    dp[i][j] += min;
                    answer = Math.max(answer, dp[i][j]);
                }
            }
        }


        return answer * answer;
    }
}