/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package selfassessment;

/**
 *
 * @author undea
 */
public class StringsAndLoops {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String test = "Test";
        
        for(int i = 0; i < test.length();) {
        System.out.println(test);
        test = cut(test);
        }
        }
    
    public static String cut(String x) {
        x = x.substring(0, x.length() - 1);
        return x;
    }
    
}
