package com.example.contest427;

import java.util.Scanner;

public class B {
    private static long f(int i) {
        long r = 0L;
        while (i > 0) {
            r += i % 10;
            i /= 10;
        }
        return r;
    }

    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var count = sc.nextInt();

        var r = 1;
        for (int i = 1; i < count; i++) {
            r += f(r);
        }
        System.out.println(r);
    }
}
