package dokumenty;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Date;

import magazyn.Towar;
import rabaty.ObliczCenePoRabacie;

public class Faktura {
	private Date dataSprzedazy;
	private String kontrahent;
	private ArrayList<Pozycja> pozycje;
	private double suma;

	public Faktura(Date dataSprzedazy, String kontrahent) {
		this.dataSprzedazy = dataSprzedazy;
		this.kontrahent = kontrahent;
		pozycje = new ArrayList<Pozycja>();
		suma = 0;
	}

	public void dodajPozycje(Towar towar, double ilosc) {
		Pozycja pozycja = new Pozycja(towar, ilosc);

		// Implementacja wzorca Obserwator - dodanie faktury jako obserwatora pozycji
		pozycja.dodajObserwatora(new ObserwatorPozycji() {
			@Override
			public void aktualizujPozycje() {
				przeliczSume();
			}
		});

		pozycje.add(pozycja);
		this.przeliczSume();
	}

	// Nowa metoda pozwalająca dodać pozycję z rabatem
	public void dodajPozycjeZRabatem(Towar towar, double ilosc, ObliczCenePoRabacie rabat) {
		Pozycja pozycja = new Pozycja(towar, ilosc);

		// Implementacja wzorca Obserwator - dodanie faktury jako obserwatora pozycji
		pozycja.dodajObserwatora(new ObserwatorPozycji() {
			@Override
			public void aktualizujPozycje() {
				przeliczSume();
			}
		});

		// Zastosowanie strategii rabatu
		pozycja.zastosujRabat(rabat);

		pozycje.add(pozycja);
		this.przeliczSume();
	}

	public double getSuma() {
		return suma;
	}

	public Date getDataSprzedazy() {
		return dataSprzedazy;
	}

	// Metoda do przeliczania sumy - wywoływana automatycznie przez obserwatorów
	private void przeliczSume() {
		Iterator<Pozycja> iteratorPozycji = pozycje.iterator();
		Pozycja pozycja;
		suma = 0;
		while (iteratorPozycji.hasNext()) {
			pozycja = iteratorPozycji.next();
			suma += pozycja.getWartosc();
		}
	}

	public Iterator<Pozycja> getIteratorPozycji() {
		return pozycje.iterator();
	}

	// Metoda pomocnicza do pobierania konkretnej pozycji
	public Pozycja getPozycja(int index) {
		if (index >= 0 && index < pozycje.size()) {
			return pozycje.get(index);
		}
		return null;
	}

	public String getKontrahent() {
		return this.kontrahent;
	}

	// Metoda pomocnicza do wypisywania wszystkich pozycji
	public void wypiszPozycje() {
		Iterator<Pozycja> iteratorPozycji = getIteratorPozycji();
		while (iteratorPozycji.hasNext()) {
			Pozycja pozycja = iteratorPozycji.next();
			System.out.println("Towar: " + pozycja.getNazwa() +
					" Ilość: " + pozycja.getIlosc() +
					" Cena: " + pozycja.getCena() +
					" Wartość: " + pozycja.getWartosc());
		}
	}
}