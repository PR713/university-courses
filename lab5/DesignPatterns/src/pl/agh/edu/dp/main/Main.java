package pl.agh.edu.dp.main;

import pl.agh.edu.dp.labirynth.*;

import java.util.Map;

public class Main {

    public static void main(String[] args) {
        ///////////////////////4.1 budowniczy:
        MazeGame mazeGame = new MazeGame();
        MazeBuilder builder = new StandardBuilderMaze();
        Maze maze = mazeGame.createMaze1(builder);

        System.out.println(maze.getRoomNumbers());

        MazeGame mazeGame1 = new MazeGame();

        // Test CountingMazeBuilder
        CountingMazeBuilder counter = new CountingMazeBuilder();
        mazeGame1.createMaze1(counter);

        Map<String, Integer> counts = counter.GetCounts();
        System.out.println("Elementy labiryntu:");
        System.out.println("Pokoje: " + counts.get("Rooms"));
        System.out.println("Ściany: " + counts.get("Walls"));
        System.out.println("Drzwi: " + counts.get("Doors"));


        /////////////////////////////// 4.2 fabryka abstrakcyjna:

        MazeFactory factory = new EnchantedMazeFactory.Builder()
                .withSpell("Brawo! Potrafisz latać przez minutę!")
                .build();

        Room room = factory.createRoom(1);
        room.Enter();
    }
}



