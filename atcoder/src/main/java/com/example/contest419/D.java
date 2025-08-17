package com.example.contest419;

import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int length = sc.nextInt();
        int query = sc.nextInt();

        String s = sc.next();
        String t = sc.next();

        int[] memo = new int[length + 1];

        for (int i = 0; i < query; i++) {
            var l = sc.nextInt();
            var r = sc.nextInt();
            l--;
            memo[l]++;
            memo[r]--;
        }

        for (int i = 0; i < length; i++) {
            memo[i + 1] += memo[i];
        }

        for (int i = 0; i < length; i++) {
            if (memo[i] % 2 == 0) {
                System.out.print(s.charAt(i));
            } else {
                System.out.print(t.charAt(i));
            }
        }

        System.out.println();
        sc.close();
    }
}
