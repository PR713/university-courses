# Sprawozdanie Entity Framework

### Autorzy: Radosław Szepielak, Kacper Wdowiak

## Część 1:
Poniżej przedstawiamy zrzuty ekranu wykonania pracy podczas zajęć:
![alt text](./zrzuty_ekranu/part1/Zrzut%20ekranu%202025-05-16%20141402.png)
![alt text](./zrzuty_ekranu/part1/Zrzut%20ekranu%202025-05-16%20141415.png)
![alt text](./zrzuty_ekranu/part1/Zrzut%20ekranu%202025-05-16%20143727.png)
![alt text](./zrzuty_ekranu/part1/Zrzut%20ekranu%202025-05-16%20143821.png)


<br><br>
<br><br>


## Część 2:

### Zadanie a: Modyfikacja modelu i wprowadzenie Dostawcy (is supplied by)
Realizację zadania a) przedstawia kod poniżej:
```csharp
public class Product
{
    public int ProductID { get; set; }
    public String? ProductName { get; set; }
    public int UnitsInStock { get; set; }

    public Supplier? Supplier { get; set; } = null;
}
```
```csharp
public class Supplier
{
    public int SupplierID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }

}
```
```csharp
using Microsoft.EntityFrameworkCore;
public class ProdContext : DbContext
{
public DbSet<Product> Products { get; set; }
public DbSet<Supplier> Suppliers { get; set; }
protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
{
    base.OnConfiguring(optionsBuilder);
    optionsBuilder.UseSqlite("Datasource=MyProductDatabase");
}
}
```
```csharp
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
```

Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

![alt text](./zrzuty_ekranu/a\)/Zrzut%20ekranu%202025-05-22%20152502.png)
![alt text](./zrzuty_ekranu/a\)/Zrzut%20ekranu%202025-05-22%20152825.png)
![alt text](./zrzuty_ekranu/a\)/Zrzut%20ekranu%202025-05-22%20153116.png)
![alt text](./zrzuty_ekranu/a\)/Zrzut%20ekranu%202025-05-22%20153648.png)



<br><br>

### Zadanie b: 
Realizację zadania b) przedstawia kod poniżej:
```csharp
public class Product
{
    public int ProductID { get; set; }
    public String? ProductName { get; set; }
    public int UnitsInStock { get; set; }
}
```

```csharp
using System.Collections.Generic;

public class Supplier
{
    public int SupplierID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }

    public List<Product>? Products { get; set; }
}
```

```csharp
using Microsoft.EntityFrameworkCore;

public class ProdContext : DbContext
{
    public DbSet<Product> Products { get; set; }
    public DbSet<Supplier> Suppliers { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        base.OnConfiguring(optionsBuilder);
        optionsBuilder.UseSqlite("Datasource=MyProductDatabase_b.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<Supplier>()
            .HasMany(s => s.Products)
            .WithOne()
            .HasForeignKey("SupplierID")
            .OnDelete(DeleteBehavior.Cascade);
    }
}
```

```csharp
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
```
Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

![alt text](./zrzuty_ekranu/b\)/b1.png)
![alt text](./zrzuty_ekranu/b\)/b2.png)
![alt text](./zrzuty_ekranu/b\)/b3.png)
![alt text](./zrzuty_ekranu/b\)/b4.png)
![alt text](./zrzuty_ekranu/b\)/b5.png)



<br><br>

### Zadanie c: Zamodelowanie relacji dwustronnej (supplies & is supplied by)
Realizację zadania c) przedstawia kod poniżej:

```csharp
public class Product
{
    public int ProductID { get; set; }
    public String? ProductName { get; set; }
    public int UnitsInStock { get; set; }

    public Supplier? Supplier { get; set; } = null;
}

```
```csharp
public class Supplier
{
    public int SupplierID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }

    public ICollection<Product> Products { get; set; } = new List<Product>();

}
```

```csharp
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
        supplier.Products.Add(product); // nowa linia w c)

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



Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

```
![alt text](./zrzuty_ekranu/c\)/Zrzut%20ekranu%202025-05-22%20155000.png)
![alt text](./zrzuty_ekranu/c\)/Zrzut%20ekranu%202025-05-22%20155103.png)
![alt text](./zrzuty_ekranu/c\)/Zrzut%20ekranu%202025-05-22%20155200.png)
![alt text](./zrzuty_ekranu/c\)/Zrzut%20ekranu%202025-05-22%20155224.png)



<br><br>

### Zadanie d:
Realizację zadania d) przedstawia kod poniżej:
```csharp
public class Product
{
    public int ProductID { get; set; }
    public string? ProductName { get; set; }
    public int UnitsInStock { get; set; }

    public List<InvoiceProduct>? InvoiceProducts { get; set; }
}
```

```csharp
using System;
using System.Collections.Generic;

public class Invoice
{
    public int InvoiceID { get; set; }
    public DateTime Date { get; set; }

    public List<InvoiceProduct>? InvoiceProducts { get; set; }
}
```

```csharp
public class InvoiceProduct
{
    public int ProductID { get; set; }
    public Product Product { get; set; }

    public int InvoiceID { get; set; }
    public Invoice Invoice { get; set; }

    public int Quantity { get; set; }
}
```

```csharp
using Microsoft.EntityFrameworkCore;

public class ProdContext : DbContext
{
    public DbSet<Product> Products { get; set; }
    public DbSet<Invoice> Invoices { get; set; }
    public DbSet<InvoiceProduct> InvoiceProducts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Datasource=MyProductDatabase_d.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<InvoiceProduct>()
            .HasKey(ip => new { ip.ProductID, ip.InvoiceID });

        modelBuilder.Entity<InvoiceProduct>()
            .HasOne(ip => ip.Product)
            .WithMany(p => p.InvoiceProducts)
            .HasForeignKey(ip => ip.ProductID);

        modelBuilder.Entity<InvoiceProduct>()
            .HasOne(ip => ip.Invoice)
            .WithMany(i => i.InvoiceProducts)
            .HasForeignKey(ip => ip.InvoiceID);
    }
}
```

```csharp
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
```

Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

![alt text](./zrzuty_ekranu/d\)/d1.png)
![alt text](./zrzuty_ekranu/d\)/d2.png)
![alt text](./zrzuty_ekranu/d\)/d3.png)
![alt text](./zrzuty_ekranu/d\)/d4.png)
![alt text](./zrzuty_ekranu/d\)/d5.png)
![alt text](./zrzuty_ekranu/d\)/d6.png)
![alt text](./zrzuty_ekranu/d\)/d7.png)


<br><br>

### Zadanie e: Wprowadzenie do modelu hierarchii dziedziczenia używając strategii Table-Per-Hierarchy
Realizację zadania e) przedstawia kod poniżej:

```csharp

public abstract class Company
{
    public int CompanyID { get; set; }
    public string CompanyName { get; set; } = String.Empty;
    public string Street { get; set; } = String.Empty;
    public string City { get; set; } = String.Empty;
    public string ZipCode { get; set; } = String.Empty;
}
```

```csharp
using Microsoft.EntityFrameworkCore;

public class CompanyContext : DbContext
{
  public DbSet<Company>? Companies { get; set; }
  public DbSet<Supplier>? Suppliers { get; set; }
  public DbSet<Customer>? Customers { get; set; }

  protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
  {
    base.OnConfiguring(optionsBuilder);
    optionsBuilder.UseSqlite("Datasource=CompaniesDatabase.db");
  }
}
```

```csharp
public static class CompanyType
  {
    public const string CUSTOMER = "customer";
    public const string SUPPLIER = "supplier";

    public static List<string> COMPANY_TYPES = new()
        {
            CUSTOMER,
            SUPPLIER
        };
  }
```

```csharp
public class Customer : Company
  {
    public float Discount { get; set; }
  }
```

```csharp
using System;

class Program
{

    static void Main()
    {

        using CompanyContext companyContext = new();
        Console.WriteLine("Wybierz co chcesz zrobić (add/display): \n");
        String? action = Console.ReadLine();


        switch (action)
        {
            case "add":
                AddCompany(companyContext);
                break;
            case "display":
                DisplayCompanies(companyContext);
                break;
        }
    }

    private static void AddCompany(CompanyContext companyContext)
    {
        while (true)
        {
            Console.WriteLine("\nWybierz rodzaj firmy, którą chciałbyś dodać: \n");
            foreach (string companyType in CompanyType.COMPANY_TYPES) Console.WriteLine($"-{companyType}");
            String? type = Console.ReadLine();
            Console.WriteLine("Podaj nazwę firmy: \n");
            String? companyName = Console.ReadLine();
            Console.WriteLine("Podaj miasto: \n");
            String? city = Console.ReadLine();
            Console.WriteLine("Podaj ulicę i nr: \n");
            String? street = Console.ReadLine();
            Console.WriteLine("Podaj kod pocztowy: \n");
            String? postalCode = Console.ReadLine();


            switch (type)
            {
                case CompanyType.CUSTOMER:
                    companyContext.Companies.Add(CreateCustomer(companyName, street, city, postalCode));
                    companyContext.SaveChanges();
                    return;
                case CompanyType.SUPPLIER:
                    companyContext.Companies.Add(CreateSupplier(companyName, street, city, postalCode));
                    companyContext.SaveChanges();
                    return;
            }
        }
    }


    private static Customer CreateCustomer(string companyName, string street, string city, string postalCode)
    {
        Console.WriteLine("Podaj wartość zniżki (0.0-1.0)\n ");

        float discount = float.Parse(Console.ReadLine());

        return new Customer
        {
            CompanyName = companyName,
            Street = street,
            City = city,
            ZipCode = postalCode,
            Discount = discount
        };
    }


    private static Supplier CreateSupplier(string companyName, string city, string street, string postalCode)
    {
        Console.WriteLine("Podaj numer konta bankowego: ");
        string bankAccountNumber = Console.ReadLine();

        return new Supplier
        {
            CompanyName = companyName,
            Street = street,
            City = city,
            ZipCode = postalCode,
            BankAccountNumber = bankAccountNumber
        };
    }


    private static void DisplayCompanies(CompanyContext companyContext)
    {
        Console.WriteLine("\nPodaj typ firm, które chcesz wyświetlić:\n -all");
        foreach (string type in CompanyType.COMPANY_TYPES) Console.WriteLine($"-{type}");
        string companyType = Console.ReadLine();


        switch (companyType) {
        case "all":
            Console.WriteLine("Lista wszystkich klientów (firm):");
            foreach (Company company in companyContext.Companies){
                        Console.WriteLine(company);
                }

            break;

        case CompanyType.SUPPLIER:
            Console.WriteLine("Lista wszystkich dostawców (firm):");
            foreach (Supplier supplier in companyContext.Suppliers){
                    Console.WriteLine(supplier);
                }

            break;

        case CompanyType.CUSTOMER:
            Console.WriteLine("Lista wszystkich klientów (firm):");
            foreach (Customer customer in companyContext.Customers){
                    Console.WriteLine(customer);
                }

             break;
      }
    }
}
```


Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

```csharp
public class Supplier : Company
{
    public string BankAccountNumber { get; set; }
}
```
![alt text](./zrzuty_ekranu/e\)/Zrzut%20ekranu%202025-05-22%20165513.png)
![alt text](./zrzuty_ekranu/e\)/Zrzut%20ekranu%202025-05-22%20165519.png)
![alt text](./zrzuty_ekranu/e\)/Zrzut%20ekranu%202025-05-22%20165716.png)
![alt text](./zrzuty_ekranu/e\)/Zrzut%20ekranu%202025-05-22%20165446.png)




<br><br>

### Zadanie f: 

Realizację zadania f) przedstawia kod poniżej:

```csharp
public abstract class Company
{
    public int CompanyID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }
    public string ZipCode { get; set; }
}
```

```csharp
public class Customer : Company
{
    public float Discount { get; set; }
}
```

```csharp
public class Supplier : Company
{
    public string BankAccountNumber { get; set; }
}
```

```csharp
using Microsoft.EntityFrameworkCore;

public class CompanyContext : DbContext
{
    public DbSet<Company> Companies { get; set; }
    public DbSet<Supplier> Suppliers { get; set; }
    public DbSet<Customer> Customers { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlite("Datasource=MyProductDatabase_f.db");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Company>().ToTable("Companies");
        modelBuilder.Entity<Supplier>().ToTable("Suppliers");
        modelBuilder.Entity<Customer>().ToTable("Customers");
    }
}

```

```csharp
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        using var context = new CompanyContext();

        Console.WriteLine("Dodaj firmę jako: supplier czy customer?");
        string? type = Console.ReadLine();

        Console.WriteLine("Podaj nazwę firmy:");
        string name = Console.ReadLine();

        Console.WriteLine("Ulica:");
        string street = Console.ReadLine();

        Console.WriteLine("Miasto:");
        string city = Console.ReadLine();

        Console.WriteLine("Kod pocztowy:");
        string zip = Console.ReadLine();

        if (type == "supplier")
        {
            Console.WriteLine("Podaj numer konta bankowego:");
            string account = Console.ReadLine();

            Supplier supplier = new Supplier
            {
                CompanyName = name,
                Street = street,
                City = city,
                ZipCode = zip,
                BankAccountNumber = account
            };

            context.Suppliers.Add(supplier);
            context.SaveChanges();

            Console.WriteLine("\nDostawcy:");
            foreach (var s in context.Suppliers)
            {
                Console.WriteLine($"[{s.CompanyID}] {s.CompanyName}, {s.City}, {s.Street}, {s.ZipCode}, Konto: {s.BankAccountNumber}");
            }
        }
        else if (type == "customer")
        {
            Console.WriteLine("Podaj wartość rabatu (np. 0.1 dla 10%):");
            float discount = float.Parse(Console.ReadLine());

            Customer customer = new Customer
            {
                CompanyName = name,
                Street = street,
                City = city,
                ZipCode = zip,
                Discount = discount
            };

            context.Customers.Add(customer);
            context.SaveChanges();

            Console.WriteLine("\nKlienci:");
            foreach (var c in context.Customers)
            {
                Console.WriteLine($"[{c.CompanyID}] {c.CompanyName}, {c.City}, {c.Street}, {c.ZipCode}, Rabat: {c.Discount * 100}%");
            }
        }
        else
        {
            Console.WriteLine("Nieznany typ firmy.");
        }
    }
}
```

Poniżej zamieszamy zrzuty ekranu realizacji przez nas powyższego kodu wraz z uzyskanym rezultatem:

![alt text](./zrzuty_ekranu/f\)/f1.png)
![alt text](./zrzuty_ekranu/f\)/f2.png)
![alt text](./zrzuty_ekranu/f\)/f3.png)
![alt text](./zrzuty_ekranu/f\)/f4.png)

<br><br>
<br><br>

### g) Porównanie strategii modelowania dziedziczenia w EF Core: Table-Per-Hierarchy (TPH) vs Table-Per-Type (TPT)

W zadaniach **e** i **f** zaprezentowaliśmy dwie różne strategie modelowania dziedziczenia w Entity Framework Core:

---

#### 1. **Table-Per-Hierarchy (TPH)** – zadanie e)

- **Opis**:
  - Wszystkie klasy dziedziczące z klasy `Company` są przechowywane w jednej wspólnej tabeli `Companies`.
  - Rozróżnienie typów (`Customer`, `Supplier`) odbywa się za pomocą kolumny dyskryminatora.
  - W tabeli występują kolumny specyficzne dla wszystkich typów dziedziczących (np. `Discount`, `BankAccountNumber`), nawet jeśli część z nich pozostaje pusta (null).

- **Zalety**:
  - Lepsza wydajność odczytu – jeden `SELECT` wystarczy do pobrania wszystkich firm bez potrzeby `JOIN`.
  - Prostota struktury bazy danych – tylko jedna tabela.
  - Łatwiejsze zarządzanie, gdy mamy małą liczbę typów dziedziczenia

- **Wady**:
  - Mniejsza zgodność z zasadami normalizacji bazy danych.
  - Trudniejsza kontrola integralności danych – kolumny mogą być null dla niektórych typów.
  - Słaba czytelność schematu przy większej liczbie klas pochodnych.

---

#### 2. **Table-Per-Type (TPT)** – zadanie f)

- **Opis**:
  - Dla każdej klasy dziedziczącej (`Customer`, `Supplier`) tworzona jest osobna tabela (`Customers`, `Suppliers`), która zawiera tylko swoje unikalne kolumny.
  - Tabela `Companies` zawiera wspólne dane bazowej klasy abstrakcyjnej.
  - Pobranie pełnych danych konkretnej firmy wymaga złączenia (`JOIN`) z tabelą bazową.

- **Zalety**:
  - Lepsza normalizacja danych – dane są uporządkowane i logicznie rozdzielone.
  - Łatwiejsza kontrola typów i spójności danych w tabelach.
  - Przejrzystość struktury – każda tabela zawiera tylko istotne dane dla danej klasy.

- **Wady**:
  - Większa złożoność zapytań (JOIN), co może obniżać wydajność.
  - Większy koszt utrzymania przy częstych migracjach i zmianach schematu.
  - Dłuższy czas zapisu i odczytu przy dużej liczbie rekordów i typów.