package com.example.contest422;

import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var str = sc.nextLine();
        var split = str.split("-");
        if (split[1].equals("8")) {
            split[0] = String.valueOf(Integer.valueOf(split[0]) + 1);
            split[1] = "1";
        } else {
            split[1] = String.valueOf(Integer.valueOf(split[1]) + 1);
        }
        System.out.println(split[0] + "-" + split[1]);
        sc.close();
    }
}
