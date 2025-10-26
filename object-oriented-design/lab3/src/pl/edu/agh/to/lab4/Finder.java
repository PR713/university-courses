package pl.edu.agh.to.lab4;

import java.util.Iterator;

public class Finder {
    private final CompositeAggregate suspectAggregate;

    public Finder(PersonDataProvider personDataProvider, PrisonersDatabase prisonersDatabase) {
        this.suspectAggregate = new CompositeAggregate();
        this.suspectAggregate.addAggregate(new PersonDataProviderDecorator(personDataProvider));
        this.suspectAggregate.addAggregate(new PrisonersDatabaseDecorator(prisonersDatabase));
    }

    public void displayAllSuspectsWithName(String name) {
        int suspectCount = 0;
        Iterator<AbstractSuspect> iterator = suspectAggregate.iterator();

        System.out.println("Znalazlem pasujacych podejrzanych:");

        while (iterator.hasNext() && suspectCount < 10) {
            AbstractSuspect suspect = iterator.next();
            if (suspect.canBeAccused() && suspect.getName().equals(name)) {
                System.out.println(suspect);
                suspectCount++;
            }
        }

        System.out.println("Znalazlem " + suspectCount + " pasujacych podejrzanych!");
    }
}