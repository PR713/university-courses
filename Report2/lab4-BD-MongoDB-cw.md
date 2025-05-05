# Dokumentowe bazy danych – MongoDB

Ćwiczenie/zadanie


---

**Imiona i nazwiska autorów:**

--- 

Odtwórz z backupu bazę north0

```
mongorestore --nsInclude='north0.*' ./dump/
```

```
use north0
```


# Zadanie 1 - operacje wyszukiwania danych,  przetwarzanie dokumentów

# a)

stwórz kolekcję  `OrdersInfo`  zawierającą następujące dane o zamówieniach
- pojedynczy dokument opisuje jedno zamówienie

```js
[  
  {  
    "_id": ...
    
    OrderID": ... numer zamówienia
    
    "Customer": {  ... podstawowe informacje o kliencie skladającym  
      "CustomerID": ... identyfikator klienta
      "CompanyName": ... nazwa klienta
      "City": ... miasto 
      "Country": ... kraj 
    },  
    
    "Employee": {  ... podstawowe informacje o pracowniku obsługującym zamówienie
      "EmployeeID": ... idntyfikator pracownika 
      "FirstName": ... imie   
      "LastName": ... nazwisko
      "Title": ... stanowisko  
     
    },  
    
    "Dates": {
       "OrderDate": ... data złożenia zamówienia
       "RequiredDate": data wymaganej realizacji
    }

    "Orderdetails": [  ... pozycje/szczegóły zamówienia - tablica takich pozycji 
      {  
        "UnitPrice": ... cena
        "Quantity": ... liczba sprzedanych jednostek towaru
        "Discount": ... zniżka  
        "Value": ... wartośc pozycji zamówienia
        "product": { ... podstawowe informacje o produkcie 
          "ProductID": ... identyfikator produktu  
          "ProductName": ... nazwa produktu 
          "QuantityPerUnit": ... opis/opakowannie
          "CategoryID": ... identyfikator kategorii do której należy produkt
          "CategoryName" ... nazwę tej kategorii
        },  
      },  
      ...   
    ],  

    "Freight": ... opłata za przesyłkę
    "OrderTotal"  ... sumaryczna wartosc sprzedanych produktów

    "Shipment" : {  ... informacja o wysyłce
        "Shipper": { ... podstawowe inf o przewoźniku 
           "ShipperID":  
            "CompanyName":
        }  
        ... inf o odbiorcy przesyłki
        "ShipName": ...
        "ShipAddress": ...
        "ShipCity": ... 
        "ShipCountry": ...
    } 
  } 
]  
```


# b)

stwórz kolekcję  `CustomerInfo`  zawierającą następujące dane kazdym klencie
- pojedynczy dokument opisuje jednego klienta

```js
[  
  {  
    "_id": ...
    
    "CustomerID": ... identyfikator klienta
    "CompanyName": ... nazwa klienta
    "City": ... miasto 
    "Country": ... kraj 

	"Orders": [ ... tablica zamówień klienta o strukturze takiej jak w punkcie a) (oczywiście bez informacji o kliencie)
	  
	]

		  
]  
```

# c) 

Napisz polecenie/zapytanie: Dla każdego klienta pokaż wartość zakupionych przez niego produktów z kategorii 'Confections'  w 1997r
- Spróbuj napisać to zapytanie wykorzystując
	- oryginalne kolekcje (`customers, orders, orderdertails, products, categories`)
	- kolekcję `OrderInfo`
	- kolekcję `CustomerInfo`

- porównaj zapytania/polecenia/wyniki

```js
[  
  {  
    "_id": 
    
    "CustomerID": ... identyfikator klienta
    "CompanyName": ... nazwa klienta
	"ConfectionsSale97": ... wartość zakupionych przez niego produktów z kategorii 'Confections'  w 1997r

  }		  
]  
```

# d)

Napisz polecenie/zapytanie:  Dla każdego klienta poaje wartość sprzedaży z podziałem na lata i miesiące
Spróbuj napisać to zapytanie wykorzystując
	- oryginalne kolekcje (`customers, orders, orderdertails, products, categories`)
	- kolekcję `OrderInfo`
	- kolekcję `CustomerInfo`

- porównaj zapytania/polecenia/wyniki

```js
[  
  {  
    "_id": 
    
    "CustomerID": ... identyfikator klienta
    "CompanyName": ... nazwa klienta

	"Sale": [ ... tablica zawierająca inf o sprzedazy
	    {
            "Year":  ....
            "Month": ....
            "Total": ...	    
	    }
	    ...
	]
  }		  
]  
```

# e)

Załóżmy że pojawia się nowe zamówienie dla klienta 'ALFKI',  zawierające dwa produkty 'Chai' oraz "Ikura"
- pozostałe pola w zamówieniu (ceny, liczby sztuk prod, inf o przewoźniku itp. możesz uzupełnić wg własnego uznania)
Napisz polecenie które dodaje takie zamówienie do bazy
- aktualizując oryginalne kolekcje `orders`, `orderdetails`
- aktualizując kolekcję `OrderInfo`
- aktualizując kolekcję `CustomerInfo`

Napisz polecenie 
- aktualizując oryginalną kolekcję orderdetails`
- aktualizując kolekcję `OrderInfo`
- aktualizując kolekcję `CustomerInfo`

# f)

Napisz polecenie które modyfikuje zamówienie dodane w pkt e)  zwiększając zniżkę  o 5% (dla każdej pozycji tego zamówienia) 

Napisz polecenie 
- aktualizując oryginalną kolekcję `orderdetails`
- aktualizując kolekcję `OrderInfo`
- aktualizując kolekcję `CustomerInfo`



UWAGA:
W raporcie należy zamieścić kod poleceń oraz uzyskany rezultat, np wynik  polecenia `db.kolekcka.fimd().limit(2)` lub jego fragment


## Zadanie 1  - rozwiązanie

> Wyniki: 
> 
> przykłady, kod, zrzuty ekranów, komentarz ...

a)

```js
db.orders.aggregate([
    { $lookup: {
        from: "customers",
        localField: "CustomerID",
        foreignField: "CustomerID",
        as: "Customer"
    }},
    { $unwind: "$Customer" },
    { $lookup: {
        from: "employees",
        localField: "EmployeeID",
        foreignField: "EmployeeID",
        as: "Employee"
    }},
    { $unwind: "$Employee" },
    { $lookup: {
        from: "orderdetails",
        localField: "OrderID",
        foreignField: "OrderID",
        as: "Orderdetails"
    }},
    { $lookup: {
        from: "shippers",
        localField: "ShipVia",
        foreignField: "ShipperID",
        as: "Shipper"
    }},
    { $unwind: { path: "$Shipper", preserveNullAndEmptyArrays: true } },
    { $unwind: { path: "$Orderdetails", preserveNullAndEmptyArrays: true } },
    { $lookup: {
        from: "products",
        localField: "Orderdetails.ProductID",
        foreignField: "ProductID",
        as: "Product"
    }},
    { $unwind: "$Product" },
    { $lookup: {
        from: "categories",
        localField: "Product.CategoryID",
        foreignField: "CategoryID",
        as: "ProdCat"
    }},
    { $unwind: "$ProdCat"},
    { $addFields: {
        "Orderdetails.product": {
          ProductID: "$Product.ProductID",
          ProductName: "$Product.ProductName",
          QuantityPerUnit: "$Product.QuantityPerUnit",
          CategoryID: "$Product.CategoryID",
          CategoryName: "$ProdCat.CategoryName"
        },
        "Orderdetails.Value": {
          $multiply: [
            "$Orderdetails.UnitPrice",
            "$Orderdetails.Quantity",
            { $subtract: [1, "$Orderdetails.Discount"] }
          ]
        }
    }},
    { $group: {
        _id: "$OrderID",
        OrderID: { $first: "$OrderID" },
        Customer: { $first: {
          CustomerID: "$Customer.CustomerID",
          CompanyName: "$Customer.CompanyName",
          City: "$Customer.City",
          Country: "$Customer.Country"
        }},
        Employee: { $first: {
          EmployeeID: "$Employee.EmployeeID",
          FirstName: "$Employee.FirstName",
          LastName: "$Employee.LastName",
          Title: "$Employee.Title"
        }},
        Dates: { $first: {
          OrderDate: "$OrderDate",
          RequiredDate: "$RequiredDate"
        }},
        Freight: { $first: "$Freight" },
        Orderdetails: { $push: {
          UnitPrice: "$Orderdetails.UnitPrice",
          Quantity: "$Orderdetails.Quantity",
          Discount: "$Orderdetails.Discount",
          Value: "$Orderdetails.Value",
          product: "$Orderdetails.product"
        }},
        Shipment: { $first: {
          Shipper: {
            ShipperID: "$Shipper.ShipperID",
            CompanyName: "$Shipper.CompanyName"
          },
          ShipName: "$ShipName",
          ShipAddress: "$ShipAddress",
          ShipCity: "$ShipCity",
          ShipCountry: "$ShipCountry"
        }}
    }},
    { $addFields: { 
        OrderTotal: { $sum: "$Orderdetails.Value" }
    }},
    { $project: {
        _id: 1,
        OrderID: 1,
        Customer: 1,
        Employee: 1,
        Dates: 1,
        Orderdetails: 1,
        Freight: 1,
        OrderTotal: 1,
        Shipment: 1
    }},
    {
      $out: "OrderInfo"
    }
  ])
```

b)


```js
db.customers.aggregate([
    {
      $lookup: {
        from: "orders",
        localField: "CustomerID",
        foreignField: "CustomerID",
        as: "Orders"
      }
    },
    { $unwind: "$Orders" },
    {
      $lookup: {
        from: "employees",
        localField: "Orders.EmployeeID",
        foreignField: "EmployeeID",
        as: "Employee"
      }
    },
    { $unwind: "$Employee" },
    {
      $lookup: {
        from: "shippers",
        localField: "Orders.ShipVia",
        foreignField: "ShipperID",
        as: "Shipper"
      }
    },
    { $unwind: "$Shipper" },
    {
      $lookup: {
        from: "orderdetails",
        localField: "Orders.OrderID",
        foreignField: "OrderID",
        as: "Details"
      }
    },
    { $unwind: "$Details" },
    {
      $lookup: {
        from: "products",
        localField: "Details.ProductID",
        foreignField: "ProductID",
        as: "Product"
      }
    },
    { $unwind: "$Product" },
    {
      $lookup: {
        from: "categories",
        localField: "Product.CategoryID",
        foreignField: "CategoryID",
        as: "Category"
      }
    },
    { $unwind: "$Category" },
    {
      $addFields: {
        "Details.Value": {
          $multiply: [
            "$Details.UnitPrice",
            "$Details.Quantity",
            { $subtract: [1, "$Details.Discount"] }
          ]
        },
        "Details.Product": {
          ProductID: "$Product.ProductID",
          ProductName: "$Product.ProductName",
          QuantityPerUnit: "$Product.QuantityPerUnit",
          CategoryID: "$Category.CategoryID",
          CategoryName: "$Category.CategoryName"
        }
      }
    },
    {
      $group: {
        _id: {
          CustomerID: "$CustomerID",
          OrderID: "$Orders.OrderID"
        },
        CompanyName: { $first: "$CompanyName" },
        City: { $first: "$City" },
        Country: { $first: "$Country" },
        Employee: {
          $first: {
            EmployeeID: "$Employee.EmployeeID",
            FirstName: "$Employee.FirstName",
            LastName: "$Employee.LastName",
            Title: "$Employee.Title"
          }
        },
        Dates: {
          $first: {
            OrderDate: "$Orders.OrderDate",
            RequiredDate: "$Orders.RequiredDate"
          }
        },
        Freight: { $first: "$Orders.Freight" },
        Shipment: {
          $first: {
            Shipper: {
              ShipperID: "$Shipper.ShipperID",
              CompanyName: "$Shipper.CompanyName"
            },
            ShipName: "$Orders.ShipName",
            ShipAddress: "$Orders.ShipAddress",
            ShipCity: "$Orders.ShipCity",
            ShipCountry: "$Orders.ShipCountry"
          }
        },
        OrderDetails: { $push: "$Details" },
        OrderTotal: {
          $sum: "$Details.Value"
        }
      }
    },
    {
      $group: {
        _id: "$_id.CustomerID",
        CustomerID: { $first: "$_id.CustomerID" },
        CompanyName: { $first: "$CompanyName" },
        City: { $first: "$City" },
        Country: { $first: "$Country" },
        Orders: {
          $push: {
            OrderID: "$_id.OrderID",
            Employee: "$Employee",
            Dates: "$Dates",
            Freight: "$Freight",
            Shipment: "$Shipment",
            Orderdetails: "$OrderDetails",
            OrderTotal: "$OrderTotal"
          }
        }
      }
    },
    {
      $project: {
        _id: 1,
        CustomerID: 1,
        CompanyName: 1,
        City: 1,
        Country: 1,
        Orders: 1
      }
    },
    {
      $out: "CustomerInfo"
    }
  ])
```

c)


```js
--  ...
```

d)


```js
db.orders.aggregate([ //orignalne kolekcje
    {
        $lookup: {
            from: "customers",
            localField: "CustomerID",
            foreignField: "CustomerID",
            as: "Customer"
        }
    },
    { $unwind: "$Customer"},

    {
        $lookup: {
            from: "orderdetails",
            localField: "OrderID",
            foreignField: "OrderID",
            as: "Orderdetails"
        }
    },
    { $unwind: "$Orderdetails"},

    {
        $project: {
            CustomerID: "$Customer.CustomerID",
            CompanyName: "$Customer.CompanyName",
            OrderDate: "$OrderDate", //z orders
            TotalSale: {
                $multiply: [
                    "$Orderdetails.UnitPrice",
                    "$Orderdetails.Quantity",
                    { $subtract: [1, "$Orderdetails.Discount"]}
                ]
            }
        }
    },

    {
        $addFields: {
            Year: { $year: "$OrderDate"},
            Month: { $month: "$OrderDate"},
        }
    },

    {
        $group: {
            _id: { CustomerID: "$CustomerID", Year: "$Year", Month: "$Month"},
            CustomerID: { $first: "$CustomerID"},
            CompanyName: { $first: "$CompanyName"},
            TotalSale: { $sum: "$TotalSale"} //wie z jakie sumować bo wcześniej TotalSale
            //było z danym CustomerID w $project
        }
    },

    {
        $group: {
            _id: { CustomerID: "$CustomerID" } ,
            CompanyName: { $first: "$CompanyName" },
            Sales: {
                $push: {
                    Year: "$_id.Year",
                    Month: "$_id.Month",
                    Total: "$TotalSale"
                }
            }
        }
    },

    {
        $project: {
            _id: 1,
            CustomerID: "$_id.CustomerID",
            CompanyName: "$CompanyName",
            Sales: 1
          }
    }

])



//----------------

db.OrderInfo.aggregate([
    {
      $unwind: "$Orderdetails"
    }, //niepotrzebne
    {
      $addFields: {
        Year: { $year: "$Dates.OrderDate" },
        Month: { $month: "$Dates.OrderDate" }
      }
    },
    {
      $group: {
        _id: { CustomerID: "$Customer.CustomerID", Year: "$Year", Month: "$Month" },
        CustomerID: { $first: "$Customer.CustomerID" },
        CompanyName: { $first: "$Customer.CompanyName" },
        TotalSale: { $sum: "$Orderdetails.Value" }
      }
    },
    {
      $group: {
        _id: {CustomerID: "$CustomerID"},//z zakresu wyżej dostępny
        CompanyName: { $first: "$CompanyName" },
        Sales: {
          $push: {
            Year: "$_id.Year",
            Month: "$_id.Month",
            Total: "$TotalSale"
          }
        }
      }
    },
    {
      $project: {
        _id: 1,
        CustomerID: "$_id.CustomerID", //wyżej tylko w _id
        CompanyName: "$CompanyName",
        Sales: 1
      }
    }
  ])
  



  //------------------ todo ogarnąć : 

  db.CustomerInfo.aggregate([
    {
      $unwind: "$Orders"
    },

    {
      $addFields: {
        Year: { $year: "$Orders.Dates.OrderDate"},
        Month: { $month: "$Orders.Dates.OrderDate"}
      }
    },
    {
      $group: {
        _id: { CustomerID: "$CustomerID", Year: "$Year", Month: "$Month" },
        CustomerID: { $first: "$CustomerID" },
        CompanyName: { $first: "$CompanyName" },
        TotalSale: { $sum: "$Orders.OrderTotal" }
      }
    },
    {
      $group: {
        _id: {CustomerID: "$CustomerID"},
        CompanyName: { $first: "$CompanyName" },
        Sales: {
          $push: {
            Year: "$_id.Year",
            Month: "$_id.Month",
            Total: "$TotalSale"
          }
        }
      }
    },
    {
      $project: {
        _id: 0,
        CustomerID: "$_id.CustomerID",
        CompanyName: "$CompanyName",
        Sales: 1
      }
    }
  ])
  
```

e)


```js
db.orders.insertOne({
    OrderID: 11078,
    EmployeeID: 5,
    OrderDate: new Date("2025-04-16"),
    RequiredDate: new Date("2025-04-23"),
    ShippedDate: null,
    ShipVia: 2,
    Freight: 20,
    ShipName: "Alfreds Futterkiste",
    ShipAddress: "Obere Str. 57",
    ShipCity: "Berlin",
    ShipRegion: null,
    ShipPostalCode: "12209",
    ShipCountry: "Germany"
})



db.orderdetails.insertMany([
    {
        OrderID: 11078,
        ProductID: 1,
        UnitPrice: 18,
        Quantity: 10,
        Discount: 0.1
    },
    {
        OrderID: 11078,
        ProductID: 10,
        UnitPrice: 31,
        Quantity: 5,
        Discount: 0
    }
])




/////////////////////

db.orders.aggregate([
    { $match: { OrderID: 11078 } },
    { $lookup: {
        from: "customers",
        localField: "CustomerID",
        foreignField: "CustomerID",
        as: "Customer"
    }},
    { $unwind: "$Customer" },
    { $lookup: {
        from: "employees",
        localField: "EmployeeID",
        foreignField: "EmployeeID",
        as: "Employee"
    }},
    { $unwind: "$Employee" },
    { $lookup: {
        from: "orderdetails",
        localField: "OrderID",
        foreignField: "OrderID",
        as: "Orderdetails"
    }},
    { $lookup: {
        from: "shippers",
        localField: "ShipVia",
        foreignField: "ShipperID",
        as: "Shipper"
    }},
    { $unwind: { path: "$Shipper", preserveNullAndEmptyArrays: true } },
    { $unwind: { path: "$Orderdetails", preserveNullAndEmptyArrays: true } },
    { $lookup: {
        from: "products",
        localField: "Orderdetails.ProductID",
        foreignField: "ProductID",
        as: "Product"
    }},
    { $unwind: "$Product" },
    { $lookup: {
        from: "categories",
        localField: "Product.CategoryID",
        foreignField: "CategoryID",
        as: "ProdCat"
    }},
    { $unwind: "$ProdCat"},
    { $addFields: {
        "Orderdetails.product": {
          ProductID: "$Product.ProductID",
          ProductName: "$Product.ProductName",
          QuantityPerUnit: "$Product.QuantityPerUnit",
          CategoryID: "$Product.CategoryID",
          CategoryName: "$ProdCat.CategoryName"
        },
        "Orderdetails.Value": {
          $multiply: [
            "$Orderdetails.UnitPrice",
            "$Orderdetails.Quantity",
            { $subtract: [1, "$Orderdetails.Discount"] }
          ]
        }
    }},
    { $group: {
        _id: "$OrderID",
        OrderID: { $first: "$OrderID" },
        Customer: { $first: {
          CustomerID: "$Customer.CustomerID",
          CompanyName: "$Customer.CompanyName",
          City: "$Customer.City",
          Country: "$Customer.Country"
        }},
        Employee: { $first: {
          EmployeeID: "$Employee.EmployeeID",
          FirstName: "$Employee.FirstName",
          LastName: "$Employee.LastName",
          Title: "$Employee.Title"
        }},
        Dates: { $first: {
          OrderDate: "$OrderDate",
          RequiredDate: "$RequiredDate"
        }},
        Freight: { $first: "$Freight" },
        Orderdetails: { $push: {
          UnitPrice: "$Orderdetails.UnitPrice",
          Quantity: "$Orderdetails.Quantity",
          Discount: "$Orderdetails.Discount",
          Value: "$Orderdetails.Value",
          product: "$Orderdetails.product"
        }},
        Shipment: { $first: {
          Shipper: {
            ShipperID: "$Shipper.ShipperID",
            CompanyName: "$Shipper.CompanyName"
          },
          ShipName: "$ShipName",
          ShipAddress: "$ShipAddress",
          ShipCity: "$ShipCity",
          ShipCountry: "$ShipCountry"
        }}
    }},
    { $addFields: {
        OrderTotal: { $sum: "$Orderdetails.Value" }
    }},
    { $merge: {
        into: "OrderInfo",
        on: "OrderID",
        whenMatched: "replace",
        whenNotMatched: "insert"
    }}
  ]);



  ///////


  db.customers.aggregate([
    { 
      $match: { 
        CustomerID: "ALFKI" // Możesz zmienić na konkretne ID lub usunąć dla wszystkich klientów
      } 
    },
    {
      $lookup: {
        from: "orders",
        let: { customerId: "$CustomerID" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$CustomerID", "$$customerId"] } 
            } 
          }
        ],
        as: "Orders"
      }
    },
    { $unwind: "$Orders" },
    {
      $lookup: {
        from: "employees",
        let: { empId: "$Orders.EmployeeID" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$EmployeeID", "$$empId"] } 
            } 
          },
          { $limit: 1 }
        ],
        as: "Employee"
      }
    },
    { $unwind: "$Employee" },
    {
      $lookup: {
        from: "shippers",
        let: { shipperId: "$Orders.ShipVia" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$ShipperID", "$$shipperId"] } 
            } 
          },
          { $limit: 1 }
        ],
        as: "Shipper"
      }
    },
    { $unwind: "$Shipper" },
    {
      $lookup: {
        from: "orderdetails",
        let: { orderId: "$Orders.OrderID" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$OrderID", "$$orderId"] } 
            } 
          }
        ],
        as: "Details"
      }
    },
    { $unwind: "$Details" },
    {
      $lookup: {
        from: "products",
        let: { productId: "$Details.ProductID" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$ProductID", "$$productId"] } 
            } 
          },
          { $limit: 1 }
        ],
        as: "Product"
      }
    },
    { $unwind: "$Product" },
    {
      $lookup: {
        from: "categories",
        let: { categoryId: "$Product.CategoryID" },
        pipeline: [
          { 
            $match: { 
              $expr: { $eq: ["$CategoryID", "$$categoryId"] } 
            } 
          },
          { $limit: 1 }
        ],
        as: "Category"
      }
    },
    { $unwind: "$Category" },
    {
      $addFields: {
        "Details.Value": {
          $multiply: [
            "$Details.UnitPrice",
            "$Details.Quantity",
            { $subtract: [1, "$Details.Discount"] }
          ]
        },
        "Details.Product": {
          ProductID: "$Product.ProductID",
          ProductName: "$Product.ProductName",
          QuantityPerUnit: "$Product.QuantityPerUnit",
          CategoryID: "$Category.CategoryID",
          CategoryName: "$Category.CategoryName"
        }
      }
    },
    {
      $group: {
        _id: {
          CustomerID: "$CustomerID",
          OrderID: "$Orders.OrderID"
        },
        CompanyName: { $first: "$CompanyName" },
        City: { $first: "$City" },
        Country: { $first: "$Country" },
        Employee: {
          $first: {
            EmployeeID: "$Employee.EmployeeID",
            FirstName: "$Employee.FirstName",
            LastName: "$Employee.LastName",
            Title: "$Employee.Title"
          }
        },
        Dates: {
          $first: {
            OrderDate: "$Orders.OrderDate",
            RequiredDate: "$Orders.RequiredDate"
          }
        },
        Freight: { $first: "$Orders.Freight" },
        Shipment: {
          $first: {
            Shipper: {
              ShipperID: "$Shipper.ShipperID",
              CompanyName: "$Shipper.CompanyName"
            },
            ShipName: "$Orders.ShipName",
            ShipAddress: "$Orders.ShipAddress",
            ShipCity: "$Orders.ShipCity",
            ShipCountry: "$Orders.ShipCountry"
          }
        },
        OrderDetails: { $push: "$Details" },
        OrderTotal: {
          $sum: "$Details.Value"
        }
      }
    },
    {
      $group: {
        _id: "$_id.CustomerID",
        CustomerID: { $first: "$_id.CustomerID" },
        CompanyName: { $first: "$CompanyName" },
        City: { $first: "$City" },
        Country: { $first: "$Country" },
        Orders: {
          $push: {
            OrderID: "$_id.OrderID",
            Employee: "$Employee",
            Dates: "$Dates",
            Freight: "$Freight",
            Shipment: "$Shipment",
            Orderdetails: "$OrderDetails",
            OrderTotal: "$OrderTotal"
          }
        }
      }
    },
    {
      $project: {
        _id: 1,
        CustomerID: 1,
        CompanyName: 1,
        City: 1,
        Country: 1,
        Orders: 1
      }
    },
    {
      $merge: {
        into: "CustomerInfo",
        on: "CustomerID",
        whenMatched: "replace",
        whenNotMatched: "insert"
      }
    }
  ])
```

f)


```js
--  ...
```



# Zadanie 2 - modelowanie danych


Zaproponuj strukturę bazy danych dla wybranego/przykładowego zagadnienia/problemu

Należy wybrać jedno zagadnienie/problem (A lub B lub C)

Przykład A
- Wykładowcy, przedmioty, studenci, oceny
	- Wykładowcy prowadzą zajęcia z poszczególnych przedmiotów
	- Studenci uczęszczają na zajęcia
	- Wykładowcy wystawiają oceny studentom
	- Studenci oceniają zajęcia

Przykład B
- Firmy, wycieczki, osoby
	- Firmy organizują wycieczki
	- Osoby rezerwują miejsca/wykupują bilety
	- Osoby oceniają wycieczki

Przykład C
- Własny przykład o podobnym stopniu złożoności

a) Zaproponuj  różne warianty struktury bazy danych i dokumentów w poszczególnych kolekcjach oraz przeprowadzić dyskusję każdego wariantu (wskazać wady i zalety każdego z wariantów)
- zdefiniuj schemat/reguły walidacji danych
- wykorzystaj referencje
- dokumenty zagnieżdżone
- tablice

b) Kolekcje należy wypełnić przykładowymi danymi

c) W kontekście zaprezentowania wad/zalet należy zaprezentować kilka przykładów/zapytań/operacji oraz dla których dedykowany jest dany wariant

W sprawozdaniu należy zamieścić przykładowe dokumenty w formacie JSON ( pkt a) i b)), oraz kod zapytań/operacji (pkt c)), wraz z odpowiednim komentarzem opisującym strukturę dokumentów oraz polecenia ilustrujące wykonanie przykładowych operacji na danych

Do sprawozdania należy kompletny zrzut wykonanych/przygotowanych baz danych (taki zrzut można wykonać np. za pomocą poleceń `mongoexport`, `mongdump` …) oraz plik z kodem operacji/zapytań w wersji źródłowej (np. plik .js, np. plik .md ), załącznik powinien mieć format zip

## Zadanie 2  - rozwiązanie

> Wyniki: 
> 
> przykłady, kod, zrzuty ekranów, komentarz ...

```js
--  ...
```

---

Punktacja:

|         |     |
| ------- | --- |
| zadanie | pkt |
| 1       | 1   |
| 2       | 1   |
| razem   | 2   |



