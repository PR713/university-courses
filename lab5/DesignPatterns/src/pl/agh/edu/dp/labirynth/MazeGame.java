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

    public Maze createInterestingMaze(MazeBuilder builder, MazeFactory factory) {
        for (int i = 1; i <= 5; i++) {
            builder.buildRoom(i);

            for (Direction dir : Direction.values()) {
                builder.buildWall(i, dir);
            }
        }

        // Pokój 1 - startowy, połączony z 2 i 3
        builder.setAdjacent(1, Direction.North, 2);
        builder.setAdjacent(1, Direction.East, 3);
        builder.buildDoor(1, 2);
        builder.buildDoor(1, 3);

        // Pokój 2 - magiczny, prowadzi do 4
        builder.setAdjacent(2, Direction.East, 4);
        builder.buildDoor(2, 4);

        // Pokój 3 - z bombą, ślepy zaułek
        // (ściany pozostają domyślne)

        // Pokój 4 - centralny, połączony ze wszystkimi
        builder.setAdjacent(4, Direction.South, 5);
        builder.buildDoor(4, 5);

        // Pokój 5 - wyjściowy, z magiczną ścianą zachodnią
        builder.setAdjacent(5, Direction.West, 3);

        // Dodajemy specjalne elementy przez fabrykę
        if (factory instanceof EnchantedMazeFactory) {
            // Pokój 2 staje się magiczny
            Room room2 = builder.getMaze().getRoom(2);
            room2.setSide(Direction.South, factory.createWall()); // Magiczna ściana

            // Ściana zachodnia w pokoju 5 jest magiczna
            Room room5 = builder.getMaze().getRoom(5);
            room5.setSide(Direction.West, factory.createWall());
        }
        else if (factory instanceof BombedMazeFactory) {
            // Pokój 3 ma bombę
            Room room3 = builder.getMaze().getRoom(3);
            ((BombedRoom)room3).activateBomb();
        }

        return builder.getMaze();
    }
}
