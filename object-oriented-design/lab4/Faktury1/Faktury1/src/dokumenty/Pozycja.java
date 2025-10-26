package dokumenty;

import magazyn.Towar;
import rabaty.ObliczCenePoRabacie;
import java.util.ArrayList;

public class Pozycja {
	private Towar towar;
	private double cena;
	private double ilosc;
	private double wartosc;
	private String nazwa;
	private ObliczCenePoRabacie strategiaRabatu;

	// Lista obserwatorów - część wzorca Obserwator
	private ArrayList<ObserwatorPozycji> obserwatorzy = new ArrayList<>();

	public Pozycja(Towar towar, double ilosc) {
		this.towar = towar;
		this.ilosc = ilosc;
		this.cena = towar.getCena();
		this.nazwa = towar.getNazwa();
		this.przeliczWartosc();
	}

	// Metody wzorca Obserwator
	public void dodajObserwatora(ObserwatorPozycji obserwator) {
		obserwatorzy.add(obserwator);
	}

	public void usunObserwatora(ObserwatorPozycji obserwator) {
		obserwatorzy.remove(obserwator);
	}

	protected void powiadomObserwatorow() {
		for (ObserwatorPozycji obserwator : obserwatorzy) {
			obserwator.aktualizujPozycje();
		}
	}

	// Metody wzorca Strategia
	public void zastosujRabat(ObliczCenePoRabacie strategiaRabatu) {
		this.strategiaRabatu = strategiaRabatu;
		this.przeliczWartosc();
		this.powiadomObserwatorow();
	}

	public void setTowar(Towar towar) {
		this.towar = towar;
		this.cena = towar.getCena();
		this.nazwa = towar.getNazwa();
		this.przeliczWartosc();
		this.powiadomObserwatorow();
	}

	public double getIlosc() {
		return ilosc;
	}

	public void setIlosc(double ilosc) {
		this.ilosc = ilosc;
		this.przeliczWartosc();
		this.powiadomObserwatorow();
	}

	public double getCena() {
		return this.cena;
	}

	public void setCena(double cena) {
		this.cena = cena;
		this.przeliczWartosc();
		this.powiadomObserwatorow();
	}

	public String getNazwa() {
		return nazwa;
	}

	public double getWartosc() {
		return wartosc;
	}

	// Zmodyfikowana metoda przeliczania wartości uwzględniająca rabat
	private void przeliczWartosc() {
		if (strategiaRabatu != null) {
			double cenaPoRabacie = strategiaRabatu.obliczCenePoRabacie(this.cena);
			this.wartosc = this.ilosc * cenaPoRabacie;
		} else {
			this.wartosc = this.ilosc * this.cena;
		}
	}
}