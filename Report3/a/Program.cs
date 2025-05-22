using System;

class Program {

    static void Main()
    {
        Console.WriteLine("Podaj nazwę produktu: \n");
        String? prodName = Console.ReadLine();
        Console.WriteLine("Podaj liczbę dostępnych sztuk: \n");
        int quantity = Int32.Parse(Console.ReadLine());

        ProdContext productContext = new ProdContext();
        Product product = new Product { ProductName = prodName, UnitsInStock = quantity };
        productContext.Products.Add(product);

        bool createdNewSupplier = false;
        bool isValidChoice = false;
        Supplier? supplier = null;

        do
        {
            Console.WriteLine("Czy chcesz dodać nowego dostawcę? (tak/nie)");
            string choice = Console.ReadLine();

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
            }

        } while (!isValidChoice);

        product.Supplier = supplier;

        if (createdNewSupplier) {
            productContext.Suppliers.Add(supplier);
        }

        productContext.Products.Add(product);
        productContext.SaveChanges();
    }


    private static Supplier CreateNewSupplier()
    {
        Console.WriteLine("\n\nuzupełnij nazwę dostawcy: ");
        string companyName = Console.ReadLine();
        Console.WriteLine("\nUzupełnij miasto: ");
        string city = Console.ReadLine();
        Console.WriteLine("\nUzupełnij ulicę: ");


        string street = Console.ReadLine();

        Supplier supplier = new Supplier
        {
            CompanyName = companyName,
            City = city,
            Street = street
        };
        Console.WriteLine($"\n Utworzono pomyślnie dostawcę: {supplier.CompanyName}");
        return supplier;
    }

    private static Supplier FindSupplier(ProdContext productContext) {
        Console.WriteLine("\n Podaj ID istniejącego dostawcy: ");
        int id = Int32.Parse(Console.ReadLine());

        var query = from sup in productContext.Suppliers
                    where sup.SupplierID == id
                    select sup;
        return query.FirstOrDefault();
    }

    private static void ShowAllSuppliers(ProdContext productContext)
    {
      Console.WriteLine("\n Lista wszystkich istniejących dostawców: ");
      foreach (Supplier supplier in productContext.Suppliers)
      {
        Console.WriteLine($"[{supplier.SupplierID}] {supplier.CompanyName}");
      }
    }
}
