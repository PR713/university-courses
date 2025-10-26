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


        // W metodzie main() dodajemy:
        System.out.println("\n=== Test BombedMazeFactory ===");

        BombedMazeFactory bombedFactory = BombedMazeFactory.getInstance();
        Room bombedRoom = bombedFactory.createRoom(3);
        Wall bombedWall = bombedFactory.createWall();

        bombedRoom.Enter();
        ((BombedWall) bombedWall).explode();
        bombedWall.Enter();


        // Test Singletonu dla podstawowej fabryki
        MazeFactory factory1 = MazeFactory.getInstance();
        MazeFactory factory2 = MazeFactory.getInstance();
        System.out.println("Czy to ta sama fabryka? " + (factory1 == factory2)); // true

        // Test Singletonu dla magicznej fabryki (teraz z Builderem)
        EnchantedMazeFactory enchanted1 = new EnchantedMazeFactory.Builder()
                .withSpell("Abrakadabra")
                .build();
        EnchantedMazeFactory enchanted2 = EnchantedMazeFactory.getInstance();
        System.out.println("Czy to ta sama magiczna fabryka? " + (enchanted1 == enchanted2)); // true
        System.out.println("Zaklęcie: " + enchanted1.getSpell()); // "Abrakadabra"

        // Próba zmiany zaklęcia (nie zadziała - singleton)
        EnchantedMazeFactory enchanted3 = new EnchantedMazeFactory.Builder()
                .withSpell("Hokus Pokus")
                .build(); // zwróci tę samą instancję
        System.out.println("Czy to ta sama instancja? " + (enchanted1 == enchanted3)); // true
        System.out.println("Zaklęcie: " + enchanted3.getSpell()); // Nadal "Abrakadabra"

        // Test Singletonu dla bombowej fabryki
        BombedMazeFactory bombed1 = BombedMazeFactory.getInstance();
        BombedMazeFactory bombed2 = BombedMazeFactory.getInstance();
        System.out.println("Czy to ta sama bombowa fabryka? " + (bombed1 == bombed2)); // true


        // Test 4.4 - Poruszanie się po labiryncie
        System.out.println("\n=== Test poruszania się po labiryncie ===");

        MazeGame game = new MazeGame();
        MazeFactory factory3 = new EnchantedMazeFactory.Builder()        //BombedMazeFactory.getInstance()
                .withSpell("Lumos Maxima")
                .build();

        StandardBuilderMaze builder3 = new StandardBuilderMaze();
        Maze maze3 = game.createInterestingMaze(builder3, factory3);

        Player player = new Player(maze3, 1);
        player.play();
    }
}



