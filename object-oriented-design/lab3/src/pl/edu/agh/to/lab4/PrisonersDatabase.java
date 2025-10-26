package pl.edu.agh.to.lab4;

import java.util.*;

public class PrisonersDatabase {

    private final Map<String, Collection<Prisoner>> prisoners = new HashMap<String, Collection<Prisoner>>();

    public PrisonersDatabase() {
        addPrisoner("Wiezienie krakowskie", new Prisoner("Jan", "Kowalski", "87080452357", 2005, 7));
        addPrisoner("Wiezienie krakowskie", new Prisoner("Anita", "Wiercipieta", "84080452357", 2009, 3));
        addPrisoner("Wiezienie krakowskie", new Prisoner("Janusz", "Zlowieszczy", "92080445657", 2001, 10));

        addPrisoner("Wiezienie przedmiejskie", new Prisoner("Janusz", "Zamkniety", "802104543357", 2010, 5));
        addPrisoner("Wiezienie przedmiejskie", new Prisoner("Adam", "Future", "880216043357", 2020, 5));
        addPrisoner("Wiezienie przedmiejskie", new Prisoner("Zbigniew", "Nienajedzony", "90051452335", 2011, 1));

        addPrisoner("Wiezienie centralne", new Prisoner("Jan", "Przedziwny", "91103145223", 2009, 4));
        addPrisoner("Wiezienie centralne", new Prisoner("Janusz", "Podejrzany", "85121212456", 2012, 1));
    }

    private void addPrisoner(String prisonName, Prisoner prisoner) {
        prisoners.putIfAbsent(prisonName, new ArrayList<>());
        prisoners.get(prisonName).add(prisoner);
    }


    public Map<String, Collection<Prisoner>> findAll() {
        Map<String, Collection<Prisoner>> unmodifiableMap = new HashMap<>();
        for (Map.Entry<String, Collection<Prisoner>> entry : prisoners.entrySet()) {
            unmodifiableMap.put(entry.getKey(), Collections.unmodifiableCollection(entry.getValue()));
        }
        return Collections.unmodifiableMap(unmodifiableMap);
    }

    @Override
    public String toString() {
        return "PrisonersDatabase{" + "prisoners=" + prisoners + '}';
    }
}
