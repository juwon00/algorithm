import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Solution {
    public static String[] solution(String[][] plans) {
        List<String> result = new ArrayList<>();

        Arrays.sort(plans, Comparator.comparing(arr -> arr[1]));
        // System.out.println("plans = " + Arrays.deepToString(plans));

        Stack<String> subject = new Stack<>();
        Stack<LocalTime> time = new Stack<>();

        for (String[] plan : plans) {

            // System.out.println();
            // System.out.println("subject = " + subject);
            // System.out.println("time = " + time);

            LocalTime startTime = LocalTime.parse(plan[1], DateTimeFormatter.ofPattern("HH:mm"));
            // System.out.println("startTime = " + startTime);

            while (true) {
                if (!time.isEmpty()) {
                    LocalTime peekTime = time.peek();
                    // System.out.println("peekTime = " + peekTime);

                    int comparison = startTime.compareTo(peekTime);
                    // System.out.println("comparison = " + comparison);

                    if (comparison < 0) {

                        time.replaceAll(localTime -> localTime.plusMinutes(Integer.parseInt(plan[2])));

                        subject.push(plan[0]);
                        time.push(startTime.plusMinutes(Integer.parseInt(plan[2])));
                        break;
                    } else {
                        String subjectPop = subject.pop();
                        time.pop();
                        result.add(subjectPop);
                    }
                } else {
                    subject.add(plan[0]);
                    time.add(LocalTime.parse(plan[1], DateTimeFormatter.ofPattern("HH:mm")).plusMinutes(Integer.parseInt(plan[2])));
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
}