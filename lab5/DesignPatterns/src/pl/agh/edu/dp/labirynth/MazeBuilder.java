package pl.agh.edu.dp.labirynth;

public interface MazeBuilder {
    void buildRoom(int roomNumber);
    void buildDoor(int roomFrom, int roomTo);
    void buildWall(int roomFrom, Direction direction);
    void setAdjacent(int roomFrom, Direction entrance, int roomTo);
    Maze getMaze();
}
