package main;

import java.util.Iterator;
import java.util.Calendar;

import dokumenty.WydrukFaktury;
import magazyn.Towar;
import dokumenty.Faktura;

//ZEWNETRZNY RABAT
import rabatlosowy.LosowyRabat;
import rabaty.Konfiguracja;
import rabaty.ObliczCenePoRabacie;
import rabaty.ObliczCenePoRabacieKwotowym;
import rabaty.ObliczCenePoRabacieProcentowym;


public class Ui {

	public static void main(String[] args) {
		Calendar teraz=Calendar.getInstance();
		WydrukFaktury wydruk = new WydrukFaktury();		// dodane w punkcie 7
		
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

		System.out.println("Faktura z rabatem procentowym (5%):");
		wydruk.drukujFakture(f5);
///////////////////////////////////////////////////////////////////////////////////


		//TEST ZEWN. rabatu
		LosowyRabat lr=new LosowyRabat();
		System.out.println(lr.losujRabat());
	}

}
