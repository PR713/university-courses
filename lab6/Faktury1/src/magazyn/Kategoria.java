package magazyn;

import java.util.ArrayList;
import java.util.List;

public class Kategoria extends CategoryComponent {
    private List<Towar> towary;

    public Kategoria(String name) {
        super(name);
        this.towary = new ArrayList<>();
    }

    @Override
    public void print(String indent) {
        System.out.println(indent + "Kategoria: " + name);
        if (!towary.isEmpty()) {
            System.out.println(indent + "  Towary w kategorii:");
            for (Towar towar : towary) {
                System.out.println(indent + "    - " + towar.getNazwa() + " (Cena: " + towar.getCena() + " zł)");
            }
        }
    }

    @Override
    public void addTowar(Towar towar) {
        this.towary.add(towar);
    }
}