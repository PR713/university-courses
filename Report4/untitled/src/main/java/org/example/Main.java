package org.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class Main {
    private static SessionFactory sessionFactory = null;

    public static void main(String[] args) {
        sessionFactory = getSessionFactory();
        Session session = sessionFactory.openSession();

        Product product = new Product("Kredki", 123);
        Transaction tx = session.beginTransaction();
        session.persist(product);
        tx.commit();

        session.close();
    }

    private static SessionFactory getSessionFactory() {
        if (sessionFactory == null) {
            Configuration configuration = new Configuration();
            configuration.addAnnotatedClass(Product.class); // Register the entity
            sessionFactory = configuration.configure().buildSessionFactory();
        }
        return sessionFactory;
    }
}
