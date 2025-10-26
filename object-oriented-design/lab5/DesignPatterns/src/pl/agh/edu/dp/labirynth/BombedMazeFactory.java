package pl.agh.edu.dp.labirynth;

public class BombedMazeFactory extends MazeFactory {
    private static BombedMazeFactory instance;

    private BombedMazeFactory() {}

    public static BombedMazeFactory getInstance() {
        if (instance == null) {
            instance = new BombedMazeFactory();
        }
        return instance;
    }

    @Override
    public Wall createWall() {
        return new BombedWall();
    }

    @Override
    public Room createRoom(int number) {
        return new BombedRoom(number);
    }
}