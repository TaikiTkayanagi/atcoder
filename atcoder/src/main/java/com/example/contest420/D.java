package com.example.contest420;

import java.util.ArrayDeque;
import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var h = sc.nextInt();
        var w = sc.nextInt();

        int[] start = new int[4];
        var table = new String[h][w];
        for (int i = 0; i < h; i++) {
            var a = sc.next().split("");
            for (int j = 0; j < w; j++) {
                table[i][j] = a[j];
                if (a[j].equals("S")) {
                    start[0] = i;
                    start[1] = j;
                    start[2] = 0;
                    start[3] = 0;
                }
            }
        }

        var queue = new ArrayDeque<int[]>();
        queue.add(start);
        int[] distRow = { 0, 0, -1, 1 };
        int[] distCol = { -1, 1, 0, 0 };
        int[][][] memo = new int[2][h][w];
        var result = -1;
        while (!queue.isEmpty()) {
            var poll = queue.poll();
            int row = poll[0];
            int col = poll[1];
            int count = poll[2];
            int onOrOff = poll[3];

            if (table[row][col].equals("G")) {
                result = count;
                break;
            } else if (table[row][col].equals("?")) {
                onOrOff ^= 1;
            }

            for (int i = 0; i < 4; i++) {
                int nextRow = row + distRow[i];
                int nextCol = col + distCol[i];
                if (nextRow >= h || nextRow < 0 || nextCol >= w || nextCol < 0) {
                    continue;
                }
                String notPass = onOrOff == 0 ? "x" : "o";
                if (table[nextRow][nextCol].equals(notPass) || table[nextRow][nextCol].equals("#")) {
                    continue;
                }
                if (memo[onOrOff][nextRow][nextCol] != 0) {
                    continue;
                }
                int[] add = { nextRow, nextCol, count + 1, onOrOff };
                queue.addLast(add);
                memo[onOrOff][nextRow][nextCol]++;
            }
        }
        System.out.println(result);
        sc.close();
    }
}
