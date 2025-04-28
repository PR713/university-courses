package pl.edu.agh.to.lab4;

import java.util.Iterator;

public class PersonDataProviderDecorator implements SuspectAggregate{

    private final PersonDataProvider personDataProvider;

    public PersonDataProviderDecorator(PersonDataProvider personDataProvider) {
        this.personDataProvider = personDataProvider;
    }

    @Override
    public Iterator<AbstractSuspect> iterator() {
        return new Iterator<AbstractSuspect>() { //powoduje implementację Iterator<AbstractSuspect>

            private final Iterator<Person> internalIterator = personDataProvider.getAllCracovCitizens().iterator();

            @Override
            public boolean hasNext() {
                return internalIterator.hasNext();
            }

            @Override
            public AbstractSuspect next() {
                return internalIterator.next();
            }
        };
    }

}
