package dokumenty;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Date;

import magazyn.Towar;
import rabaty.Konfiguracja;
import rabaty.ObliczCenePoRabacie;


public class Faktura {
	Date dataSprzedazy;
	String kontrahent;
	ArrayList<Pozycja> pozycje;
	double suma;
	private ObliczCenePoRabacie obliczCenePoRabacie;

	public Faktura(Date dataSprzedazy,String kontrahent)
	{
		this.dataSprzedazy=dataSprzedazy;
		this.kontrahent=kontrahent;
		pozycje=new ArrayList<Pozycja>();
		suma=0;
		this.obliczCenePoRabacie = Konfiguracja.getInstance().getObliczanieRabatu();
	}
	public void dodajPozycje(Towar towar, double ilosc)
	{
		Pozycja pozycja = new Pozycja(towar, ilosc);
		if (obliczCenePoRabacie != null) {
			double cenaPoRabacie = obliczCenePoRabacie.obliczCenePoRabacie(towar.getCena());
			pozycja.setCena(cenaPoRabacie);
		}
		pozycje.add(pozycja);
		this.przeliczSume();
	}
	public double getSuma()
	{
		return suma;
	}
	public Date getDataSprzedazy()
	{
		return dataSprzedazy;
	}

	private void przeliczSume() {
		Iterator<Pozycja> iteratorPozycji = pozycje.iterator();
		Pozycja pozycja;
		suma = 0;
		while (iteratorPozycji.hasNext()) {
			pozycja = iteratorPozycji.next();
			suma += pozycja.getWartosc();
		}
	}

	public Iterator<Pozycja> getIteratorPozycji()
	{
		return pozycje.iterator();
	}
	public String getKontrahent()
	{
		return this.kontrahent;
	}

	public void setObliczCenePoRabacie(ObliczCenePoRabacie obliczCenePoRabacie) {
		this.obliczCenePoRabacie = obliczCenePoRabacie;
		this.przeliczSume();
	}
	
	
}
