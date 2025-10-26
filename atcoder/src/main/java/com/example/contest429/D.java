package com.example.contest429;

import java.util.Arrays;
import java.util.Scanner;

public class D {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var oneLines = sc.nextLine().split(" ");
        var secondLines = sc.nextLine().split(" ");
        var N = Integer.valueOf(oneLines[0]);
        var M = Long.valueOf(oneLines[1]);
        var C = Integer.valueOf(oneLines[2]);
        long[] A = new long[N];

        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(secondLines[i]);
        }

        Arrays.sort(A); // A.sort()

        // A2 = A + (A[i] + M)
        long[] A2 = new long[2 * N];
        for (int i = 0; i < N; i++) {
            A2[i] = A[i];
            A2[i + N] = A[i] + M;
        }

        long r = 0; // 右端ポインタ
        long total = 0; // 現在見ている人数
        long sumDist = 0; // 答えの合計

        // しゃくとり法
        for (int i = 0; i < N; i++) {
            while (total < C) {
                total++;
                r++;
            }
            sumDist += (A2[(int) r - 1] - A2[i]);
            total--; // i の人を抜けるので人数を1減らす
        }

        System.out.println(sumDist);
    }
}
