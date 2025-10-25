package com.example.contest428;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var lines = sc.nextLine().split(" ");

        int s = Integer.valueOf(lines[0]);
        int a = Integer.valueOf(lines[1]);
        int b = Integer.valueOf(lines[2]);
        int x = Integer.valueOf(lines[3]);

        int r = 0;
        int run = 0;
        while (x > 0) {
            r += s;
            x -= 1;
            run++;
            if (a == run) {
                x -= b;
                run = 0;
            }
        }
        System.out.println(r);
    }
}
