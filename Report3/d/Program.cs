using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

class Program
{
    static void Main()
    {
        using var context = new ProdContext();

        Console.WriteLine("Wybierz akcję:");
        Console.WriteLine("1 - Dodaj produkt i przypisz do faktury");
        Console.WriteLine("2 - Pokaż produkty z faktury");
        Console.WriteLine("3 - Pokaż faktury produktu");

        string? choice = Console.ReadLine();

        switch (choice)
        {
            case "1":
                AddProductToInvoice(context);
                break;
            case "2":
                ShowProductsOfInvoice(context);
                break;
            case "3":
                ShowInvoicesOfProduct(context);
                break;
            default:
                Console.WriteLine("Nieznana opcja.");
                break;
        }
    }

    static void AddProductToInvoice(ProdContext context)
    {
        Console.WriteLine("Podaj nazwę produktu:");
        string? name = Console.ReadLine();

        Console.WriteLine("Podaj ilość dostępnych sztuk:");
        int stock = int.Parse(Console.ReadLine());

        Product product = new Product { ProductName = name, UnitsInStock = stock };
        context.Products.Add(product);
        context.SaveChanges();

        Console.WriteLine("Czy chcesz przypisać do istniejącej faktury? (tak/nie)");
        string? reuse = Console.ReadLine();

        int invoiceId;
        if (reuse == "tak")
        {
            Console.WriteLine("Podaj ID faktury:");
            invoiceId = int.Parse(Console.ReadLine());
        }
        else
        {
            Invoice invoice = new Invoice { Date = DateTime.Now };
            context.Invoices.Add(invoice);
            context.SaveChanges();
            invoiceId = invoice.InvoiceID;
        }

        Console.WriteLine("Podaj ilość sprzedanych sztuk w tej fakturze:");
        int quantity = int.Parse(Console.ReadLine());

        InvoiceProduct ip = new InvoiceProduct
        {
            ProductID = product.ProductID,
            InvoiceID = invoiceId,
            Quantity = quantity
        };

        context.InvoiceProducts.Add(ip);
        context.SaveChanges();

        Console.WriteLine($"Dodano produkt do faktury {invoiceId} (ilość: {quantity}).");
    }

    static void ShowProductsOfInvoice(ProdContext context)
    {
        Console.WriteLine("Podaj ID faktury:");
        int invoiceId = int.Parse(Console.ReadLine());

        var products = context.InvoiceProducts
            .Include(ip => ip.Product)
            .Where(ip => ip.InvoiceID == invoiceId)
            .ToList();

        Console.WriteLine($"Produkty z faktury {invoiceId}:");
        foreach (var ip in products)
        {
            Console.WriteLine($"- {ip.Product.ProductName}, sprzedano: {ip.Quantity} szt.");
        }
    }

    static void ShowInvoicesOfProduct(ProdContext context)
    {
        Console.WriteLine("Podaj ID produktu:");
        int productId = int.Parse(Console.ReadLine());

        var invoices = context.InvoiceProducts
            .Include(ip => ip.Invoice)
            .Where(ip => ip.ProductID == productId)
            .ToList();

        Console.WriteLine($"Faktury z udziałem produktu {productId}:");
        foreach (var ip in invoices)
        {
            Console.WriteLine($"- Faktura ID: {ip.InvoiceID}, data: {ip.Invoice.Date}, ilość: {ip.Quantity}");
        }
    }
}
