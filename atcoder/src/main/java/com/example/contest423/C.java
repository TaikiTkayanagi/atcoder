package com.example.contest423;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        String[] oneLine = sc.nextLine().split(" ");
        int n = Integer.valueOf(oneLine[0]);
        int r = Integer.valueOf(oneLine[1]);
        String[] doors = sc.nextLine().split(" ");

        int left = -1;
        int right = -1;
        for (int i = 0; i < doors.length; i++) {
            if (left == -1 && doors[i].equals("0")) {
                left = i;
            }
            if (doors[i].equals("0")) {
                right = i;
            }
        }

        int count = 0;
        if (r - 1 >= 0 && left != -1 && r - 1 >= left) {
            for (int i = r - 1; i > left; i--) {
                if (doors[i].equals("1")) {
                    count++;
                }
            }
            count += r - left;
        }

        if (r < doors.length && r <= right) {
            for (int i = r; i < right; i++) {
                if (doors[i].equals("1")) {
                    count++;
                }
            }
            count += right - r + 1;
        }
        System.out.println(count);
        sc.close();
    }
}
