package org.example.model.onetomany;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class MainOneToMany {
    public static void main(String[] args) {
        Configuration config = new Configuration().configure("hibernate_onetomany.cfg.xml");
        SessionFactory sessionFactory = config.buildSessionFactory();

        try (Session session = sessionFactory.openSession()) {
            session.beginTransaction();

            System.out.println("=== [OneToMany] Tworzenie dostawcy i 3 produktów ===");

            Supplier supplier = new Supplier("Acme Corp", "Main Street", "Krakow");
            Product p1 = new Product("Wiertarka", 15);
            Product p2 = new Product("Młotek", 30);
            Product p3 = new Product("Śrubokręt", 50);

            supplier.addProduct(p1);
            supplier.addProduct(p2);
            supplier.addProduct(p3);

            session.persist(supplier);

            session.getTransaction().commit();

            System.out.println("Dostawca został zapisany: " + supplier.getCompanyName());
            System.out.println("Produkty:");
            for (Product p : supplier.getProducts()) {
                System.out.println(" - " + p.getProductName() + ", " + p.getUnitsOnStock() + " szt.");
            }
        }

        sessionFactory.close();
    }
}
