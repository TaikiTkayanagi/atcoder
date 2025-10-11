package com.example.contest422;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var t = Integer.valueOf(sc.nextLine());
        for (int i = 0; i < t; i++) {
            var line = sc.nextLine().split(" ");
            int a = Integer.valueOf(line[0]);
            int b = Integer.valueOf(line[1]);
            int c = Integer.valueOf(line[2]);
            if (a == b && b == c) {
                System.out.println(a);
                continue;
            }
            if (b >= a || b >= c) {
                System.out.println(a > c ? c : a);
                continue;
            }
            int count = b;
            a -= b;
            c -= b;
            if (a >= c) {
                count += Math.ceil(a / 2);
            } else {
                count += Math.ceil(c / 2);
            }
            System.out.println(count);

        }
        sc.close();
    }
}
