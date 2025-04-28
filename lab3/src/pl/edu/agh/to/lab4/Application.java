package pl.edu.agh.to.lab4;

public class Application {
    public static void main(String[] args) {
        PersonDataProvider personDataProvider = new PersonDataProvider();
        PrisonersDatabase prisonersDatabase = new PrisonersDatabase();

        Finder suspects = new Finder(personDataProvider, prisonersDatabase);
        suspects.displayAllSuspectsWithName("Jan");
    }
}