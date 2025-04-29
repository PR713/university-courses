package main;

import dokumenty.Faktura;
import dokumenty.Pozycja;
import magazyn.Towar;
import rabaty.ObliczCenePoRabacie;
import rabaty.RabatKwotowy;
import rabaty.RabatProcentowy;

import java.util.Calendar;

public class Ui {

    public static void main(String[] args) {
        Calendar teraz = Calendar.getInstance();

        // Tworzymy towary
        Towar t1 = new Towar(10, "buty");
        Towar t2 = new Towar(2, "skarpety");
        Towar t3 = new Towar(50, "kurtka");

        // Tworzymy strategie rabatów (wzorzec Strategia)
        ObliczCenePoRabacie rabatProcentowy = new RabatProcentowy(10); // 10% rabatu
        ObliczCenePoRabacie rabatKwotowy = new RabatKwotowy(5); // 5 zł rabatu

        // Tworzymy fakturę
        Faktura faktura = new Faktura(teraz.getTime(), "Fido");

        // Dodajemy pozycje - normalne i z rabatami
        faktura.dodajPozycje(t1, 3);
        faktura.dodajPozycjeZRabatem(t2, 5, rabatProcentowy);
        faktura.dodajPozycjeZRabatem(t3, 1, rabatKwotowy);

        System.out.println("Początkowa faktura:");
        wypiszFakture(faktura);

        // Demonstracja działania wzorca Obserwator - zmiana ilości automatycznie zaktualizuje sumę
        System.out.println("\nPo zmianie ilości w pierwszej pozycji:");
        Pozycja pozycja = faktura.getPozycja(0);
        pozycja.setIlosc(5); // To automatycznie zaktualizuje sumę faktury

        wypiszFakture(faktura);

        // Demonstracja zmiany ceny
        System.out.println("\nPo zmianie ceny w drugiej pozycji:");
        Pozycja pozycja2 = faktura.getPozycja(1);
        pozycja2.setCena(3); // To automatycznie zaktualizuje sumę faktury

        wypiszFakture(faktura);

        // Demonstracja dodania rabatu do istniejącej pozycji
        System.out.println("\nPo dodaniu rabatu do trzeciej pozycji:");
        Pozycja pozycja3 = faktura.getPozycja(2);
        pozycja3.zastosujRabat(new RabatProcentowy(20)); // 20% rabatu

        wypiszFakture(faktura);
    }

    private static void wypiszFakture(Faktura faktura) {
        System.out.println("=====================================================");
        System.out.println("FA z dnia: " + faktura.getDataSprzedazy().toString());
        System.out.println("Wystawiona dla: " + faktura.getKontrahent());
        System.out.println("Na kwotę: " + faktura.getSuma());
        System.out.println("Pozycje:");
        faktura.wypiszPozycje();
        System.out.println("=====================================================");
    }
}