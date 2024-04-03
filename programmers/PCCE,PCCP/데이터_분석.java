import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        List<List<Integer>> arr = new ArrayList<>();

        for (int[] row : data) {
            List<Integer> a = new ArrayList<>();
            if (ext.equals("code")) {
                if (row[0] < val_ext) {
                    for (int num : row) {
                        a.add(num);
                    }
                }
            }
            else if (ext.equals("date")) {
                if (row[1] < val_ext) {
                    for (int num : row) {
                        a.add(num);
                    }
                }

            }
            else if (ext.equals("maximum")) {
                if (row[2] < val_ext) {
                    for (int num : row) {
                        a.add(num);
                    }
                }
            }
            else if (ext.equals("remain")) {
                if (row[3] < val_ext) {
                    for (int num : row) {
                        a.add(num);
                    }
                }
            }
            if (a.size() > 0) {
                arr.add(a);
            }

        }

        if (sort_by.equals("code")) {
            Collections.sort(arr, Comparator.comparingInt(list -> list.get(0)));
        }
        else if (sort_by.equals("date")) {
            Collections.sort(arr, Comparator.comparingInt(list -> list.get(1)));
        }
        else if (sort_by.equals("maximum")) {
            Collections.sort(arr, Comparator.comparingInt(list -> list.get(2)));
        }
        else if (sort_by.equals("remain")) {
            Collections.sort(arr, Comparator.comparingInt(list -> list.get(3)));
        }
        // System.out.println(arr);

        int[][] answer = new int[arr.size()][4];
        for (int i = 0; i < arr.size(); i++){
            answer[i][0] = arr.get(i).get(0);
            answer[i][1] = arr.get(i).get(1);
            answer[i][2] = arr.get(i).get(2);
            answer[i][3] = arr.get(i).get(3);
        }

        return answer;
    }
}