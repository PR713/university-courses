package org.example;

import java.io.Serializable;
import java.util.Objects;

public class InvoiceProductId implements Serializable {
    private Long invoice;
    private Long product;

    public InvoiceProductId() {}

    public InvoiceProductId(Long invoice, Long product) {
        this.invoice = invoice;
        this.product = product;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof InvoiceProductId)) return false;
        InvoiceProductId that = (InvoiceProductId) o;
        return Objects.equals(invoice, that.invoice) &&
                Objects.equals(product, that.product);
    }

    @Override
    public int hashCode() {
        return Objects.hash(invoice, product);
    }
}
