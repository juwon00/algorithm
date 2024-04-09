static int solution(int[][] land) {
        int answer = 0;

        int n = land.length;

        int[][] dp = new int[n + 1][4];
        System.out.println("dp = " + Arrays.deepToString(dp));

        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (j == k) {
                        continue;
                    }
                    System.out.println("ijk = " + i + " " + j + " " + k);
                    dp[i][j] = Math.max(dp[i][j], land[i - 1][j] + dp[i - 1][k]);

                    answer = Math.max(dp[i][j], answer);
                }
            }
        }

        System.out.println("dp = " + Arrays.deepToString(dp));

        return answer;
    }

//    효율성 테스트에서 실패한 코드
//    static int solution(int[][] land) {
//
//        int n = land.length;
//        System.out.println("n = " + n);
//
//        List<List<Integer>> lands = new ArrayList<>();
//        for (int[] rows : land) {
//            List<Integer> rowList = new ArrayList<>();
//            for (int num : rows) {
//                rowList.add(num);
//            }
//            lands.add(rowList);
//        }
//        System.out.println("lands = " + lands);
//
//        for (int i = 1; i < n; i++) {
//            for (int j = 0; j < 4; j++) {
//                System.out.println("i j = " + i + " " + j);
//                List<Integer> tmp = new ArrayList<>(lands.get(i - 1));
//                tmp.remove(j);
//                System.out.println("tmp = " + tmp);
//                Integer max = Collections.max(tmp);
//                System.out.println("max = " + max);
//                lands.get(i).set(j, lands.get(i).get(j) + max);
//            }
//        }
//        System.out.println("lands = " + lands);
//        return Collections.max(lands.get(n - 1));
//    }