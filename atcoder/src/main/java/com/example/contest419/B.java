package com.example.contest419;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int queryCount = sc.nextInt();

        int[] bag = new int[101];
        for (int i = 0; i < queryCount; i++) {
            var type = sc.nextInt();
            if (type == 1) {
                int v = sc.nextInt();
                bag[Integer.valueOf(v)]++;
            } else {
                for (int j = 1; j <= 100; j++) {
                    if (bag[j] > 0) {
                        bag[j]--;
                        System.out.println(j);
                        break;
                    }
                }
            }
        }
        sc.close();
    }
}
