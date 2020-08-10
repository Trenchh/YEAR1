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
public class TriangleAngleCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[] sides = input();
        for (int i = 0; i < sides.length; i++) {
            System.out.println(sides[i]);
        }
        double a = sides[0];
        System.out.println("-------------" + a);
        double b = sides[1];
        System.out.println("-------------" + b);
        double c = sides[2];
        System.out.println("-------------" + c);
        System.out.println(Math.toDegrees(Math.asin(a / c))); //NOT WORKINGGG
        System.out.println(Math.toDegrees(Math.acos(b / c)));
        System.out.println(Math.toDegrees(Math.atan(a / b)));
    }

    public static int[] input() {
        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.println("Enter 1st leg length: ");
        int a = reader.nextInt();
        System.out.println("Enter 2nd leg length: ");
        int b = reader.nextInt();
        System.out.println("Enter hypotenuse length: ");
        int c = reader.nextInt();
        int[] values = {a, b, c};
        return values;
    }

}
