import java.util.Scanner;
//This uses a Player class and a Board class to play one round of Tic Tac Toe
public class Playgame {
	//2 player objects
    static Player p1 = new Player('X');
    static Player p2 = new Player('O');
	
	public static void main(String[] args) {
		// This method plays the game

		System.out.println("Enter Player 1 name: ");
		Scanner sc1 = new Scanner(System.in);
		p1.setName(sc1.nextLine());
		//System.out.println(p1.getName());
		
		System.out.println("Enter Player 2 name: ");
		p2.setName(sc1.nextLine());

		//System.out.println(p2.getName());
		
		Board board = new Board();
		board.printBoard();
		
			while(true) {
				//Player 1 turn
				if(board.hasWinner()) {
					System.out.println(p2.getName() +" is winner!");
					break;
				}
				if(board.isTied()) {
					System.out.println("Game tied");
					break;
				}
				System.out.println(p1.getName() + " chose a number:");
				int selection = sc1.nextInt();
				
				while(board.isTaken(selection)) {
					board.printBoard();
					selection = sc1.nextInt();
				}
				
				board.replace((char)(selection + '0'), p1.getSpot());
				
				//Player 2 turn
				if(board.hasWinner()) {
					System.out.println(p1.getName() + " is winner!");
					break;
				}
				if(board.isTied()) {
					System.out.println("Game Tied!");
					break;
				}
				System.out.println(p2.getName() + " chose a number");
				
				selection = sc1.nextInt();
				while(board.isTaken(selection)) {
					board.printBoard();
					selection = sc1.nextInt();
				}
				board.replace((char)(selection + '0'), p2.getSpot());
			}
			sc1.close();
		}//end main
	}


