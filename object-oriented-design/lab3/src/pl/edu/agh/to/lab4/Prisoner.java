package pl.edu.agh.to.lab4;

import java.util.Calendar;

public class Prisoner extends AbstractSuspect {
    private final int judgementYear;

    private final int sentenceDuration;

    private final String pesel;

    public Prisoner(String name, String surname, String pesel, int judgementYear, int sentenceDuration) {
        super(name, surname, calculateAgeFromPesel(pesel));
        this.pesel = pesel;
        this.judgementYear = judgementYear;
        this.sentenceDuration = sentenceDuration;
    }

    private static int calculateAgeFromPesel(String pesel) {
        int year = Integer.parseInt(pesel.substring(0, 2));
        int currentYear = Calendar.getInstance().get(Calendar.YEAR);

        if (year <= 24) {
            year += 2000;
        } else {
            year += 1900;
        }

        return currentYear - year;
    }

    public String getPesel() {
        return pesel;
    }

    public boolean isJailedNow() {
        return judgementYear + sentenceDuration >= getCurrentYear();
    }

    public int getCurrentYear() {
        return Calendar.getInstance().get(Calendar.YEAR);
    }

    public int getJudgementYear() {
        return judgementYear;
    }


    @Override
    boolean canBeAccused() {
        return !isJailedNow() && getAge() >= 18;
    }

    @Override
    public String toString() {
        return "Prisoner{" +
                "name='" + name + '\'' +
                ", surname='" + surname + '\'' +
                '}';
    }
}
