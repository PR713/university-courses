package org.example;

import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Invoice {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "invoice_gen")
    @SequenceGenerator(name = "invoice_gen", sequenceName = "invoice_seq", allocationSize = 1)
    private Long id;

    private String invoiceNumber;

    @OneToMany(mappedBy = "invoice", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<InvoiceProduct> invoiceProducts = new HashSet<>();

    public Invoice() {}

    public Invoice(String invoiceNumber) {
        this.invoiceNumber = invoiceNumber;
    }

    // Gettery i settery
    public Long getId() { return id; }
    public String getInvoiceNumber() { return invoiceNumber; }
    public Set<InvoiceProduct> getInvoiceProducts() { return invoiceProducts; }

    public void setInvoiceNumber(String invoiceNumber) { this.invoiceNumber = invoiceNumber; }
}
