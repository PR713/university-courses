package org.example.model.onetomany;

import jakarta.persistence.*;

@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String productName;
    private int unitsOnStock;

    @ManyToOne
    @JoinColumn(name = "supplier_id")
    private Supplier supplier;

    public Product() {}

    public Product(String productName, int unitsOnStock) {
        this.productName = productName;
        this.unitsOnStock = unitsOnStock;
    }

    public Long getId() { return id; }
    public String getProductName() { return productName; }
    public int getUnitsOnStock() { return unitsOnStock; }
    public Supplier getSupplier() { return supplier; }

    public void setProductName(String productName) { this.productName = productName; }
    public void setUnitsOnStock(int unitsOnStock) { this.unitsOnStock = unitsOnStock; }
    public void setSupplier(Supplier supplier) { this.supplier = supplier; }
}
