package rabaty;

public class Konfiguracja {
    private static Konfiguracja instance;
    private ObliczCenePoRabacie obliczanieRabatu;

    private Konfiguracja() {
        this.obliczanieRabatu = new ObliczCenePoRabacieProcentowym(0);
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
}