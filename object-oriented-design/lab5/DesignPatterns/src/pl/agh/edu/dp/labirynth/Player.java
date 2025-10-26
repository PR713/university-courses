package pl.agh.edu.dp.labirynth;

import java.util.Scanner;

public class Player {
    private Room currentRoom;
    private final Maze maze;

    public Player(Maze maze, int startingRoom) {
        this.maze = maze;
        this.currentRoom = maze.getRoom(startingRoom);
        if (currentRoom == null) {
            throw new IllegalArgumentException("Starting room doesn't exist");
        }
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Rozpoczynasz grę w pokoju " + currentRoom.getRoomNumber());

        while (true) {
            handleBombedRoom();
            System.out.println("\nGdzie chcesz iść? (N - północ, E - wschód, S - południe, W - zachód, Q - wyjście)");
            String input = scanner.nextLine().toUpperCase();

            if (input.equals("Q")) {
                System.out.println("Koniec gry!");
                break;
            }

            Direction direction = parseDirection(input);
            if (direction == null) {
                System.out.println("Nieprawidłowy kierunek!");
                continue;
            }

            move(direction);
        }
    }

    private Direction parseDirection(String input) {
        return switch (input) {
            case "N" -> Direction.North;
            case "E" -> Direction.East;
            case "S" -> Direction.South;
            case "W" -> Direction.West;
            default -> null;
        };
    }

    private void move(Direction direction) {
        MapSite side = currentRoom.getSide(direction);
        side.Enter();

        if (side instanceof Door) {
            Door door = (Door) side;
            currentRoom = (door.getRoom1() == currentRoom) ? door.getRoom2() : door.getRoom1();
            System.out.println("Wszedłeś do pokoju " + currentRoom.getRoomNumber());
        }
        else if (side instanceof EnchantedWall) {
            // Magiczna ściana przenosi do losowego pokoju
            int randomRoom = (int) (Math.random() * maze.getRoomNumbers()) + 1;
            currentRoom = maze.getRoom(randomRoom);
            System.out.println("Magia przeniosła cię do pokoju " + currentRoom.getRoomNumber());
        }

        if (currentRoom instanceof BombedRoom) {
            ((BombedRoom) currentRoom).checkBomb();
        }
    }

    private void handleBombedRoom() {
        if (currentRoom instanceof BombedRoom) {
            BombedRoom bombedRoom = (BombedRoom) currentRoom;
            if (!bombedRoom.isBombActive()) {
                System.out.println("Widzisz podejrzaną paczkę...");
                System.out.println("A - aktywuj bombę, I - zignoruj");

                Scanner scanner = new Scanner(System.in);
                String choice = scanner.nextLine().toUpperCase();

                if (choice.equals("A")) {
                    bombedRoom.activateBomb();
                }
            } else {
                System.out.println("Bomba tyka! Uciekaj szybko!");
            }
        }
    }

    public Room getCurrentRoom() {
        return currentRoom;
    }
}