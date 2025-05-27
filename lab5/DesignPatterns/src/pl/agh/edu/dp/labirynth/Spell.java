package pl.agh.edu.dp.labirynth;

public class Spell {
    private final String spellText;

    public Spell(String spellText) {
        this.spellText = spellText;
    }

    public String getSpellEffect(){
        return this.spellText;
    }
}
