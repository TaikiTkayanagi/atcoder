package com.example.contest420;

import java.util.ArrayList;
import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] votes = new int[n][m];

        for (int i = 0; i < n; i++) {
            var line = sc.next().split("");
            for (int j = 0; j < m; j++) {
                votes[i][j] = Integer.valueOf(line[j]);
            }
        }

        var total = new int[n];
        int max = 0;
        for (int i = 0; i < m; i++) {
            var zeroList = new ArrayList<Integer>();
            var oneList = new ArrayList<Integer>();
            for (int j = 0; j < n; j++) {
                var vote = votes[j][i];
                if (vote == 1) {
                    oneList.add(j);
                } else {
                    zeroList.add(j);
                }
            }

            ArrayList<Integer> iterator;
            if (zeroList.size() == n || oneList.size() == n) {
                iterator = zeroList.size() == 0 ? oneList : zeroList;
            } else if (zeroList.size() > oneList.size()) {
                iterator = oneList;
            } else {
                iterator = zeroList;
            }
            for (int who : iterator) {
                total[who]++;
                if (total[who] > max) {
                    max = total[who];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (total[i] == max) {
                System.out.print(i + 1 + " ");
            }
        }
        sc.close();
    }
}
