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
public class SearchArray {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[] test = {23,12,32,43,56,67,8987,3453,23,89789,12,2345235,234};
        int high = 0;
        
        for(int i = 0; i < test.length; i++) {
            if( high <= test[i]) {
                high = test[i];
            }
        }
        System.out.println(high);
        
    }
    
}
