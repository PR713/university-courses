package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class Main {
    public static void main(String[] args) {
        Configuration config = new Configuration().configure();
        SessionFactory sessionFactory = config.buildSessionFactory();

        try (Session session = sessionFactory.openSession()) {
            session.beginTransaction();

            Product p1 = new Product("Młotek", 30);
            Product p2 = new Product("Wiertarka", 20);

            Invoice i1 = new Invoice("FV/001");
            Invoice i2 = new Invoice("FV/002");

            session.persist(p1);
            session.persist(p2);
            session.persist(i1);
            session.persist(i2);

            InvoiceProduct ip1 = new InvoiceProduct(i1, p1, 5); // młotek w FV/001
            InvoiceProduct ip2 = new InvoiceProduct(i1, p2, 2); // wiertarka w FV/001
            InvoiceProduct ip3 = new InvoiceProduct(i2, p1, 1); // młotek w FV/002

            session.persist(ip1);
            session.persist(ip2);
            session.persist(ip3);

            session.getTransaction().commit();

            session.beginTransaction();

            Invoice loadedInvoice = session.createQuery(
                            "FROM Invoice i WHERE i.invoiceNumber = :nr", Invoice.class)
                    .setParameter("nr", "FV/001")
                    .getSingleResult();

            System.out.println("Produkty z faktury " + loadedInvoice.getInvoiceNumber() + ":");
            for (InvoiceProduct ip : loadedInvoice.getInvoiceProducts()) {
                System.out.println(" - " + ip.getProduct().getProductName() +
                        " x " + ip.getQuantity());
            }

            Product loadedProduct = session.createQuery(
                            "FROM Product p WHERE p.productName = :name", Product.class)
                    .setParameter("name", "Młotek")
                    .getSingleResult();

            System.out.println("Faktury zawierające produkt: " + loadedProduct.getProductName());
            for (InvoiceProduct ip : loadedProduct.getInvoiceProducts()) {
                System.out.println(" - " + ip.getInvoice().getInvoiceNumber() +
                        " (ilość: " + ip.getQuantity() + ")");
            }

            session.getTransaction().commit();
        }

        sessionFactory.close();
    }
}
