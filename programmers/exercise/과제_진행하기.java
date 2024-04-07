import java.util.*;

class Solution {
    public static String[] solution(String[][] plans) {
        List<String> result = new ArrayList<>();

        Arrays.sort(plans, Comparator.comparing(arr -> arr[1]));
        // System.out.println("plans = " + Arrays.deepToString(plans));

        Stack<String> subject = new Stack<>();
        Stack<Integer> time = new Stack<>();

        for (String[] plan : plans) {

            // System.out.println();
            // System.out.println("subject = " + subject);
            // System.out.println("time = " + time);

            Integer startTime = convertToMinutes(plan[1]);
            // System.out.println("startTime = " + startTime);

            while (true) {
                if (!time.isEmpty()) {
                    Integer peekTime = time.peek();
                    // System.out.println("peekTime = " + peekTime);

                    int comparison = startTime - peekTime;
                    // System.out.println("comparison = " + comparison);

                    if (comparison < 0) {

                        time.replaceAll(localTime -> localTime + Integer.parseInt(plan[2]));

                        subject.push(plan[0]);
                        time.push(startTime + Integer.parseInt(plan[2]));
                        break;
                    } else {
                        String subjectPop = subject.pop();
                        time.pop();
                        result.add(subjectPop);
                    }
                } else {
                    subject.add(plan[0]);
                    time.add(convertToMinutes(plan[1]) + Integer.parseInt(plan[2]));
                    break;
                }
            }
        }
        // System.out.println("subject = " + subject);
        // System.out.println("time = " + time);
        while (!subject.isEmpty()) {
            String pop = subject.pop();
            result.add(pop);
        }
        // System.out.println("result = " + result);

        return result.toArray(new String[0]);
    }

    private static Integer convertToMinutes(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}