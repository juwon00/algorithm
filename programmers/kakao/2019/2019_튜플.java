import java.util.*;

class Solution {
    public static int[] solution(String s) {

        String ss = s.substring(1, s.length() - 1);
        // System.out.println("ss = " + ss);


        List<List<Integer>> parts = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        StringBuilder builder = new StringBuilder();
        int count = 0;

        for (char c : ss.toCharArray()) {

            // System.out.println("c = " + c);

            if (c == '{') {
                count++;
            } else if (c == '}') {
                count--;
            }

            if (c == ',') {
                tmp.add(Integer.valueOf(builder.toString()));
                builder = new StringBuilder();
            } else if (c != '{' && c != '}') {
                builder.append(c);
            }


            if (count == 0 && c == ',') {
                // System.out.println("find");
                parts.add(tmp);
                tmp = new ArrayList<>();
            }
        }
        // 마지막 부분 추가
        tmp.add(Integer.valueOf(builder.toString()));
        parts.add(tmp);


        // Comparator를 사용하여 리스트를 정렬합니다.
        Collections.sort(parts, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> list1, List<Integer> list2) {
                return Integer.compare(list1.size(), list2.size());
            }
        });

        // for (List<Integer> part : parts) {
        //     System.out.println("part = " + part);
        // }


        int n = parts.size();
        int[] answer = new int[n];
        answer[0] = parts.get(0).get(0);


        for (int i = 1; i < n; i++) {
            // System.out.println("i = " + i);

            List<Integer> tmp1 = new ArrayList<>(parts.get(i));
            List<Integer> tmp2 = new ArrayList<>(parts.get(i - 1));

            tmp1.removeAll(tmp2);
            // System.out.println("tmp1 = " + tmp1);
            answer[i] = tmp1.get(0);


            // for (List<Integer> part : parts) {
            //     System.out.println("part = " + part);
            // }
        }


        return answer;
    }
//     다른사람의 더 깔끔한 풀이
//     Set.add()를 활용
//     public static int[] solution(String s) {
//
//         Set<String> set = new HashSet<>();
//         String[] arr = s.replaceAll("[{]", " ").replaceAll("[}]", " ").trim().split(" , ");
//         System.out.println("s = " + s);
//         System.out.println("arr = " + Arrays.toString(arr));
//
//         Arrays.sort(arr, (a, b) -> {
//             return a.length() - b.length();
//         });
//         System.out.println("arr = " + Arrays.toString(arr));
//
//         int[] answer = new int[arr.length];
//         int idx = 0;
//         for (String s1 : arr) {
//             System.out.println("s1 = " + s1);
//             for (String s2 : s1.split(",")) {
//                 System.out.println("s2 = " + s2);
//                 System.out.println("set = " + set);
//                 if (set.add(s2)) answer[idx++] = Integer.parseInt(s2);
//             }
//             System.out.println();
//         }
//         return answer;
//     }
}