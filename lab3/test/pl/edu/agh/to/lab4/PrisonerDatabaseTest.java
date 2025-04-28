package pl.edu.agh.to.lab4;

import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;

import static org.junit.Assert.*;

public class PrisonerDatabaseTest {
    private PrisonersDatabase prisonersDatabase;

    @Before
    public void setUp() {
        prisonersDatabase = new PrisonersDatabase();
    }

    @Test
    public void testThereAreThreeJails() {
        assertEquals(3, prisonersDatabase.findAll().size());
    }

    @Test
    public void testPrisonersCountInJails() {
        int totalPrisoners = prisonersDatabase.findAll().values()
                .stream()
                .mapToInt(Collection::size)
                .sum();
        assertEquals(8, totalPrisoners);
    }

    @Test
    public void testFindAllReturnsUnmodifiableMap() {
        Map<String, Collection<Prisoner>> map = prisonersDatabase.findAll();
        try {
            map.put("New Jail", new ArrayList<>());
            fail("Should throw UnsupportedOperationException");
        } catch (UnsupportedOperationException e) {
            // Expected behavior
        }
    }
}