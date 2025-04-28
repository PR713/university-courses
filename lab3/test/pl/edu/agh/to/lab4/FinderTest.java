package pl.edu.agh.to.lab4;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class FinderTest {
    private ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private PrintStream originalOut;
    private PersonDataProvider personDataProvider;
    private PrisonersDatabase prisonersDatabase;
    private Finder suspectFinder;

    @Before
    public void setUp() {
        originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        personDataProvider = new PersonDataProvider();
        prisonersDatabase = new PrisonersDatabase();
        suspectFinder = new Finder(personDataProvider, prisonersDatabase);
    }

    @Test
    public void testDisplayingNotJailedPrisoner() {
        suspectFinder.displayAllSuspectsWithName("Jan");
        assertTrue(outContent.toString().contains("Prisoner{name='Jan', surname='Kowalski'}"));
    }

    @Test
    public void testDisplayingSuspectedPerson() {
        // Jan Kowalski jest dorosły i może być podejrzany
        suspectFinder.displayAllSuspectsWithName("Jan");
        assertTrue(outContent.toString().contains("Person{name='Jan', surname='Kowalski'}"));
    }

    @Test
    public void testNotDisplayingTooYoungPerson() {
        // Tomek Gimbus ma 14 lat i nie może być podejrzany
        suspectFinder.displayAllSuspectsWithName("Tomek");
        assertFalse(outContent.toString().contains("Person{name='Tomek', surname='Gimbus'}"));
    }

    @Test
    public void testNotDisplayingJailedPrisoner() {
        // Adam Future jest obecnie w więzieniu (judgementYear + sentenceDuration >= currentYear)
        suspectFinder.displayAllSuspectsWithName("Adam");
        assertFalse(outContent.toString().contains("Prisoner{name='Adam', surname='Future'}"));
    }

    @Test
    public void testDisplayLimitedTo10Suspects() {
        // Dodajmy więcej podejrzanych niż limit 10
        for (int i = 0; i < 15; i++) {
            personDataProvider.getAllCracovCitizens().add(new Person("Jan", "Nowak" + i, 25));
        }

        suspectFinder.displayAllSuspectsWithName("Jan");
        String output = outContent.toString();
        int count = output.split("Person\\{name='Jan', surname='").length - 1;
        count += output.split("Prisoner\\{name='Jan', surname='").length - 1;

        assertTrue(count <= 10);
    }

    @After
    public void tearDown() {
        System.setOut(originalOut);
    }
}