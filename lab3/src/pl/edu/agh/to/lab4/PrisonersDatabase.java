package pl.edu.agh.to.lab4;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class PrisonersDatabase {

    private final Map<String, Collection<Prisoner>> prisoners = new HashMap<String, Collection<Prisoner>>();

    public PrisonersDatabase() {
        if (!prisoners.containsKey("Wiezienie krakowskie")) {
            prisoners.put("Wiezienie krakowskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie krakowskie").add(new Prisoner("Jan", "Kowalski", "87080452357", 2005, 7));
        if (!prisoners.containsKey("Wiezienie krakowskie")) {
            prisoners.put("Wiezienie krakowskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie krakowskie").add(new Prisoner("Anita", "Wiercipieta", "84080452357", 2009, 3));
        if (!prisoners.containsKey("Wiezienie krakowskie")) {
            prisoners.put("Wiezienie krakowskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie krakowskie").add(new Prisoner("Janusz", "Zlowieszczy", "92080445657", 2001, 10));
        if (!prisoners.containsKey("Wiezienie przedmiejskie")) {
            prisoners.put("Wiezienie przedmiejskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie przedmiejskie").add(new Prisoner("Janusz", "Zamkniety", "802104543357", 2010, 5));
        if (!prisoners.containsKey("Wiezienie przedmiejskie")) {
            prisoners.put("Wiezienie przedmiejskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie przedmiejskie").add(new Prisoner("Adam", "Future", "880216043357", 2020, 5));
        if (!prisoners.containsKey("Wiezienie przedmiejskie")) {
            prisoners.put("Wiezienie przedmiejskie", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie przedmiejskie").add(new Prisoner("Zbigniew", "Nienajedzony", "90051452335", 2011, 1));
        if (!prisoners.containsKey("Wiezienie centralne")) {
            prisoners.put("Wiezienie centralne", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie centralne").add(new Prisoner("Jan", "Przedziwny", "91103145223", 2009, 4));
        if (!prisoners.containsKey("Wiezienie centralne")) {
            prisoners.put("Wiezienie centralne", new ArrayList<Prisoner>());
        }
        prisoners.get("Wiezienie centralne").add(new Prisoner("Janusz", "Podejrzany", "85121212456", 2012, 1));
    }

    public Map<String, Collection<Prisoner>> findAll() {
        return prisoners;
    }

    @Override
    public String toString() {
        return "PrisonersDatabase{" + "prisoners=" + prisoners + '}';
    }
}
