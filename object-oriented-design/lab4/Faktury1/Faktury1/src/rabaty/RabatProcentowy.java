package rabaty;

public class RabatProcentowy implements ObliczCenePoRabacie {
    private double procentRabatu;

    public RabatProcentowy(double procentRabatu) {
        this.procentRabatu = procentRabatu;
    }

    @Override
    public double obliczCenePoRabacie(double cena) {
        return cena * (1 - procentRabatu / 100);
    }
}