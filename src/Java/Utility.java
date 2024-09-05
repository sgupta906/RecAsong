// src/Java/Utility.java
package Java;  // Add this line

public class Utility {
    public static void main(String[] args) {
        if (args.length > 0) {
            System.out.println("Received input: " + args[0]);
        } else {
            System.out.println("No input provided.");
        }
    }
}