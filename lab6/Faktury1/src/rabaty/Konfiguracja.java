package rabaty;

import dokumenty.WydrukFaktury;
import dokumenty.WydrukStandardowyFaktury;

public class Konfiguracja {
    private static Konfiguracja instance;
    private ObliczCenePoRabacie obliczanieRabatu;
    private WydrukFaktury wydrukFaktury;

    private Konfiguracja() {
        this.obliczanieRabatu = new ObliczCenePoRabacieProcentowym(0);
        this.wydrukFaktury = new WydrukStandardowyFaktury();
    }

    public static synchronized Konfiguracja getInstance() {
        if (instance == null) {
            instance = new Konfiguracja();
        }
        return instance;
    }

    public ObliczCenePoRabacie getObliczanieRabatu() {
        return obliczanieRabatu;
    }

    public void setObliczanieRabatu(ObliczCenePoRabacie obliczanieRabatu) {
        this.obliczanieRabatu = obliczanieRabatu;
    }

    public WydrukFaktury getWydrukFaktury() {
        return wydrukFaktury;
    }

    public void setWydrukFaktury(WydrukFaktury wydrukFaktury) {
        this.wydrukFaktury = wydrukFaktury;
    }
}