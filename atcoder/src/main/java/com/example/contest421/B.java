package com.example.contest421;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        long x = sc.nextLong();
        long y = sc.nextLong();
        long prevPrev = y;
        long prev = reverse(x + y);
        for (int i = 4; i <= 10; i++) {
            long a = prev + prevPrev;
            prevPrev = prev;
            prev = reverse(a);
        }

        System.out.println(prev);

        sc.close();
    }

    private static long reverse(long v) {
        var s = String.valueOf(v);
        int left = 0;
        int right = s.length() - 1;
        char[] r = new char[s.length()];
        while (right >= left) {
            r[left] = s.charAt(right);
            r[right] = s.charAt(left);
            right--;
            left++;
        }
        return Long.valueOf(new String(r));
    }
}
