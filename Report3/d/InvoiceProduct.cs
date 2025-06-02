public class InvoiceProduct
{
    public int ProductID { get; set; }
    public Product Product { get; set; }

    public int InvoiceID { get; set; }
    public Invoice Invoice { get; set; }

    public int Quantity { get; set; }  // <-- kluczowe pole zgodne z diagramem
}
