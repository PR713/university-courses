package org.example;

import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "product_gen")
    @SequenceGenerator(name = "product_gen", sequenceName = "product_seq", allocationSize = 1)
    private Long id;

    private String name;
    private int unitsInStock;

    @OneToMany(mappedBy = "product", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<InvoiceProduct> invoiceProducts = new HashSet<>();

    public Product() {}

    public Product(String name, int unitsInStock) {
        this.name = name;
        this.unitsInStock = unitsInStock;
    }

    // Gettery i settery
    public Long getId() { return id; }
    public String getName() { return name; }
    public int getUnitsInStock() { return unitsInStock; }
    public Set<InvoiceProduct> getInvoiceProducts() { return invoiceProducts; }

    public void setName(String name) { this.name = name; }
    public void setUnitsInStock(int unitsInStock) { this.unitsInStock = unitsInStock; }
}
