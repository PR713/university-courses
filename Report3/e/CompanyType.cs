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