package com.example.contest421;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var n = sc.nextInt();

        String[] memo = new String[n + 1];
        for (int i = 0; i < n; i++) {
            memo[i + 1] = sc.next();
        }

        int x = sc.nextInt();
        String y = sc.next();

        System.out.println(memo[x].equals(y) ? "Yes" : "No");

        sc.close();
    }
}
