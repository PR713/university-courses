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
