package pl.agh.edu.dp.labirynth;

public class MazeFactory {
    private static MazeFactory instance;

    protected MazeFactory() {}

    public static MazeFactory getInstance() {
        if (instance == null) {
            instance = new MazeFactory();
        }
        return instance;
    }

    public Room createRoom(int number) {
        return new Room(number);
    }

    public Wall createWall() {
        return new Wall();
    }

    public Door createDoor(Room r1, Direction enter, Room r2, Direction exit) {
        return new Door(r1, enter, r2, exit);
    }
}
