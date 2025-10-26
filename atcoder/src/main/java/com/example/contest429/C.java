package com.example.contest429;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var n = Integer.valueOf(sc.nextLine());
        var lines = sc.nextLine().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < a.length; i++) {
            a[i] = Integer.valueOf(lines[i]);
        }

        int[] count = new int[n + 1];
        for (var v : a) {
            count[v]++;
        }

        int ans = 0;
        for (int i = 1; i < a.length; i++) {
            var c = count[i];
            if (c >= 2) {
                ans += (c * (c - 1) / 2) * (n - c);
            }
        }
        System.out.println(ans);
    }
}
