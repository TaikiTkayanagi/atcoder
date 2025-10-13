package com.example.contest427;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var s = sc.nextLine();
        var l = (s.length() + 1) / 2;

        System.out.println(s.substring(0, l - 1) + s.substring(l, s.length()));
    }
}
