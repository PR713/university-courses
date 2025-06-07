package org.example.model.manytomany;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String productName;
    private int unitsOnStock;

    @ManyToMany(mappedBy = "products")
    private List<Supplier> suppliers = new ArrayList<>();

    public Product() {}

    public Product(String productName, int unitsOnStock) {
        this.productName = productName;
        this.unitsOnStock = unitsOnStock;
    }

    public Long getId() { return id; }
    public String getProductName() { return productName; }
    public int getUnitsOnStock() { return unitsOnStock; }
    public List<Supplier> getSuppliers() { return suppliers; }

    public void setProductName(String productName) { this.productName = productName; }
    public void setUnitsOnStock(int unitsOnStock) { this.unitsOnStock = unitsOnStock; }
}
