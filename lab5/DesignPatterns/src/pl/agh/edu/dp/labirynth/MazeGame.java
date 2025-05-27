package pl.agh.edu.dp.labirynth;

public class MazeGame {
    public Maze createMaze1(MazeBuilder builder) {

        builder.buildRoom(1);
        builder.buildRoom(2);
        builder.setAdjacent(1, Direction.North, 2);

        builder.buildWall(1, Direction.North);
        builder.buildWall(1, Direction.East);
        builder.buildWall(1, Direction.South);
        builder.buildWall(1, Direction.West);

        builder.buildWall(2, Direction.North);
        builder.buildWall(2, Direction.East);
        builder.buildWall(2, Direction.South);
        builder.buildWall(2, Direction.West);


        builder.buildDoor(1, 2);

        return builder.getMaze();
    }
}
