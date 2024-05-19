import java.util.*;

class Solution {
    public static int solution(int[][] board, int[] moves) {
        int answer = 0;

        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        for (int i = 0; i < moves.length; i++) {
            // System.out.println("moves = " + moves[i]);

            for (int j = 0; j < board.length; j++) {
                // System.out.println("board = " + board[j][moves[i] - 1]);
                if (board[j][moves[i] - 1] > 0) {
                    if (stack.peek() == board[j][moves[i] - 1]) {
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(board[j][moves[i] - 1]);
                    }
                    board[j][moves[i] - 1] = 0;
                    break;
                }
            }
            // System.out.println();
        }
//         for (int[] b : board) {
//             System.out.println("b = " + Arrays.toString(b));
//         }
        return answer;
    }
}