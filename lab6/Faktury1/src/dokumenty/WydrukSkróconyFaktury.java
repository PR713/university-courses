package dokumenty;

import java.util.Iterator;

public class WydrukSkróconyFaktury extends WydrukFaktury {

    @Override
    protected void drukujNaglowek(Faktura faktura) {
        System.out.println("--- Wydruk skrócony ---");
        System.out.println("Faktura dla: " + faktura.getKontrahent() + ", z dnia: " + faktura.getDataSprzedazy().toString());
    }

    @Override
    protected void drukujPozycje(Faktura faktura) {
        System.out.println("Pozycje:");
        Iterator<Pozycja> iteratorPozycji = faktura.getIteratorPozycji();
        while (iteratorPozycji.hasNext()) {
            Pozycja pozycja = iteratorPozycji.next();
            System.out.printf(" - %s -> %.2f zł%n", pozycja.getNazwa(), pozycja.getWartosc());
        }
    }

    @Override
    protected void drukujStopke(Faktura faktura) {
        System.out.printf("Łączna kwota: %.2f zł%n", faktura.getSuma());
        System.out.println("--- Koniec wydruku ---");
    }
}