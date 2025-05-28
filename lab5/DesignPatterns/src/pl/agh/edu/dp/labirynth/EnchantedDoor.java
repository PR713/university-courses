package pl.agh.edu.dp.labirynth;

public class EnchantedDoor extends Door {
    public EnchantedDoor(Room r1, Direction enter, Room r2, Direction exit) {
        super(r1, enter, r2, exit);
    }

    @Override
    public void Enter() {
        System.out.println("Drzwi otwierają się bez posiadania klucza :O");
    }
}