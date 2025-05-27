package pl.agh.edu.dp.main;

import pl.agh.edu.dp.labirynth.*;

import java.util.Map;

public class Main {

    public static void main(String[] args) {

        MazeGame mazeGame = new MazeGame();
        MazeBuilder builder = new StandardBuilderMaze();
        Maze maze = mazeGame.createMaze(builder);

        System.out.println(maze.getRoomNumbers());

        MazeGame mazeGame1 = new MazeGame();

        // Test CountingMazeBuilder
        CountingMazeBuilder counter = new CountingMazeBuilder();
        mazeGame1.createMaze(counter);

        Map<String, Integer> counts = counter.GetCounts();
        System.out.println("Elementy labiryntu:");
        System.out.println("Pokoje: " + counts.get("Rooms"));
        System.out.println("Ściany: " + counts.get("Walls"));
        System.out.println("Drzwi: " + counts.get("Doors"));
    }
}



