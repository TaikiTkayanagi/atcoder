package com.example.contest427;

import java.util.Scanner;

public class B {
    private static int f(int i) {
        var r = 0;
        double iterator = (double) i;
        while (iterator >= 1) {
            r += iterator % 10;
            iterator /= 10;
        }
        return r;
    }

    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var count = sc.nextInt();

        var r = 1;
        for (int i = 0; i < count; i++) {
            if (i == 0) {
                continue;
            }
            r += f(r);
        }
        System.out.println(r);
    }
}
