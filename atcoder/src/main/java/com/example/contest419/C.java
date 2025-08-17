package com.example.contest419;

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt();

        long maxX = Long.MIN_VALUE;
        long minX = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            long y = sc.nextLong();
            if (x > maxX)
                maxX = x;
            if (minX > x)
                minX = x;
            if (y > maxY)
                maxY = y;
            if (minY > y)
                minY = y;
        }

        var x = maxX - minX;
        var y = maxY - minY;
        System.out.println(x > y ? (x + 1) / 2 : (y + 1) / 2);

        sc.close();
    }

}
