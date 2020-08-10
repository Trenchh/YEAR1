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
public class isEven {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[] test = {1,2,3,4,5,6,7,8,9,10};
        for(int i = 0; i < test.length; i++) {
            isEven(test[i]);
        }
        
    }
    
    public static boolean isEven(int x) {
        boolean outcome = false;
        if (x % 2 == 0) {
            outcome = true;
        }
        System.out.println(outcome);
        return outcome;
    }
    
}
