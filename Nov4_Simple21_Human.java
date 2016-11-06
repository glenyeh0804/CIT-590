package Simple21;

import java.util.Scanner;

/**
 * Represents the human player in a game of Simple 21.
 * @author David Matuszek
 */
public class Human extends Player {
    Scanner scanner = new Scanner(System.in);
    
    /**
     * Constructs a Human object to represent the user.
     * 
     * @param name The name of the user.
     */
    Human(String name) {
        super(name);
    }
    
    /**
     * Asks the user whether to take another card.
     * 
     * @param players Ignored.
     */
    @Override
    boolean offerCard(Player[] players) {
        showVisibleCards(players);
        return getYesOrNo("Take another card?");
    }
    
    /**
     * Takes a card that is not visible to the other players.
     * Overrides the method in Player so that the card value
     * can be displayed.
     * @param card The card taken.
     * @see simple21CompleteInteractive.Player#takeHiddenCard(int)
     */
    @Override
    void takeHiddenCard(int card) {
        super.takeHiddenCard(card);
        System.out.println("  (It's a " + card + ")");
    }

    /**
     * Returns a boolean response to a yes-no question.
     * 
     * @param question The question to be asked.
     * @return The answer to the question.
     */
    private boolean getYesOrNo(String question) {
        String answer;
        while (true) {
            System.out.print(question + "  ");
            answer = scanner.next();
            if (answer.toLowerCase().charAt(0) == 'y')
                return true;
            if (answer.toLowerCase().charAt(0) == 'n')
                return false;
        }
    }
    
    /**
     * Prints the sum of the visible cards for each player.
     * 
     * @param players The array of Players.
     */
    void showVisibleCards(Player[] players) {
        System.out.print("Visible cards: ");
        for (Player player : players) {
            System.out.print(player.name + " " + player.sumOfVisibleCards + "   ");
        }
        System.out.println();
    }
}
