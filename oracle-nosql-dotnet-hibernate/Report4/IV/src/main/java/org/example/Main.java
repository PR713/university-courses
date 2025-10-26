package org.example;

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
        Supplier otherSupp = new Supplier("Outpost", "Armii","Mysłowice");
        Product productTest1 = new Product("kredka", 123);
        Product productTest2 = new Product("baton", 10);
        Product productTest3 = new Product("koszulka", 1);
        Product productTest4 = new Product("pisaki", 2);
        Category category1 = new Category("Żywność");
        Category category2 = new Category("Akcesoria");
        Category category3 = new Category("Ubrania");

        session.persist(category1);
        session.persist(category2);
        session.persist(category3);
        session.persist(supplier);
        session.persist(otherSupp);

        productTest1.setCategory(category2);
        productTest2.setCategory(category1);
        productTest3.setCategory(category3);
        productTest4.setCategory(category2);

        productTest1.setSupplier(supplier);
        productTest2.setSupplier(otherSupp);
        productTest3.setSupplier(supplier);
        productTest4.setSupplier(otherSupp);

        category1.addProduct(productTest2);
        category2.addProduct(productTest1);
        category2.addProduct(productTest4);
        category3.addProduct(productTest3);

        session.persist(productTest1);
        session.persist(productTest2);
        session.persist(productTest3);
        session.persist(productTest4);

        List<Product> products = session.createQuery("from Product", Product.class).getResultList();

        session.createQuery("from Category", Category.class).getResultList()
                .forEach(cat -> {
                    System.out.println("Kategoria: " + cat);
                    cat.getProducts().forEach(p -> {
                        System.out.println("Product: " + p);
                    });
                    System.out.println("\n");
                });

        tx.commit();

//        for (Category category : categories) { //kategorie i ich produkty jeśli zrobilibyśmy jak dla products wyżej
//            System.out.println("Kategoria: " + category + " ");
//            for (Product product : category.getProducts()) {
//                System.out.println(product);
//            }
//        }

        for (Product p : products) { //produkty i ich kategorie
            System.out.println("Produkt '" + p + "' jest dostarczany przez dostawcę '" + p.getSupplier() + "'"
                    + " i należy do kategorii '" + p.getCategory() + "'");
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
