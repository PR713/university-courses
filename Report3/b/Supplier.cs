using System.Collections.Generic;

public class Supplier
{
    public int SupplierID { get; set; }
    public string CompanyName { get; set; }
    public string Street { get; set; }
    public string City { get; set; }

    public List<Product>? Products { get; set; }
}
