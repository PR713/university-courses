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
