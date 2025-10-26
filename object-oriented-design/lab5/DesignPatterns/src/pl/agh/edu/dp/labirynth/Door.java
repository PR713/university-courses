package pl.agh.edu.dp.labirynth;

public class Door extends MapSite {
    private final Room room1;
    private final Room room2;
    private final Direction enter;
    private final Direction exit;

    public Door(Room r1, Direction enterDir, Room r2, Direction exitDir) {
        if (r1.getNeighbour(enterDir) != r2 || r2.getNeighbour(exitDir) != r1) {
            throw new IllegalArgumentException("Door directions don't match room adjacency");
        } //podwójna walidacja w razie czego (CommonWall i tak waliduje)

        this.room1 = r1;
        this.room2 = r2;
        this.enter = enterDir;
        this.exit = exitDir;

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
