package pl.agh.edu.dp.labirynth;

public class Door extends MapSite {
    private final Room room1;
    private final Room room2;
    private final Direction enter;
    private final Direction exit;

    public Door(Room r1, Direction enter, Room r2, Direction exit) {
        this.room1 = r1;
        this.room2 = r2;
        this.enter = enter;
        this.exit = exit;

    }


    @Override
    public void Enter(){

    }

    public Room getRoom1() {
        return room1;
    }

    public Room getRoom2() {
        return room2;
    }

    public Direction getEnter() {
        return enter;
    }

    public Direction getExit() {
        return exit;
    }
}
