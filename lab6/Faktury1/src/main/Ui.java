package main;

import java.util.Date;
import java.util.Iterator;
import java.util.Calendar;

import dokumenty.WydrukFaktury;
import dokumenty.WydrukSkróconyFaktury;
import magazyn.Kategoria;
import magazyn.Podkategoria;
import magazyn.Towar;
import dokumenty.Faktura;

//ZEWNETRZNY RABAT
import rabatlosowy.LosowyRabat;
import rabaty.*;


public class Ui {

	public static void main(String[] args) {
		Calendar teraz=Calendar.getInstance();
		WydrukFaktury wydruk = new WydrukSkróconyFaktury();		// dodane w punkcie 7

		//Tworzymy towary
		Towar t1=new Towar(10,"buty");
		Towar t2=new Towar(2,"skarpety");

		//I przykladowa fakture
		Faktura f=new Faktura(teraz.getTime(),"Fido");
		f.dodajPozycje(t1,10);
		f.dodajPozycje(t2, 5);

		System.out.println("Faktura bez prduktów rabatowych:");
		wydruk.drukujFakture(f);


/////////////////////////	TESTY DLA WZORCA STRATEGIA (4 kropka z instrukcji)
//		po zmianach w punkcie 5 najpierw musimy ustalić rabat a później dodawać produkty(pozycje) objęte tym rabatem
//		(wcześniej rabat był naliczany na całą fakturę a nie na pozycję)

		//Rabat procentowy 10%
		Faktura f2=new Faktura(teraz.getTime(),"Fido");
		f2.dodajPozycje(t1,3);
		f2.dodajPozycje(t2, 5);
		ObliczCenePoRabacie rabatProcentowy = new ObliczCenePoRabacieProcentowym(10);
		f2.setObliczCenePoRabacie(rabatProcentowy);
		f2.dodajPozycje(t1, 7);
		System.out.println("Faktura z rabatem procentowym 10%:");
		wydruk.drukujFakture(f2);

		//Rabat kwotowy 5 zł
		Faktura f3=new Faktura(teraz.getTime(),"Fido");
		f3.dodajPozycje(t1,3);
		f3.dodajPozycje(t2, 5);
		ObliczCenePoRabacie rabatKwotowy = new ObliczCenePoRabacieKwotowym(5);
		f3.setObliczCenePoRabacie(rabatKwotowy);
		f3.dodajPozycje(t1, 7);
		System.out.println("Faktura z rabatem kwotowym 5 zł:");
		wydruk.drukujFakture(f3);
///////////////////////////////////////////////////////////////
/////////////////	punkt 6 - SINGLETON
		Konfiguracja konfiguracja = Konfiguracja.getInstance();

		Faktura f4 = new Faktura(teraz.getTime(), "Fido");
		f4.dodajPozycje(t1, 3);
		f4.dodajPozycje(t2, 5);

		System.out.println("Faktura z domyślnym rabatem (0%):");
		wydruk.drukujFakture(f4);

		// Zmieniamy metodę obliczania rabatu na kwotowy (5 zł)
		konfiguracja.setObliczanieRabatu(new ObliczCenePoRabacieProcentowym(5));

		// Nowa faktura będzie używać nowej metody obliczania rabatu
		Faktura f5 = new Faktura(teraz.getTime(), "Fido");
		f5.dodajPozycje(t1, 3);
		f5.dodajPozycje(t2, 5);
		//konstruktor pobiera konfiguracja.getObliczanieRabatu w momencie tworzenia instancji Faktury
		System.out.println("Faktura z rabatem procentowym (5%):");
		wydruk.drukujFakture(f5);
///////////////////////////////////////////////////////////////////////////////////




		//TEST ZEWN. rabatu
		LosowyRabat lr=new LosowyRabat();
		System.out.println(lr.losujRabat());



		// ADAPTER

		ObliczCenePoRabacie strategiaLosowa = new AdapterLosowyRabat();
		Faktura f6 = new Faktura(teraz.getTime(), "Fido");
		f6.setObliczCenePoRabacie(strategiaLosowa);
		f6.dodajPozycje(t1, 3);


		// TEMPLATE METHOD
		konfiguracja.setObliczanieRabatu(new ObliczCenePoRabacieProcentowym(0));
		Towar t12 = new Towar(100, "Dysk SSD");
		Towar t22 = new Towar(250, "Pamięć RAM 16GB");

		// Tworzenie faktury
		Faktura f12 = new Faktura(new Date(), "Jan Kowalski");
		f12.dodajPozycje(t12, 2); // 2 * 100 = 200
		f12.dodajPozycje(t22, 1); // 1 * 250 = 250

		System.out.println("FORMAT STANDARDOWY:");
		WydrukFaktury drukarka = Konfiguracja.getInstance().getWydrukFaktury();
		drukarka.drukujFakture(f12);

		System.out.println("\n");

		System.out.println("ZMIANA KONFIGURACJI na format skrócony");
		Konfiguracja.getInstance().setWydrukFaktury(new WydrukSkróconyFaktury());
		//analogicznie można ustawić strategię rabatu i potem getObliczanieRabatu(), albo tylko dla pojedynczego nadal użyć:
		f12.setObliczCenePoRabacie(new ObliczCenePoRabacieKwotowym(10));
		f12.dodajPozycje(t12, 1); // 1 * (100-10) = 90

		drukarka = Konfiguracja.getInstance().getWydrukFaktury();
		drukarka.drukujFakture(f12);


		System.out.println("\n--- DRZEWO KATEGORII TOWARÓW ---");
		Towar laptop = new Towar(3500, "Laptop Gamingowy");
		Towar monitor = new Towar(1200, "Monitor Ultrawide");
		Towar klawiatura = new Towar(300, "Klawiatura Mechaniczna");
		Towar myszka = new Towar(150, "Myszka Bezprzewodowa");
		Towar sluchawki = new Towar(200, "Słuchawki z mikrofonem");
		Towar graPrzygodowa = new Towar(200, "Gra Przygodowa XYZ");
		Towar graStrategiczna = new Towar(180, "Gra Strategiczna ABC");

		Podkategoria elektronika = new Podkategoria("Elektronika");

		Podkategoria komputery = new Podkategoria("Komputery");

		Kategoria laptopy = new Kategoria("Laptopy");

		laptopy.addTowar(laptop);

		Kategoria akcesoriaPC = new Kategoria("Akcesoria PC");

		akcesoriaPC.addTowar(monitor);
		akcesoriaPC.addTowar(klawiatura);
		akcesoriaPC.addTowar(myszka);

		komputery.add(laptopy);
		komputery.add(akcesoriaPC);

		Kategoria audio = new Kategoria("Audio");
		audio.addTowar(sluchawki);

		Podkategoria gry = new Podkategoria("Gry i Oprogramowanie");

		Kategoria gryPC = new Kategoria("Gry PC");

		gryPC.addTowar(graPrzygodowa);
		gryPC.addTowar(graStrategiczna);
		gry.add(gryPC);

		elektronika.add(komputery);
		elektronika.add(audio);
		elektronika.add(gry);

		elektronika.print("");
	}

}
