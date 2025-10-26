package dokumenty;

import magazyn.Towar;

public class Pozycja {
	private Towar towar;
	private double cena;
	private double ilosc;
	private double wartosc;
	private String nazwa;

	public Pozycja(Towar towar, double ilosc) {
		this.towar = towar;
		this.ilosc = ilosc;
		this.cena = towar.getCena();
		this.nazwa = towar.getNazwa();
		this.przeliczWartosc();
	}

	public void setTowar(Towar towar) {
		this.towar = towar;
		this.cena = towar.getCena();
		this.przeliczWartosc();
	}

	public double getIlosc() {
		return ilosc;
	}

	public void setIlosc(double ilosc) {
		this.ilosc = ilosc;
		this.przeliczWartosc();
	}

	public double getCena()
	{
		return this.cena;
	}
	
	public void setCena(double cena) {
		this.cena = cena;
		this.przeliczWartosc();
	}

	public String getNazwa() {
		return nazwa;
	}

	public double getWartosc() {
		return wartosc;
	}

	// jak sie zmieni cos w pozycji to trzeba wywolac te metode
	private void przeliczWartosc() {
		this.wartosc = this.ilosc * this.cena;
	}

}
