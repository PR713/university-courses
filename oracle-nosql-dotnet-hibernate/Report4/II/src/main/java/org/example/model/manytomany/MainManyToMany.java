package org.example.model.manytomany;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class MainManyToMany {
    public static void main(String[] args) {
        Configuration config = new Configuration().configure("hibernate_manytomany.cfg.xml");
        SessionFactory sessionFactory = config.buildSessionFactory();

        try (Session session = sessionFactory.openSession()) {
            session.beginTransaction();

            System.out.println("=== [ManyToMany] Tworzenie dostawcy i 3 produktów ===");

            Supplier supplier = new Supplier("Beta Tools", "Industrial Rd", "Warszawa");
            Product p1 = new Product("Piła", 20);
            Product p2 = new Product("Kombinerki", 40);
            Product p3 = new Product("Klucz francuski", 25);

            supplier.addProduct(p1);
            supplier.addProduct(p2);
            supplier.addProduct(p3);

            session.persist(p1);
            session.persist(p2);
            session.persist(p3);
            session.persist(supplier);

            session.getTransaction().commit();

            System.out.println("Dostawca został zapisany: " + supplier.getCompanyName());
            System.out.println("Produkty przypisane:");
            for (Product p : supplier.getProducts()) {
                System.out.println(" - " + p.getProductName() + ", " + p.getUnitsOnStock() + " szt.");
            }
        }

        sessionFactory.close();
    }
}
