package com.example.contest422;

import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var oneline = sc.nextLine().split(" ");
        var row = Integer.valueOf(oneline[0]);
        var col = Integer.valueOf(oneline[1]);

        Character[][] tables = new Character[row][col];
        for (int i = 0; i < row; i++) {
            var line = sc.nextLine();
            for (int j = 0; j < col; j++) {
                tables[i][j] = line.charAt(j);
            }
        }

        var result = "Yes";
        for (int i = 0; i < row; i++) {
            if (result.equals("No")) {
                break;
            }
            for (int j = 0; j < col; j++) {
                var c = tables[i][j];
                if (c == '.') {
                    continue;
                }

                int count = 0;
                if (i - 1 >= 0 && tables[i - 1][j].equals(c)) {
                    count++;
                }

                if (i + 1 < row && tables[i + 1][j].equals(c)) {
                    count++;
                }

                if (j - 1 >= 0 && tables[i][j - 1].equals(c)) {
                    count++;
                }

                if (j + 1 < col && tables[i][j + 1].equals(c)) {
                    count++;
                }

                if (count != 2 && count != 4) {
                    result = "No";
                    break;
                }
            }
        }
        sc.close();
        System.out.println(result);
    }
}
