package pl.edu.agh.to.lab4;

import java.util.Collection;
import java.util.Iterator;
import java.util.Map;

public class FlatIterator implements Iterator<AbstractSuspect> {

    private final Iterator<Map.Entry<String, Collection<Prisoner>>> prisonIterator;
    private Iterator<Prisoner> currentPrisonersIterator;

    public FlatIterator(Map<String, Collection<Prisoner>> map){
        this.prisonIterator = map.entrySet().iterator();
        this.currentPrisonersIterator = null;
    }

    @Override
    public boolean hasNext() {
        while ((currentPrisonersIterator == null || !currentPrisonersIterator.hasNext()) && prisonIterator.hasNext()) {
            currentPrisonersIterator = prisonIterator.next().getValue().iterator();
        }//musi być while, jeśli pusta lista w value to != null, false || true = !.. hasNext() więc szuka dalej
        //jeśli if to w return by zwróciło false i nie szukało dalej w prisonIterator
        return currentPrisonersIterator != null && currentPrisonersIterator.hasNext();
    }

    @Override
    public AbstractSuspect next() {
        return currentPrisonersIterator.next();
    }
}
