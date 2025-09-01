package com.example.contest421;

import java.util.ArrayList;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var n = Integer.valueOf(sc.nextLine());
        var s = sc.nextLine();
        sc.close();

        // Aスタート
        var aMemo1 = new ArrayList<Integer>();
        var bMemo1 = new ArrayList<Integer>();
        // Bスタート
        var aMemo2 = new ArrayList<Integer>();
        var bMemo2 = new ArrayList<Integer>();
        for (int i = 0; i < n * 2; i++) {
            if (s.charAt(i) == 'A') {
                if (i % 2 == 0) {
                    aMemo2.add(i);
                } else {
                    aMemo1.add(i);
                }
            } else if (s.charAt(i) == 'B') {
                if (i % 2 == 0) {
                    bMemo1.add(i);
                } else {
                    bMemo2.add(i);
                }
            }
        }

        long count1 = 0;
        long count2 = 0;
        for (int i = 0; i < aMemo1.size(); i++) {
            int a = aMemo1.get(i);
            int b = bMemo1.get(i);
            count1 += Math.abs(a - b);
        }
        for (int i = 0; i < aMemo2.size(); i++) {
            int a = aMemo2.get(i);
            int b = bMemo2.get(i);
            count2 += Math.abs(a - b);
        }
        System.out.println(Math.min(count1, count2));
    }
}
