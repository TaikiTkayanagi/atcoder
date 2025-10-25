package com.example.contest427;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var oneLine = sc.nextLine().split(" ");
        int n = Integer.valueOf(oneLine[0]);
        int m = Integer.valueOf(oneLine[1]);

        var map = new HashMap<Integer, ArrayList<Integer>>();

        for (int i = 0; i < m; i++) {
            var line = sc.nextLine().split(" ");
            int from = Integer.valueOf(line[0]);
            int to = Integer.valueOf(line[1]);
            if (map.containsKey(from)) {
                map.get(from).add(to);
            } else {
                var list = new ArrayList<Integer>();
                list.add(to);
                map.put(from, list);
            }
        }

        String[] status = new String[n];
        var queue = new ArrayDeque<Integer>();
        while (!queue.isEmpty()) {
            var pop = queue.poll();
            var list = map.get(pop);

        }
    }
}
