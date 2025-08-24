package com.example.contest420;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class D {
    private static class QueueNode {
        public int[] info;
        public String[][] table;

        public QueueNode(int[] info, String[][] table) {
            this.info = info;
            this.table = table;
        }
    }

    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var h = sc.nextInt();
        var w = sc.nextInt();

        int[] start = new int[3];
        var table = new String[h][w];
        HashMap<String, ArrayList<int[]>> memo = new HashMap<>();
        for (int i = 0; i < h; i++) {
            var a = sc.next().split("");
            for (int j = 0; j < w; j++) {
                table[i][j] = a[j];
                if (a[j].equals("S")) {
                    start[0] = i;
                    start[1] = j;
                    start[2] = 0;
                } else if (a[j].equals("o")) {
                    int[] add = { i, j };
                    if (memo.containsKey(a[j])) {
                        memo.get(a[j]).add(add);
                    } else {
                        var array = new ArrayList<int[]>();
                        array.add(add);
                        memo.put(a[j], array);
                    }
                } else if (a[j].equals("x")) {
                    int[] add = { i, j };
                    if (memo.containsKey(a[j])) {
                        memo.get(a[j]).add(add);
                    } else {
                        var array = new ArrayList<int[]>();
                        array.add(add);
                        memo.put(a[j], array);
                    }
                }
            }
        }

        var queue = new ArrayDeque<QueueNode>();
        queue.add(new QueueNode(start, table.clone()));
        while (!queue.isEmpty()) {
            var node = queue.poll();
            var position = node.info;
            int row = position[0];
            int col = position[1];
            int count = position[2];
            var virtualTable = node.table;

            if (virtualTable[row][col].equals("G")) {
                System.out.println(count);
                break;
            } else if (virtualTable[row][col].equals("?")) {

                var openList = memo.get("o");
                var closeList = memo.get("x");
                virtualTable = virtualTable.clone();
                for (int[] value : openList) {
                    virtualTable[value[0]][value[1]] = "x";
                }
                for (int[] value : closeList) {
                    virtualTable[value[0]][value[1]] = "o";
                }
            }

            if (row + 1 < h && !virtualTable[row + 1][col].equals("x") && !virtualTable[row + 1][col].equals("#")) {
                int[] add = { row + 1, col, count + 1 };
                queue.addLast(new QueueNode(add, virtualTable));
            }

            if (row - 1 >= 0 && !virtualTable[row - 1][col].equals("x") && !virtualTable[row - 1][col].equals("#")) {
                int[] add = { row - 1, col, count + 1 };
                queue.addLast(new QueueNode(add, virtualTable));
            }

            if (col + 1 < w && !virtualTable[row][col + 1].equals("x") && !virtualTable[row][col + 1].equals("#")) {
                int[] add = { row, col + 1, count + 1 };
                queue.addLast(new QueueNode(add, virtualTable));
            }

            if (col - 1 >= 0 && !virtualTable[row][col - 1].equals("x") && !virtualTable[row][col - 1].equals("#")) {
                int[] add = { row, col - 1, count + 1 };
                queue.addLast(new QueueNode(add, virtualTable));
            }
        }
    }
}
