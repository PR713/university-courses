using System;

Console.WriteLine("Podaj nazwę produktu: ");
String? prodName = Console.ReadLine();

ProdContext productContext = new ProdContext();
Product product = new Product { ProductName = prodName };
productContext.Products.Add(product);
productContext.SaveChanges();


var query = from prod in productContext.Products
            select prod.ProductName;


foreach (var pName in query)
{
Console.WriteLine(pName);
}