package rabaty;

public class RabatKwotowy implements ObliczCenePoRabacie {
    private double kwotaRabatu;

    public RabatKwotowy(double kwotaRabatu) {
        this.kwotaRabatu = kwotaRabatu;
    }

    @Override
    public double obliczCenePoRabacie(double cena) {
        return Math.max(0, cena - kwotaRabatu);
    }
}