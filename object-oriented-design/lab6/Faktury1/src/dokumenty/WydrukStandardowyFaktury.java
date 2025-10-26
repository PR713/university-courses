package dokumenty;

import java.util.Iterator;

public class WydrukStandardowyFaktury extends WydrukFaktury {

    @Override
    protected void drukujNaglowek(Faktura faktura) {
        System.out.println("=====================================================");
        System.out.println("FAKTURA VAT z dnia: " + faktura.getDataSprzedazy().toString());
        System.out.println("Wystawiona dla: " + faktura.getKontrahent());
        System.out.println("-----------------------------------------------------");
    }

    @Override
    protected void drukujPozycje(Faktura faktura) {
        Iterator<Pozycja> iteratorPozycji = faktura.getIteratorPozycji();
        while (iteratorPozycji.hasNext()) {
            Pozycja pozycja = iteratorPozycji.next();
            System.out.printf("Towar: %-20s | Ilość: %-5.2f | Cena: %-7.2f zł | Wartość: %.2f zł%n",
                    pozycja.getNazwa(), pozycja.getIlosc(), pozycja.getCena(), pozycja.getWartosc());
        }
    }

    @Override
    protected void drukujStopke(Faktura faktura) {
        System.out.println("-----------------------------------------------------");
        System.out.printf("SUMA DO ZAPŁATY: %.2f zł%n", faktura.getSuma());
        System.out.println("=====================================================");
    }
}