# Sprawozdanie Entity Framework

### Autorzy: Radosław Szepielak, Kacper Wdowiak

## Część 1:
Poniżej przedstawiamy zrzuty ekranu wykonania pracy podczas zajęć:
![alt text](./Zrzut%20ekranu%202025-05-16%20141402.png)
![alt text](./Zrzut%20ekranu%202025-05-16%20141415.png)
![alt text](./Zrzut%20ekranu%202025-05-16%20143727.png)
![alt text](./Zrzut%20ekranu%202025-05-16%20143821.png)


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

![alt text](./Zrzut%20ekranu%202025-05-22%20152502.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20152825.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20153116.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20153648.png)



<br><br>

### Zadanie b: 
Realizację zadania b) przedstawia kod poniżej:
```csharp
```
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

```
![alt text](./Zrzut%20ekranu%202025-05-22%20155000.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20155103.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20155200.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20155224.png)



<br><br>

### Zadanie d:
Realizację zadania d) przedstawia kod poniżej:
```csharp
```

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

```csharp
public class Supplier : Company
{
    public string BankAccountNumber { get; set; }
}
```
![alt text](./Zrzut%20ekranu%202025-05-22%20165513.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20165519.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20165716.png)
![alt text](./Zrzut%20ekranu%202025-05-22%20165446.png)




<br><br>

### Zadanie f: 

Realizację zadania f) przedstawia kod poniżej:

```csharp
```