package org.example;

import jakarta.persistence.*;

public class Main {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("my-jpa-unit");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();

        Product p1 = new Product("Młotek", 30);
        Product p2 = new Product("Wiertarka", 20);

        Invoice i1 = new Invoice("FV/001");
        Invoice i2 = new Invoice("FV/002");

        em.persist(p1);
        em.persist(p2);
        em.persist(i1);
        em.persist(i2);

        InvoiceProduct ip1 = new InvoiceProduct(i1, p1, 5);
        InvoiceProduct ip2 = new InvoiceProduct(i1, p2, 2);
        InvoiceProduct ip3 = new InvoiceProduct(i2, p1, 1);

        em.persist(ip1);
        em.persist(ip2);
        em.persist(ip3);

        em.getTransaction().commit();

        System.out.println("Produkty z faktury FV/001:");
        for (InvoiceProduct ip : i1.getInvoiceProducts()) {
            System.out.println(" - " + ip.getProduct().getProductName() + " x " + ip.getQuantity());
        }

        System.out.println("Faktury zawierające produkt: " + p1.getProductName());
        for (InvoiceProduct ip : p1.getInvoiceProducts()) {
            System.out.println(" - " + ip.getInvoice().getInvoiceNumber() + " (ilość: " + ip.getQuantity() + ")");
        }

        em.close();
        emf.close();
    }
}
