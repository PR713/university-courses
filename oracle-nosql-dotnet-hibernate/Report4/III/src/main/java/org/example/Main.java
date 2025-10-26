package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {
        Configuration config = new Configuration().configure(); // domyślnie hibernate.cfg.xml
        SessionFactory sessionFactory = config.buildSessionFactory();

        try (Session session = sessionFactory.openSession()) {
            session.beginTransaction();

            System.out.println("=== [III] Tworzenie dostawcy i produktów (relacja dwustronna) ===");

            Supplier supplier = new Supplier("Gamma Sp. z o.o.", "Kwiatowa", "Wrocław");
            Product p1 = new Product("Młot pneumatyczny", 7);
            Product p2 = new Product("Szlifierka taśmowa", 14);
            Product p3 = new Product("Piła tarczowa", 11);

            supplier.addProduct(p1);
            supplier.addProduct(p2);
            supplier.addProduct(p3);

            session.persist(supplier); // kaskadowo zapisze produkty

            session.getTransaction().commit();

            System.out.println("Dostawca zapisany: " + supplier.getCompanyName());
            System.out.println("Produkty:");
            for (Product p : supplier.getProducts()) {
                System.out.println(" - " + p.getProductName() + ", " + p.getUnitsOnStock() + " szt.");
            }
        }

        sessionFactory.close();
    }
}
