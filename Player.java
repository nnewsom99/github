
public class Player {
	private String player_name;
	private char spot;
	
	//constructor
	Player(char marker){
		this.spot = marker;
	}
	
	//methods
	void setName(String name) {
		this.player_name = name;
	}
	
	String getName() {
		return player_name;
	}
	char getSpot() {
		return spot;
	}
}
