package pl.agh.edu.dp.labirynth;

public class EnchantedRoom extends Room {
    private final Spell spell;

    public EnchantedRoom(int number, Spell spell) {
        super(number);
        this.spell = spell;
    }

    @Override
    public void Enter() {
        super.Enter();
        System.out.println("W tym pokoju zdobywasz: " + this.spell.getSpellEffect());
    }
}
