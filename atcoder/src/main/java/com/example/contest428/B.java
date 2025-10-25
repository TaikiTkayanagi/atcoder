package com.example.contest428;

import java.util.Scanner;
import java.util.TreeMap;

public class B {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var line = sc.nextLine().split(" ");
        var n = Integer.valueOf(line[0]);
        var k = Integer.valueOf(line[1]);
        var s = sc.nextLine();

        var last = n - k + 1;
        var map = new TreeMap<String, Integer>();
        int max = 1;
        for (int i = 0; i < last; i++) {
            var t = i + k;
            var sub = s.substring(i, t);
            if (map.containsKey(sub)) {
                var next = map.get(sub) + 1;
                if (next > max) {
                    max = next;
                }
                map.put(sub, next);
            } else {
                map.put(sub, 1);
            }
        }
        System.out.println(max);
        for (var entry : map.entrySet()) {
            if (entry.getValue() == max) {
                System.out.print(entry.getKey());
                System.out.print(" ");
            }
        }
    }
}
