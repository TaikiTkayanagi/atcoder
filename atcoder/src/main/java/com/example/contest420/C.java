package com.example.contest420;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var n = sc.nextInt();
        var q = sc.nextInt();

        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        long[] b = new long[n];
        long[] min = new long[n];
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
            if (a[i] > b[i]) {
                min[i] = b[i];
            } else {
                min[i] = a[i];
            }
        }

        long total = 0;
        for (var value : min) {
            total += value;
        }

        for (int i = 0; i < q; i++) {
            var v = sc.next();
            var index = sc.nextInt() - 1;
            var replace = sc.nextInt();
            if (v.equals("A")) {
                a[index] = replace;
            } else {
                b[index] = replace;
            }
            var before = min[index];
            var after = a[index] > b[index] ? b[index] : a[index];
            min[index] = after;
            total = total - before + after;
            System.out.println(total);
        }
    }
}
