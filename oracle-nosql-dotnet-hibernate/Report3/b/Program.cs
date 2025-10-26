using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Podaj nazwę produktu: ");
        string? prodName = Console.ReadLine();

        Console.WriteLine("Podaj liczbę dostępnych sztuk: ");
        int quantity = int.Parse(Console.ReadLine());

        ProdContext productContext = new ProdContext();
        Product product = new Product { ProductName = prodName, UnitsInStock = quantity };

        bool createdNewSupplier = false;
        bool isValidChoice = false;
        Supplier? supplier = null;

        do
        {
            Console.WriteLine("Czy chcesz dodać nowego dostawcę? (tak/nie)");
            string? choice = Console.ReadLine();

            switch (choice)
            {
                case "tak":
                    isValidChoice = true;
                    supplier = CreateNewSupplier();
                    createdNewSupplier = true;
                    break;
                case "nie":
                    isValidChoice = true;
                    ShowAllSuppliers(productContext);
                    supplier = FindSupplier(productContext);
                    break;
                default:
                    Console.WriteLine("Wybierz: tak / nie");
                    break;
            }
        } while (!isValidChoice);

        if (supplier != null)
        {
            if (supplier.Products == null)
                supplier.Products = new System.Collections.Generic.List<Product>();

            supplier.Products.Add(product);

            if (createdNewSupplier)
            {
                productContext.Suppliers.Add(supplier);
            }

            productContext.SaveChanges();
            Console.WriteLine("Produkt został zapisany i przypisany do dostawcy.");
        }
        else
        {
            Console.WriteLine("Nie udało się znaleźć lub utworzyć dostawcy.");
        }
    }

    private static Supplier CreateNewSupplier()
    {
        Console.WriteLine("Uzupełnij nazwę dostawcy: ");
        string companyName = Console.ReadLine();

        Console.WriteLine("Uzupełnij miasto: ");
        string city = Console.ReadLine();

        Console.WriteLine("Uzupełnij ulicę: ");
        string street = Console.ReadLine();

        Supplier supplier = new Supplier
        {
            CompanyName = companyName,
            City = city,
            Street = street
        };

        Console.WriteLine($"\nUtworzono dostawcę: {supplier.CompanyName}");
        return supplier;
    }

    private static Supplier? FindSupplier(ProdContext productContext)
    {
        Console.WriteLine("Podaj ID istniejącego dostawcy: ");
        int id = int.Parse(Console.ReadLine());

        foreach (Supplier s in productContext.Suppliers)
        {
            if (s.SupplierID == id)
                return s;
        }

        return null;
    }

    private static void ShowAllSuppliers(ProdContext productContext)
    {
        Console.WriteLine("Lista wszystkich dostawców:");
        foreach (Supplier supplier in productContext.Suppliers)
        {
            Console.WriteLine($"[{supplier.SupplierID}] {supplier.CompanyName}, {supplier.City}, {supplier.Street}");
        }
    }
}
