public class Supplier
{
    public int SupplierID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }

    public ICollection<Product> Products { get; set; } = new List<Product>();

}