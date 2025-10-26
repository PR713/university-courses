package org.example.model.onetomany;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
public class Supplier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String companyName;
    private String street;
    private String city;

    @OneToMany(mappedBy = "supplier", cascade = CascadeType.ALL)
    private List<Product> products = new ArrayList<>();

    public Supplier() {}

    public Supplier(String companyName, String street, String city) {
        this.companyName = companyName;
        this.street = street;
        this.city = city;
    }

    public void addProduct(Product product) {
        products.add(product);
        product.setSupplier(this);
    }

    public Long getId() { return id; }
    public String getCompanyName() { return companyName; }
    public String getStreet() { return street; }
    public String getCity() { return city; }
    public List<Product> getProducts() { return products; }

    public void setCompanyName(String companyName) { this.companyName = companyName; }
    public void setStreet(String street) { this.street = street; }
    public void setCity(String city) { this.city = city; }
}
