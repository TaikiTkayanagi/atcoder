package com.example.contest420;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var x = sc.nextInt();
        var y = sc.nextInt();

        var ans = (x + y) % 12;

        System.out.println(ans == 0 ? "12" : ans);

        sc.close();
    }
}
