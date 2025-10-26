package org.example;

import jakarta.persistence.*;

@Entity
@IdClass(InvoiceProductId.class)
public class InvoiceProduct {
    @Id
    @ManyToOne
    private Invoice invoice;

    @Id
    @ManyToOne
    private Product product;

    private int quantity;

    public InvoiceProduct() {}
    public InvoiceProduct(Invoice invoice, Product product, int quantity) {
        this.invoice = invoice;
        this.product = product;
        this.quantity = quantity;
        invoice.getInvoiceProducts().add(this);
        product.getInvoiceProducts().add(this);
    }

    public int getQuantity() {
        return quantity;
    }
    public Product getProduct() {
        return product;
    }
    public Invoice getInvoice() {
        return invoice;
    }
}
