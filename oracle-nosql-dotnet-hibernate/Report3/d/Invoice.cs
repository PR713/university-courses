using System;
using System.Collections.Generic;

public class Invoice
{
    public int InvoiceID { get; set; }
    public DateTime Date { get; set; }

    public List<InvoiceProduct>? InvoiceProducts { get; set; }
}
