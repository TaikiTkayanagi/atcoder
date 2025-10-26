package com.example.contest429;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var line = sc.nextLine().split(" ");
        int n = Integer.valueOf(line[0]);
        int m = Integer.valueOf(line[1]);

        for (int i = 0; i < n; i++) {
            if (i < m) {
                System.out.println("OK");
            } else {
                System.out.println("Too Many Requests");
            }
        }
    }
}
