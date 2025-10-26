package pl.agh.edu.dp.labirynth;

import java.sql.SQLOutput;
import java.util.EnumMap;
import java.util.Map;

public class Room extends MapSite
{
    private final int roomNumber;
    private final Map<Direction, MapSite> sides;
    private final Map<Direction, Room> neighbours;


    public Room(int number){
        this.sides = new EnumMap<>(Direction.class);
        this.roomNumber = number;
        this.neighbours = new EnumMap<>(Direction.class);
    }

    public MapSite getSide(Direction direction){
        return this.sides.get(direction);
    }

    public void setSide(Direction direction, MapSite ms){
        this.sides.put(direction, ms);
    }

    public int getRoomNumber(){
        return this.roomNumber;
    }

    public void setNeighbour(Direction direction, Room neighbour) {
        this.neighbours.put(direction, neighbour);
    }

    public Room getNeighbour(Direction direction) {
        return this.neighbours.get(direction);
    }

    @Override
    public void Enter(){
        System.out.println("Entering room " + this.roomNumber);
    }
}
