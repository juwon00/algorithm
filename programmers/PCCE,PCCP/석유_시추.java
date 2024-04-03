import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] land = {
                {0, 0, 0, 1, 1, 1, 0, 0},
                {0, 0, 0, 0, 1, 1, 0, 0},
                {1, 1, 0, 0, 0, 1, 1, 0},
                {1, 1, 1, 0, 0, 0, 0, 0},
                {1, 1, 1, 0, 0, 0, 1, 1}
        };

        int result = solution(land);
        System.out.println("result = " + result);
    }

    public static int solution(int[][] land) {
        int answer = 0;

        Map<Integer, Integer> bfs = new HashMap<>();
        int color = 2;

        int[] dx = {0, 1, 0, -1};
        int[] dy = {-1, 0, 1, 0};

        int n = land.length;
        int m = land[0].length;
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.println("i = " + i + j);
                if (land[i][j] == 1) {

                    int count = 1;
                    Queue<Node> q = new LinkedList<>();
                    q.offer(new Node(i, j));
                    visited[i][j] = true;
                    land[i][j] = color;
                    System.out.println("node = " + i + j);

                    while (!q.isEmpty()) {
                        Node node = q.poll();
                        System.out.println("node = " + node.x + node.y);

                        for (int k = 0; k < 4; k++) {
                            int nx = node.x + dx[k];
                            int ny = node.y + dy[k];
                            if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                                if (land[nx][ny] == 1 && !visited[nx][ny]) {
                                    visited[nx][ny] = true;
                                    q.offer(new Node(nx, ny));
                                    count += 1;
                                    land[nx][ny] = color;
                                }
                            }
                        }
                    }
                    bfs.put(color, count);
                    color += 1;
                }
            }
            System.out.println();
        }

        System.out.println("bfs = " + bfs);
        for (int[] ints : land) {
            System.out.println("land = " + Arrays.toString(ints));
        }

        for (int i = 0; i < m; i++) {
            List<Integer> v = new ArrayList<>();
            int tmp = 0;
            for (int j = 0; j < n; j++) {
                System.out.println("i = " + j + i);
                if (land[j][i] > 0) {
                    if (!v.contains(land[j][i])) {
                        v.add(land[j][i]);
                    }
                }
            }
            System.out.println("v = " + v);
            for (Integer integer : v) {
                System.out.println("integer = " + integer);
                tmp += bfs.get(integer);
            }
            System.out.println("tmp = " + tmp);
            if (tmp > answer) {
                answer = tmp;
            }
            System.out.println();
        }

        return answer;
    }

    public static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
