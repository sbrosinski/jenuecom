---
title: Answer To Abecedarian 
date: "2022-04-03"
---

So with a lot of tears and sweat and HELP I've finally completed the 
Abecedarian exercise. I have a long way to go, but onto the 
next chapter. 


```java
package com.jenue;

import java.util.Scanner;

public class Abecedarian {

    public static void main(String[] args) {
        String word;
        do {
            System.out.print("Enter word: ");

            Scanner in = new Scanner(System. in);
            word = in.nextLine();
            System.out.println(word.length());

        } while (word.length()<1);

        boolean result=isAbecedarian(word.toLowerCase());

        System.out.println(result);
    }

    public static boolean isAbecedarian(String word) {
        boolean result = true;
        char previousChar =  ' ';
        for(int i = 0; i < word.length() && result; i++) {
            char currentChar = word.charAt(i);
            result = currentChar>previousChar;
            previousChar = currentChar;
        }

        return result;
    }
}
```

