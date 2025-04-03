package pl.edu.agh.to.lab4;

public class Person {
    private String firstname;

    private String lastname;

    private int age;

    public Person(String firstname, String lastname, int age) {
        this.age = age;
        this.firstname = firstname;
        this.lastname = lastname;
    }

    public int getAge() {
        return age;
    }

    public String firstname() {
        return firstname;
    }

    public String middlename() {
        return lastname;
    }

    public String display() {
        return firstname + " " + lastname;
    }
}
