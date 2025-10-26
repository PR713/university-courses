package pl.edu.agh.to.lab4;

import java.util.Iterator;

public class PrisonersDatabaseDecorator implements SuspectAggregate{

    private final PrisonersDatabase prisonersDatabase;

    public PrisonersDatabaseDecorator(PrisonersDatabase prisonersDatabase) {
        this.prisonersDatabase = prisonersDatabase;
    }

    @Override
    public Iterator<AbstractSuspect> iterator() {
        return new FlatIterator(prisonersDatabase.findAll());
    }
}
