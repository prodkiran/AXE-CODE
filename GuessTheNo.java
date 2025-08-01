import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int secretNumber = random.nextInt(100) + 1; // random number between 1-100
        int attempts = 0;
        boolean hasGuessed = false;
        
        System.out.println("welcome to guess the number game!");
        System.out.println("i've picked a number between 1 and 100. can you guess it?");
        
        while (!hasGuessed) {
            System.out.print("Enter your guess: ");
            int guess = scanner.nextInt();
            attempts++;
            
            if (guess < secretNumber) {
                System.out.println("too low! try again.");
            } else if (guess > secretNumber) {
                System.out.println("too high! try again.");
            } else {
                hasGuessed = true;
                System.out.println(
                    "congratulations! you guessed the number in " + attempts + " attempts."
                );
            }
        }
        scanner.close();
    }
}
