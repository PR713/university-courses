package rabaty;

import rabatlosowy.LosowyRabat;

public class AdapterLosowyRabat implements ObliczCenePoRabacie{

    private final LosowyRabat losowyRabat;

    public AdapterLosowyRabat() {
        this.losowyRabat = new LosowyRabat();
    }

    @Override
    public double obliczCenePoRabacie(double cena) {
        double wylosowanyRabat = this.losowyRabat.losujRabat();
        return cena * (1 - wylosowanyRabat);
    }
}
