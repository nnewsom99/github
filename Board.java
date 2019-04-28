
public class Board {
	char b[][] = new char[3][3];
	
	public Board() {//constructor
		newBoard();
	}
	
	//methods
	public void newBoard() {
		b[0][0] = '1';
		b[0][1] = '2';
		b[0][2] = '3';
		b[1][0] = '4';
		b[1][1] = '5';
		b[1][2] = '6';
		b[2][0] = '7';
		b[2][1] = '8';
		b[2][2] = '9';
	}
	public void replace(char spot, char mark) {
	
			switch(spot) {
			case '1':b[0][0] = mark; break;
			case '2':b[0][1] = mark; break;
			case '3':b[0][2] = mark; break;
			case '4':b[1][0] = mark; break;
			case '5':b[1][1] = mark; break;
			case '6':b[1][2] = mark; break;
			case '7':b[2][0] = mark; break;
			case '8':b[2][1] = mark; break;
			case '9':b[2][2] = mark; break;
			}
			printBoard();
	}
	public void printBoard() {
		for (int i = 0; i < 3; i++) {
			System.out.println("| "+b[i][0]+" | "+b[i][1]+" | "+b[i][2]+" |");
			if(i != 2)
				System.out.println("-------------");
		}
	}
	
	public boolean isValid(int choice) {
		return choice <=9 && choice >=1;
	}
	
	public boolean isTaken(int choice) {
		//returns true is the selection is invalid or taken
		//returns false if the spot has not been previously selected
		if(!isValid(choice)) {
			System.out.println("Not a valid input. Try again");
			return true;
		}
		//calculate what row or column the number is located
		int row = (choice - 1)/3;
		int column = (choice -1 )%3;
		char spot = b[row][column];
		return (spot=='X' || spot=='O');
	}
	
	public boolean isTied() {
		int count = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if(b[i][j] == 'X' || b[i][j] == 'O') {
					count++;
				}
			}
		}
		return count==9;
	}
	
	public boolean hasWinner() {
		//returns true is there is a winner
		//returns false if no winner
		return((b[0][0]==b[0][1] && b[0][1]==b[0][2])||
			(b[1][0]==b[1][1] && b[1][1]==b[1][2])||
			(b[2][0]==b[2][1] && b[2][1]==b[2][2])||
			(b[0][0]==b[1][0] && b[2][0]==b[1][0])||
			(b[1][0]==b[1][1] && b[1][1]==b[1][2])||
			(b[2][0]==b[2][1] && b[2][1]==b[2][2])||
			(b[0][0]==b[1][1] && b[1][1]==b[2][2])||
			(b[2][0]==b[1][1] && b[1][1]==b[0][2]));
	}
}
