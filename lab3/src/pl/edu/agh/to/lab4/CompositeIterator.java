package pl.edu.agh.to.lab4;

import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class CompositeIterator implements Iterator<AbstractSuspect> {
    private final List<SuspectAggregate> aggregates;
    private int currentAggregateIndex = 0;
    private Iterator<AbstractSuspect> currentIterator = null;

    public CompositeIterator(List<SuspectAggregate> aggregates) {
        this.aggregates = aggregates;
        if (!aggregates.isEmpty()) {
            currentIterator = aggregates.get(0).iterator();
        }
    }

    @Override
    public boolean hasNext() {
        if (currentIterator == null) return false;

        while (!currentIterator.hasNext()) {
            currentAggregateIndex++;
            if (currentAggregateIndex >= aggregates.size()) {
                return false;
            }
            currentIterator = aggregates.get(currentAggregateIndex).iterator();
        }
        return true;
    }

    @Override
    public AbstractSuspect next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return currentIterator.next();
    }
}