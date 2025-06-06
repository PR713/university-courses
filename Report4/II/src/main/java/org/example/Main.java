package org.example;

import jakarta.persistence.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class Main {
    private static SessionFactory sessionFactory = null;

    public static void main(String[] args) {
        sessionFactory = getSessionFactory();
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();

        Supplier supplier = new Supplier("Extra dostawca", "Tokarskiego", "Kraków");
        Product productTest = new Product("kredka", 123);

        session.persist(productTest);

        Product product = session.get(Product.class, 1);
        product.setSupplier(supplier);
        session.persist(supplier);
        tx.commit();

        List<Product> products = session.createQuery("from Product", Product.class).getResultList();

        for (Product p : products) {
            System.out.println("Produkt '" + p + "' jest dostarczany przez dostawcę '" + p.getSupplier() + "'");
        }
        session.close();
    }

    public static SessionFactory getSessionFactory() {
        if (sessionFactory == null) {
            try {
                Configuration configuration = new Configuration();
                configuration.configure();
                sessionFactory = configuration.buildSessionFactory();
            } catch (Throwable ex) {
                throw new ExceptionInInitializerError(ex);
            }
        }
        return sessionFactory;
    }
}
