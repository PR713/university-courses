package rabaty;

public class ObliczCenePoRabacieProcentowym implements ObliczCenePoRabacie {
    private double procentRabatu;

    public ObliczCenePoRabacieProcentowym(double procentRabatu) {
        this.procentRabatu = procentRabatu;
    }

    @Override
    public double obliczCenePoRabacie(double cena) {
        return cena * (1 - procentRabatu / 100);
    }
}