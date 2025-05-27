package pl.agh.edu.dp.labirynth;

public class EnchantedMazeFactory extends MazeFactory{
    private final String spell;

    private EnchantedMazeFactory(String spell) {
        this.spell = spell;
    }

    @Override
    public Room createRoom(int number) {
        return new EnchantedRoom(number, new Spell(this.spell));
    }

    // Statyczny builder lub po prostu public konstruktor(String spellText)
    public static class Builder {
        private String spell = "brak zaklęcia";

        public Builder withSpell(String spell) {
            this.spell = spell;
            return this;
        }

        public EnchantedMazeFactory build() {
            return new EnchantedMazeFactory(this.spell);
        }
    }

    @Override
    public Wall createWall() {
        return new EnchantedWall();
    }

    @Override
    public Door createDoor(Room r1, Direction enter, Room r2, Direction exit) {
        return new EnchantedDoor(r1, enter, r2, exit);
    }

    private Spell castSpell(String text) {
        return new Spell(text);
    }
}
