package pl.edu.agh.to.lab4;

import java.util.Calendar;

public class Prisoner extends AbstractSuspect{
    private final int judgementYear;

    private final int sentenceDuration;

    private final String pesel;

    public Prisoner(String name, String surname, String pesel, int judgementYear, int sentenceDuration) {
        super(name, surname, Integer.parseInt(pesel.substring(0,2)));
        this.pesel = pesel;
        this.judgementYear = judgementYear;
        this.sentenceDuration = sentenceDuration;
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
    public String toString() {
        return "Prisoner{" +
                "name='" + name + '\'' +
                ", surname='" + surname + '\'' +
                '}';
    }
}
