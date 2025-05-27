package pl.agh.edu.dp.labirynth;

import java.util.Map;

public interface MazeBuilder {
    void buildRoom(int roomNumber);
    void buildDoor(int roomFrom, int roomTo);
    void buildWall(int roomFrom, Direction direction);
    void setAdjacent(int roomFrom, Direction entrance, int roomTo);
    Map<String, Integer> GetCounts();
    Maze getMaze();
}
