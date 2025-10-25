package com.example.contest428;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);

        var q = Integer.valueOf(sc.nextLine());

        var sb = new StringBuilder(q);
        int count = 0;
        int falseIndex = -1;
        for (int i = 0; i < q; i++) {
            var query = sc.nextLine();
            if (query.charAt(0) == '1') {
                var l = query.charAt(2);
                if (l == '(') {
                    count++;
                } else {
                    count--;
                }
                sb.append(l);
                if (falseIndex == -1 && count < 0) {
                    falseIndex = sb.length() - 1;
                }
            } else {
                if (sb.length() != 0) {
                    var last = sb.length() - 1;
                    var l = sb.charAt(last);
                    if (l == '(') {
                        count--;
                    } else {
                        count++;
                    }
                    sb.deleteCharAt(last);
                    if (falseIndex == last) {
                        falseIndex = -1;
                    }
                }
            }
            if (falseIndex != -1) {
                System.out.println("No");
                continue;
            }
            System.out.println(count == 0 ? "Yes" : "No");
        }
    }
}
