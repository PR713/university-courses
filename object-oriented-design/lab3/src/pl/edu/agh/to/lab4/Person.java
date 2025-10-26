package pl.edu.agh.to.lab4;

public class Person extends AbstractSuspect{

    public Person(String name, String lastname, int age) {
        super(name, lastname, age);
    }

    @Override
    boolean canBeAccused() {
        return getAge() >= 18;
    }

}
