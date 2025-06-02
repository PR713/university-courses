public class Product
{
    public int ProductID { get; set; }
    public string? ProductName { get; set; }
    public int UnitsInStock { get; set; }

    public List<InvoiceProduct>? InvoiceProducts { get; set; }
}
