/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package selfassessment;

import java.util.Scanner;

/**
 *
 * @author undea
 */
public class Input {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int count = 0;

        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.println("Enter a word: ");
        String n = reader.next();
        n = n.toLowerCase();
        for (int i = 0; i < n.length(); i++) {
            char t = n.charAt(i);
            switch (t) {
                case 'a':
                    count++;
                    break;
                case 'e':
                    count++;
                    break;
                case 'i':
                    count++;
                    break;
                case 'o':
                    count++;
                    break;
                case 'u':
                    count++;
                    break;
                default:
                    break;
            }
        }
        System.out.println("There are " + count + " vowels");
    }

}
