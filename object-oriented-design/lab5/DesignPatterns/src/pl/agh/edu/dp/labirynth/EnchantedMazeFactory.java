package pl.agh.edu.dp.labirynth;

public class EnchantedMazeFactory extends MazeFactory {
    private static EnchantedMazeFactory instance;
    private final String spell;

    private EnchantedMazeFactory(String spell) {
        this.spell = spell;
    }

    public static class Builder {
        private String spell = "Default Spell";

        public Builder withSpell(String spell) {
            this.spell = spell;
            return this;
        }

        public EnchantedMazeFactory build() {
            if (instance == null) {
                synchronized (EnchantedMazeFactory.class) {
                    if (instance == null) {
                        instance = new EnchantedMazeFactory(spell);
                    }
                }
            }
            return instance;
        }
    }

    public static EnchantedMazeFactory getInstance() {
        if (instance == null) {
            synchronized (EnchantedMazeFactory.class) {
                if (instance == null) {
                    instance = new EnchantedMazeFactory("Default Spell");
                }
            }
        }
        return instance;
    }

    public String getSpell() {
        return this.spell;
    }

    @Override
    public Room createRoom(int number) {
        return new EnchantedRoom(number, new Spell(this.spell));
    }

    @Override
    public Wall createWall() {
        return new EnchantedWall();
    }

    @Override
    public Door createDoor(Room r1, Direction enter, Room r2, Direction exit) {
        return new EnchantedDoor(r1, enter, r2, exit);
    }

    // For testing purposes only
    public static void reset() {
        synchronized (EnchantedMazeFactory.class) {
            instance = null;
        }
    }
}