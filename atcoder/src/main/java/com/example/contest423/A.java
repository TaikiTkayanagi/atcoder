package com.example.contest423;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int x = sc.nextInt();
        int c = sc.nextInt();
        int last = 0;
        double fee = (double) c / 1000;
        for (int i = 1000; i <= x; i += 1000) {
            double f = i * fee;
            if (x < f + i) {
                break;
            }
            last = i;
        }
        System.out.println(last);
        sc.close();
    }
}
