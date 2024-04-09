public static int solution(int n) {

        int count = Integer.bitCount(n);

        return findNextNumber(count, n);
    }

    private static int findNextNumber(int count, int n) {
        while (true) {
            n++;
            int bitCount = Integer.bitCount(n);
            if (bitCount == count) {
                return n;
            }
        }
    }

//    효율성 테스트에서 실패한 코드
//    public static int solution(int n) {
//
//        String binaryString = "0" + Integer.toBinaryString(n);
//        System.out.println("binaryString = " + binaryString);
//
//        int index1 = 0;
//        for (int i = 0; i < binaryString.length(); i++) {
//            if (binaryString.charAt(i) == '1') {
//                index1 = i;
//            }
//        }
//        System.out.println("index1 = " + index1);
//
//        int index0 = 0;
//        for (int i = 0; i < index1; i++) {
//            if (binaryString.charAt(i) == '0') {
//                index0 = i;
//            }
//        }
//        System.out.println("index0 = " + index0);
//
//        String swapString = swapCharacters(binaryString, index0, index1);
//        System.out.println("swapString = " + swapString);
//
//        int count1 = 0;
//        for (int i = index0 + 1; i < swapString.length(); i++) {
//            if (swapString.charAt(i) == '1') {
//                System.out.println("i = " + i);
//                count1 += 1;
//            }
//        }
//        System.out.println("count1 = " + count1);
//        int count0 = swapString.length() - index0 - count1 - 1;
//        System.out.println("count0 = " + count0);
//
//        String prefix = swapString.substring(0, index0 + 1);
//        System.out.println("prefix = " + prefix);
//
//        String second = appendString(prefix, "0", count0);
//        String third = appendString(second, "1", count1);
//        System.out.println("third = " + third);
//
//        String result = removeFirstZero(third);
//        System.out.println("result = " + result);
//
//        return Integer.parseInt(result, 2);
//    }
//
//    private static String removeFirstZero(String str) {
//        if (str.length() > 0 && str.charAt(0) == '0') {
//            return str.substring(1);  // 첫 번째 문자가 '0'인 경우 첫 번째 문자를 제외한 부분 문자열 반환
//        }
//        return str;  // 첫 번째 문자가 '0'이 아닌 경우 원래 문자열 반환
//    }
//
//    private static String appendString(String prefix, String appendStr, int count) {
//        StringBuilder sb = new StringBuilder(prefix);
//        for (int i = 0; i < count; i++) {
//            sb.append(appendStr);  // 문자열에 특정 문자 추가
//        }
//        return sb.toString();  // 변경된 문자열 반환
//    }
//
//    private static String swapCharacters(String binaryString, int index0, int index1) {
//        // StringBuilder를 사용하여 문자열을 변경
//        StringBuilder sb = new StringBuilder(binaryString);
//        char temp = sb.charAt(index1);  // 첫 번째 문자 임시로 저장
//        sb.setCharAt(index1, sb.charAt(index0));  // 두 번째 문자를 첫 번째 위치로 이동
//        sb.setCharAt(index0, temp);  // 임시로 저장한 문자를 두 번째 위치로 이동
//
//        return sb.toString();  // 변경된 문자열 반환
//    }