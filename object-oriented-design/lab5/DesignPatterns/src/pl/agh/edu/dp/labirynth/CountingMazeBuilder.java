package pl.agh.edu.dp.labirynth;

import java.util.HashMap;
import java.util.Map;

public class CountingMazeBuilder implements MazeBuilder {
    private final Map<String, Integer> counts;

    public CountingMazeBuilder() {
        this.counts = new HashMap<>();
        this.counts.put("Rooms", 0);
        this.counts.put("Walls", 0);
        this.counts.put("Doors", 0);
    }

    @Override
    public void buildRoom(int roomNumber) {
        counts.put("Rooms", counts.get("Rooms") + 1);
    }

    @Override
    public void buildDoor(int roomFrom, int roomTo) {
        counts.put("Doors", counts.get("Doors") + 1);
    }

    @Override
    public void buildWall(int roomNumber, Direction direction) {
        counts.put("Walls", counts.get("Walls") + 1);
    }

    @Override
    public Map<String, Integer> GetCounts() {
        return new HashMap<>(counts); // Zwracamy kopię
    }

    @Override
    public Maze getMaze() {
        return null; // Nie tworzymy faktycznego labiryntu
    }

    @Override
    public void setAdjacent(int room1, Direction dir1, int room2) {
        // Nie potrzebujemy implementacji dla zliczania
    }
}
