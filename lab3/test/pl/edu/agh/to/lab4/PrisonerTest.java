package pl.edu.agh.to.lab4;

import org.junit.Test;
import java.util.Calendar;

import static org.junit.Assert.*;

public class PrisonerTest {
    @Test
    public void testPrisonerIsInJail() {
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);
        Prisoner prisoner = new Prisoner("Jan", "Kowalski", "802104543357", currentYear - 1, 2);
        assertTrue(prisoner.isJailedNow());
    }

    @Test
    public void testPrisonerHasBeenReleasedFromJail() {
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);
        Prisoner prisoner = new Prisoner("Jan", "Kowalski", "802104543357", currentYear - 5, 3);
        assertFalse(prisoner.isJailedNow());
    }

    @Test
    public void testPrisonerCanBeAccused() {
        Prisoner prisoner = new Prisoner("Jan", "Kowalski", "802104543357", 2008, 5);
        assertTrue(prisoner.canBeAccused());
    }

    @Test
    public void testPrisonerAgeCalculation() {
        Prisoner prisoner = new Prisoner("Jan", "Kowalski", "802104543357", 2008, 5);
        int expectedAge = Calendar.getInstance().get(Calendar.YEAR) - 1980;
        assertEquals(expectedAge, prisoner.getAge());
    }

    @Test
    public void testPrisonerToString() {
        Prisoner prisoner = new Prisoner("Jan", "Kowalski", "802104543357", 2008, 5);
        assertEquals("Prisoner{name='Jan', surname='Kowalski'}", prisoner.toString());
    }
}