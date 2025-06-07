package org.example;

import jakarta.persistence.*;

public class Main {
    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("my-jpa-unit");
        EntityManager em = emf.createEntityManager();

        em.getTransaction().begin();

        Product p1 = new Product("Młotek", 100);
        Product p2 = new Product("Wkrętarka", 50);
        Product p3 = new Product("Piła", 25);

        Invoice invoice = new Invoice("FV/2025/001");

        invoice.getInvoiceProducts().add(new InvoiceProduct(invoice, p1, 10));
        invoice.getInvoiceProducts().add(new InvoiceProduct(invoice, p2, 5));
        invoice.getInvoiceProducts().add(new InvoiceProduct(invoice, p3, 3));

        em.persist(p1);
        em.persist(p2);
        em.persist(p3);
        em.persist(invoice);

        em.getTransaction().commit();

        System.out.println("=== Zapisano fakturę: " + invoice.getInvoiceNumber());
        for (InvoiceProduct ip : invoice.getInvoiceProducts()) {
            System.out.println(" → " + ip.getQuantity() + " x " + ip.getProduct().getName());
        }

        em.getTransaction().begin();
        System.out.println("\n=== Odczyt z bazy:");
        Invoice found = em.find(Invoice.class, invoice.getId());
        System.out.println("Faktura: " + found.getInvoiceNumber());
        for (InvoiceProduct ip : found.getInvoiceProducts()) {
            System.out.println(" • " + ip.getQuantity() + " x " + ip.getProduct().getName());
        }
        em.getTransaction().commit();

        em.close();
        emf.close();
    }
}
