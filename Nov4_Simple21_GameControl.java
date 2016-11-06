package Simple21;

import java.util.Scanner;
import java.util.Random;

/**
 * This is a simplified version of a common card game, "21".<p>
 * In this game, the dealer deals two "cards" to each player,
 * one hidden, so that only the player who gets the card knows
 * what it is, and one face up, so that everyone can see it.
 * (Actually, what the other players see is the <i>total</i>
 * of each other player's visible cards, not the individual cards.)<p>
 *
 * The players then take turns requesting cards, trying to get
 * as close to 21 as possible, but not going over 21. These cards
 * will be visible to all players.  A player may pass (ask for no
 * more cards). Once a player has passed, he or she cannot later
 * ask for another card. When all players have passed, the
 * game ends.<p>
 *
 * The winner is the player who has come closest to 21 without
 * exceeding it. In the case of a tie, or if everyone goes over
 * 21, no one wins.<p>
 *
 * In this program, there are some number of computer players
 * and one human player. The game is only played once. 
 * 
 * @author David Matuszek
 * @author (Students: Ting-Chun Yeh) 
 * @version 0
 */
public class GameControl {
    
    /** All the Player objects, including the Human player.
     * The number of players is set here; other places in the
     * program should use <code>players.length</code>. */
    Player[] players = new Player[4];
    
    /** passed[i] == true indicates that players[i] has passed. */
    boolean[] passed = new boolean[] {false, false, false, false};
    
    /** Used for getting input from the user. */
    Scanner scanner = new Scanner(System.in);
    
    /** A random number generator. */
    Random random = new Random();
      
    /**
     * The main method just creates a GameControl object and calls
     * its <code>run</code> method.
     * 
     * @param args Not used.
     */
    public static void main(String args[]) {    
    	new GameControl().run();
    }
    
    /**
     * Prints a welcome method, then calls methods to perform each
     * of the following actions:
     * <ol>
     *   <li>Create the Players (one of them a Human),</li>
     *   <li>Deal the initial two cards to each player,</li>
     *   <li>Control the play of the game, and</li>
     *   <li>Print the final results.</li>
     * </ol>
     */
    void run() { 
    	System.out.println("Welcome to the game of 21!");
    	this.createPlayers();
    	this.deal();
    	this.controlPlay();
    	this.printResults();
    }
    
    /**
     * Asks the human player for a name, and then creates a Human
     * object and all the other Player objects, saving them in the
     * <code>players</code> array. (Names of the other players may
     * be hardwired; don't ask the user for them.)
     */
    void createPlayers() {
        System.out.print("What is your name?  ");
        String humansName = scanner.next();
        Human human = new Human(humansName);
        Player player1 = new Player("Manny");
        Player player2 = new Player("Moe");
        Player player3 = new Player("Jack");
        players[0] = human;
        players[1] = player1;
        players[2] = player2;
        players[3] = player3;
    }
    
    /**
     * Deals the initial two cards (one hidden, one not hidden)
     * to each player.
     */
    void deal() { 
       int visible = 0;
       int hidden = 0; 
       for (Player player : players) {
    	   visible = this.nextCard();
    	   hidden = this.nextCard();
    	   player.takeHiddenCard(hidden);
    	   player.takeVisibleCard(visible);
       }
       System.out.println("");
    }
    
    /**
     * Returns a random "card", represented by a integer between
     * 1 and 10, inclusive. The odds of returning a 10 are four
     * times as likely as any other value (because in an actual
     * deck of cards, 10, Jack, Queen, and King all count as 10).<br />
     * <b>Note:</b> The java.util package contains a <code>Random</code>
     * class, which is perfect for generating random numbers.
     *
     * @return a random integer in the range 1..10.
     */
    int nextCard() { 
        int rannum = random.nextInt(13) + 1;
        if (rannum > 10) {
        	rannum = 10;
        }
        return rannum;
    }

    /**
     * Gives each player in turn a chance to take a card, until all
     * players have passed. Prints a message when a player passes.
     * Once a player has passed, that player is not given another
     * chance to take a card.<br />
     * <b>Note:</b> The global array <code>passed</code> is used to
     * keep track of which players have passed.
     */
    void controlPlay() { 
        int index = 0;
    	while (index != players.length){
    		for (int i = 0; i < players.length; i++){
    			if (!passed[i]){
    				if (players[i].offerCard(players)) {
    					players[i].takeVisibleCard(this.nextCard());
    				}
    				else {
	            		System.out.println(players[i].name + " passes.");
	            		passed[i] = true;
	            		index++;
    				}
    			}
    		}
    	System.out.println("");
        }
       }    
    /**
     * Prints a summary at the end of the game, saying how many
     * points each player had, and who won.
     */
    void printResults() { 
        System.out.println("Game Over.");
        for (Player player : players){
        	System.out.println(player.name + " has " + player.getScore() + " points.");
        }
        int result = this.findWinningPlayer();
        if (result != -1){
        	System.out.println(players[result].name + " wins with " + players[result].getScore() + " points!");
        }
        else {
        	System.out.println("Nobody wins.");
        }
    }

    /**
     * Determines who won the game, and returns it as an index into
     * the players array.
     * 
     * @return The index of the winner, or -1 if nobody won.
     */
    int findWinningPlayer() { 
        int base = 0;
        int index = -1;
        int tie = 0;
    	for (int i = 0; i < players.length; i++){
    		if ((players[i].getScore() > base) && (players[i].getScore() < 22)){
        		base = players[i].getScore();
        		index = i;
        		tie = 0;
        	}
        	else if (players[i].getScore() == base){
        		tie = 1;
        	}
        }
    	if ((index != -1) && (tie == 0)){
    		return index;
    	}
    	else {
    		return -1;
    	}
    }
}
