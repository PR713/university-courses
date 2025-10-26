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
