package com.example.contest429;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var oneLines = sc.nextLine().split(" ");
        var secondLines = sc.nextLine().split(" ");

        int n = Integer.valueOf(oneLines[0]);
        int m = Integer.valueOf(oneLines[1]);
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.valueOf(secondLines[i]);
        }

        boolean isOk = false;
        for (int i = 0; i < n; i++) {
            int c = 0;
            for (int j = 0; j < a.length; j++) {
                if (i == j) {
                    continue;
                }
                c += a[j];
            }
            if (c == m) {
                isOk = true;
                break;
            }
        }
        System.out.println(isOk ? "Yes" : "No");
    }
}
