package pl.agh.edu.dp.labirynth;

public class StandardBuilderMaze implements MazeBuilder {

    private final Maze currentMaze;

    public StandardBuilderMaze() {
        this.currentMaze = new Maze();
    }

    @Override
    public void buildRoom(int roomNumber) {
        if (currentMaze.getRoomNumbers() < roomNumber) {
            currentMaze.addRoom(new Room(roomNumber));
        }
    }

    @Override
    public void buildDoor(int roomFrom, int roomTo) {
        Room r1 = currentMaze.getRoom(roomFrom);
        Room r2 = currentMaze.getRoom(roomTo);

        if (r1 == null || r2 == null) {
            throw new IllegalArgumentException("Room doesn't exist");
        }

        Direction dir1 = CommonWall(r1, r2);

        if (dir1 == null) {
            throw new IllegalArgumentException("Rooms are not adjacent");
        }

        Direction dir2 = dir1.opposite();

        if (r1.getSide(dir1) != null && r2.getSide(dir2) != null) { //czyli są ściany
            Door door = new Door(r1, dir1, r2, dir2);
            r1.setSide(dir1, door); //zatem w kierunku dir1 ma drzwi (WK to ściana w if'ie wyżej)
            r2.setSide(dir2, door);
            r1.setNeighbour(dir1, r2);
            r2.setNeighbour(dir2, r1);
        }


    }

    @Override
    public void buildWall(int roomFrom, Direction direction) {
        Room room = currentMaze.getRoom(roomFrom);
        if (room == null) {
            throw new IllegalArgumentException();
        }
        room.setSide(direction, new Wall());
    }

    @Override
    public void setAdjacent(int roomFrom, Direction entrance, int roomTo) {
        Room r1 = currentMaze.getRoom(roomFrom);
        Room r2 = currentMaze.getRoom(roomTo);
        r1.setNeighbour(entrance, r2);
        r2.setNeighbour(entrance.opposite(), r1);
    }

    private Direction CommonWall(Room room1, Room room2) {
        for (Direction dir : Direction.values()) {
            if (room1.getNeighbour(dir) == room2) {
                return dir;
            }
        }
        return null;
    }

    public Maze getMaze() {
        return currentMaze;
    }
}
