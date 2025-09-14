package com.example.contest423;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.nextLine());
        String[] l = sc.nextLine().split(" ");

        int left = 0;
        int right = n;
        int count = 2;
        while (left < right) {
            if (l[left].equals("1") && l[right - 1].equals("1")) {
                break;
            }
            String leftKey = l[left];
            String rightKey = l[right - 1];
            if (leftKey.equals("0")) {
                left++;
                if (left != right) {
                    count++;
                }
            }
            if (rightKey.equals("0")) {
                right--;
                if (left != right) {
                    count++;
                }
            }
        }
        System.out.println(n + 1 - count);
        sc.close();
    }
}
