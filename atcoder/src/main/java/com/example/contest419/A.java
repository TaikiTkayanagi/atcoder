package com.example.contest419;

import java.util.HashMap;
import java.util.Scanner;

public class A {
    public static void main(String[] args) {

        var sc = new Scanner(System.in);
        var s = sc.next();
        sc.close();

        var memo = new HashMap<String, String>();
        memo.put("red", "SSS");
        memo.put("blue", "FFF");
        memo.put("green", "MMM");

        if (memo.containsKey(s)) {
            System.out.println(memo.get(s));
        } else {
            System.out.println("Unknown");
        }
    }
}
