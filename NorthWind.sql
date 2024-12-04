--Written by Radosław Szepielak @2024

declare @id int
set @id = (select CategoryID from Categories where CategoryName = 'Meat/Poultry')

select ProductName,UnitPrice
from Products
where categoryid = (select categoryid from categories where CategoryName = 'Meat/Poultry')
--lub = @id





---------------------------------str 13
--1
--Szukamy informacji o produktach sprzedawanych w butelkach (‘bottle’)
select ProductID, ProductName, QuantityPerUnit
from Products
where QuantityPerUnit like '%bottle%'

--2
--Wyszukaj informacje o stanowisku pracowników,
--których nazwiska zaczynają się na literę z zakresu od B do L
select LastName, Title
from Employees
where LastName like '[B-L]%'


--3
--Wyszukaj informacje o stanowisku pracowników,
--których nazwiska zaczynają się na literę  B lub L
select LastName, Title
from Employees
where LastName like '[BL]%'

-- bez użycia like

select LastName, Title
from Employees --lub left(LastName,1) >= 'B' and <= 'L'
where LastName >= 'B' and LastName < 'M' -- <= 'L' nie bo może być nazwisko 'LI....' > 'L'


----------------------str17

--2
select OrderID,OrderDate
from Orders
where OrderDate >= '1997-01-01' and OrderDate < '1998-01-01'
--<= '1997-12-31' nie zadziała bo dalej może być godzina > 00:00...
-- lub można YEAR(1997)



------------------20
--Napisz instrukcję select tak aby wybrać numer zlecenia, datę zamówienia, numer klienta
--dla wszystkich niezrealizowanych jeszcze zleceń, dla których krajem odbiorcy jest Argentyna
SELECT OrderID, OrderDate, CustomerID, ShippedDate, ShipCountry
FROM Orders
WHERE ShipCountry IN ('Argentina') AND ShippedDate IS NULL;

--a gdy np pojutrze ma być od dzisiaj .... and ( ShippedDate IS NULL or GETDATE())
SELECT CAST(GETDATE() AS DATE) AS CurrentDate; --typ DATE 2024-11-30
SELECT GETDATE() AS CurrentDate; -- cała data 2024-11-30 19:23:02.140


--stringi, nazwy kolumn
select FirstName, LastName as Nazwiska, 'pracownik' kto
from Employees

select UnitPrice, UnitPrice * 1.05 as NewUnitPrice,
       UnitPrice*1.05 - UnitPrice as Diff--tu nie można wprost
--użyc aliasu NewUnitPrice - Unit..., as opcjonalnie
from [Order Details]


select concat(FirstName,' ', LastName) as imie_nazwisko
-- lub FirstName + ' ' +  LastName as imie_nawzisko
from Employees

---------str33
--1
select OrderID, round((UnitPrice*Quantity*(1-Discount)), 2) as Price
from [Order Details]
where OrderID = '10250'
--lub cast(UnitPrice...(1-Discount) as money)


--2
--Napisz polecenie które dla każdego dostawcy (supplier) pokaże pojedynczą
--kolumnę zawierającą nr telefonu i nr faksu w formacie (numer telefonu
--i faksu mają być oddzielone przecinkiem)
select CompanyName, SupplierID, concat(Phone, ', ', Fax) as abc
from Suppliers

select CompanyName, ContactName, IIF(Fax is not NULL, CONCAT(Phone, ', ', Fax), Phone)
from Suppliers;

select CompanyName, CONCAT(Phone, ', ' + Fax) from Suppliers
-- jeśli Phone = Null to bez przecinka

-------------------------------
--------------------------------
---------------------------------
----------------------------------

select top 5 with ties orderid, productid, quantity
from [order details]
order by quantity desc


---

select count (*) -- wszystkie wiersze
from Employees

select count (ReportsTo) -- bez null jeśli argument
from Employees

select count ('ala ma kota') -- ale takiej kolumny nie ma
from Employees

select *
from Employees



------
------ str 7
--Podaj sumę/wartość zamówienia o numerze 10250
select sum(Quantity * UnitPrice * (1 - Discount)) as TotalPrice
from [Order Details]
where OrderID = '10250'


------
select max(UnitPrice)
from Products
where UnitPrice < 20

select top 1 with ties UnitPrice, ProductName --Można nazwę dodatkowo
--jeśli kilka miałoby takie samo max
from Products
where UnitPrice < 20
order by UnitPrice desc

select max(UnitPrice) max, min(UnitPrice) min, avg(UnitPrice) average
from Products
where QuantityPerUnit like '%bottle%'


select * from Products
where UnitPrice > (select avg(UnitPrice) from Products)

---

select *
from orderhist

select ProductID, sum(quantity) as total_quantity, min(quantity)
from orderhist
group by ProductID

select OrderID, sum(quantity*UnitPrice*(1-Discount)) as total_price
from [Order Details]
where OrderID < 10250
group by OrderID
order by OrderID desc -- lub total_price

--12,16 str + group ćwiczenia

-------str 12
--1 Podaj maksymalną cenę zamawianego produktu dla każdego zamówienia
select OrderID, max(UnitPrice) as MaxPricePerOrder
from [Order Details]
group by OrderID


--2 Posortuj zamówienia wg maksymalnej ceny produktu
select OrderID, max(UnitPrice) as MaxPricePerOrder
from [Order Details]
group by OrderID
order by MaxPricePerOrder


--3 Podaj maksymalną i minimalną cenę zamawianego produktu dla każdego zamówienia
select OrderID, min(UnitPrice) MinPricePerOrder, max(UnitPrice) MaxPricePerOrder
from [Order Details]
group by OrderID


--4 Podaj liczbę zamówień dostarczanych przez poszczególnych spedytorów (przewoźników)
select COUNT(ShipVia)
from Orders
group by ShipVia


--5 Który ze spedytorów był najaktywniejszy w 1997 roku
select top 1 ShipVia as ShipperID_, COUNT(ShipVia) as Quantity
from Orders
where OrderDate >= '1997-01-01' and OrderDate < '1998-01-01'
group by ShipVia
order by Quantity desc



---------str 16

--1 Wyświetl zamówienia dla których liczba pozycji zamówienia jest większa niż 5

select OrderID, sum(Quantity)
from [Order Details]
group by OrderID
having sum(Quantity) > 5


--2 Wyświetl  klientów dla których w 1998 roku zrealizowano więcej niż 8 zamówień
-- (wyniki posortuj malejąco wg łącznej kwoty za dostarczenie zamówień dla każdego z klientów)

select CustomerID, COUNT(OrderID) as QuantityOfOrders, sum(Freight) as PriceOfFreight
from Orders
where ShippedDate >= '1998-01-01' and OrderDate < '1999-01-01'
group by CustomerID
having COUNT(OrderID) > 8
order by PriceOfFreight desc
--można używać np dodatkowo jakiejś kolumny w select ale trzeba ją dodać
--do group by bo np jeśli grupujemy po Nazwie produktu a mają różne ID
--to nie wie co ma zrobić z ID (któro wstawić do wyniku zapytania dla
--danego wiersza w którym zgrupowano nazwę produktu :) i wtedy robi unikalne
--pary między elementami - tu łatwiej, ale np Region/Województwo -> Miasta)

--na razie tylko Orders więc bez problemu Freight raz zliczane


------------------------
---------- ćwiczenie 1 group by

----------str 1
-- 1.Dla każdego zamówienia podaj jego wartość. Posortuj wynik wg wartości
--zamówień (w malejęcej kolejności)

select OrderID, sum(Quantity*UnitPrice) as TotalPrice
from [Order Details]
group by OrderID
order by TotalPrice desc

-- 2. Zmodyfikuj zapytanie z poprzedniego punktu,
-- tak aby zwracało tylko pierwszych 10 wierszy
select top 10 OrderID, sum(Quantity*UnitPrice) as TotalPrice
from [Order Details]
group by OrderID
order by TotalPrice desc


-- 3. Podaj  nr zamówienia oraz wartość  zamówienia, dla zamówień,
-- dla których łączna liczba zamawianych jednostek produktów jest większa niż 250

select OrderID, sum(Quantity*UnitPrice) as TotalPrice, sum(Quantity) as TotalQuantity
from [Order Details]
group by OrderID
having sum(Quantity) > 250
order by TotalPrice desc

-- 4. Podaj liczbę zamówionych jednostek produktów dla  produktów,
-- dla których productid jest mniejszy niż 3

select ProductID, sum(Quantity) as QuantityOfProduct
from [Order Details]
where ProductID < 3
group by ProductID


---------- str 4
-- 1. Dla każdego pracownika podaj liczbę obsługiwanych przez niego zamówień w 1997r
select EmployeeID, COUNT(OrderID)
from Orders
where OrderDate >= '1997-01-01' and OrderDate < '1998-01-01'
group by EmployeeID

-- 2.  Dla każdego pracownika podaj ilu klientów (różnych klientów) obsługiwał
--ten pracownik w 1997r

select EmployeeID, COUNT( DISTINCT CustomerID) as LiczbaRóżnychKlientów
from Orders
where OrderDate >= '1997-01-01' and OrderDate < '1998-01-01'
group by EmployeeID -- z CustomerID tu unikalne pary i bez DISTINCT widzimy który
-- pracownik ile razy obsługiwał tego samego klienta, z CustomerID w select
--kogo dokładnie wiele razy


-- 3. Dla każdego spedytora/przewoźnika podaj łączną wartość "opłat za przesyłkę"
-- dla przewożonych przez niego zamówień
select ShipVia, sum(Freight) as ŁącznaOpłata --count(OrderID) as LiczbaZamówień
from Orders
group by ShipVia --dodatkowo OrderID możliwe unikalne pary


-- 4. Dla każdego spedytora/przewoźnika podaj łączną wartość "opłat za przesyłkę"
-- przewożonych przez niego zamówień w latach od 1996 do 1997
select ShipVia, sum(Freight) as ŁącznaOpłata -- count(OrderID) --> liczba zamówień dla każdego
from Orders
where OrderDate >= '1996-01-01' and OrderDate < '1998-01-01'
group by ShipVia --OrderID


------------str 5
-- 1. Dla każdego pracownika podaj liczbę obsługiwanych przez
-- niego zamówień z podziałem na lata

select EmployeeID, YEAR(OrderDate) as YEAR, COUNT(OrderID) as TotalAmountOfOrders
from Orders
group by EmployeeID, YEAR(OrderDate)
order by EmployeeID, YEAR

-- 2. Dla każdego pracownika podaj liczbę obsługiwanych przez
-- niego zamówień z podziałem na lata i miesiące

select EmployeeID, YEAR(OrderDate) as YEAR, MONTH(OrderDate) as MONTH, COUNT(OrderID) as TotalAmountOfOrders
from Orders
group by EmployeeID, YEAR(OrderDate), MONTH(OrderDate)
order by EmployeeID, YEAR, MONTH





-----------------------------------------------------
------------------------------------------------------
-------------------------------------------------------
---------------------INNER JOIN kolejność bez znaczenia

select productname, companyname
from products
         inner join suppliers
                    on products.supplierid = suppliers.supplierid


select p.productid, productname, companyname, s.SupplierID
from products p
         inner join suppliers s
                    on p.supplierid = s.supplierid

--Napisz polecenie zwracające jako wynik nazwy klientów,
--którzy złożyli zamówienia po 01 marca 1998 (baza northwind)

select distinct customers.CustomerID, companyname
from orders
         inner join customers -- inner join = join
                    on orders.customerid = customers.customerid
where orderdate > '1998-03-01'


select distinct customers.CustomerID, companyname -- to samo co wyżej
from Orders, Customers
where orderdate > '1998-03-01' and orders.CustomerID = customers.CustomerID
-- też inner join ale inny zapis!!!



--------------------- OUTER JOIN
--kolejność outer joinów ma znaczenie a inner nie

select companyname, customers.customerid, orderdate
from customers -- jest po lewej a nie ma po prawej
         left outer join orders
                         on customers.customerid = orders.customerid
where OrderID is null -- nie shipped date bo mogło być wysłane albo nie a i tak mieć null




------------str 17
--1. Wybierz nazwy i ceny produktów (baza northwind) o cenie jednostkowej pomiędzy
--20.00 a 30.00, dla każdego produktu podaj dane adresowe dostawcy

select ProductName, UnitPrice, s.Address
from Products p inner join Suppliers s on s.SupplierID = p.SupplierID
where UnitPrice > 20.00 and UnitPrice < 30.00


--2. Wybierz nazwy produktów oraz inf. o stanie magazynu dla
-- produktów dostarczanych przez firmę ‘Tokyo Traders’

select ProductName, UnitsInStock
from Products p inner join Suppliers s on p.SupplierID = s.SupplierID
where CompanyName = 'Tokyo Traders'


--3. Czy są jacyś klienci którzy nie złożyli żadnego zamówienia w 1997 roku,
-- jeśli tak to pokaż ich dane adresowe

select c.CustomerID, Address, City -- left outer join = left join
from Customers c left outer join Orders o on c.CustomerID = o.CustomerID
    and YEAR(o.OrderDate) = 1997 -- już ma znaczenie że warunek jest tutaj
--bo pokazuje tych co zamówili w 1997 albo nie zamówili w 1997 (ale mogli zamówić w innym roku)
--a niżej odrzucamy tych co faktycznie zamówili w 1997 i wykorzystujemy to że left join takie
--coś nam daje dodatkowo, tutaj w where nie bo da 0, chcemy zamówienie && null ... bez sensu
where o.OrderID is null


--4. Wybierz nazwy i numery telefonów dostawców, dostarczających produkty,
-- których aktualnie nie ma w magazynie.

select CompanyName, s.Phone
from Suppliers s join Products p on s.SupplierID = p.SupplierID
    and UnitsInStock = 0


-- 5. Wybierz zamówienia złożone w marcu 1997. Dla każdego takiego zamówienia wyświetl jego numer,
-- datę złożenia zamówienia oraz nazwę i numer telefonu klienta

select o.OrderID, o.OrderDate, c.CompanyName, c.Phone
from Orders o join Customers c on c.CustomerID = o.CustomerID
where o.OrderDate >= '1997-03-01' and o.OrderDate < '1997-04-01'

-----------
--Napisz polecenie zwracające listę produktów zamawianych w dniu 1996-07-08
select distinct ProductName
from [Order Details] od join Products p
on p.ProductID = od.ProductID
    join Orders o
    on o.OrderID = od.OrderID
where OrderDate = '1996-07-08'
--lub from Orders... bez znaczenia w join


-----------------------str23
----1. Wybierz nazwy i ceny produktów (baza northwind) o cenie jednostkowej pomiędzy 20.00 a 30.00,
-- dla każdego produktu podaj dane adresowe dostawcy, interesują nas tylko produkty
-- z kategorii ‘Meat/Poultry’

select ProductName, p.UnitPrice, Address
from Products p join Suppliers s on p.SupplierID = s.SupplierID
                join Categories cat on p.CategoryID = cat.CategoryID
where p.UnitPrice between 20.00 and 30.00 and CategoryName = 'Meat/Poultry'
-- jeśli dodamy join Order Details on ProductID to wyjdzie więcej,
--jeśli where od.UnitPrice to ceny tam dla różnych zamówień określonego
--produktu były inne niż w Products + discount


--2. Wybierz nazwy i ceny produktów z kategorii ‘Confections’ dla każdego produktu podaj nazwę dostawcy.
select ProductName, UnitPrice, CompanyName
from Products p join Suppliers s on p.SupplierID = s.SupplierID
                join Categories c on c.CategoryID = p.CategoryID
where c.CategoryName like '%Confections%'


--3. Dla każdego klienta podaj liczbę złożonych przez niego zamówień. Zbiór wynikowy
-- powinien zawierać nazwę klienta, oraz liczbę zamówień
select c.CompanyName, COUNT(OrderID) as LiczbaZamówień
from Customers c left join Orders o on c.CustomerID = o.CustomerID
group by c.CustomerID, c.CompanyName
-- ^^^^^ na wypadek gdyby taka sama nazwa firmy


--4. Dla każdego klienta podaj liczbę złożonych przez niego zamówień w marcu 1997r
select c.CompanyName, COUNT(OrderID) as LiczbaZamówień
from Customers c left join Orders o on c.CustomerID = o.CustomerID and
                                       OrderDate > '1997-03-01' and OrderDate < '1997-04-01'
group by c.CustomerID, c.CompanyName



---------------str24
--1.Który ze spedytorów był najaktywniejszy w 1997 roku, podaj nazwę tego spedytora
select top 1 CompanyName, COUNT(OrderID) as LiczbaZamówień
from Shippers s join Orders o on s.ShipperID = o.ShipVia
group by s.ShipperID, CompanyName -- na wypadek takiego samego CompanyName
order by 2 desc


--2. Dla każdego zamówienia podaj wartość zamówionych produktów. Zbiór wynikowy powinien
--zawierać nr zamówienia, datę zamówienia, nazwę klienta oraz wartość zamówionych produktów
select o.OrderID, OrderDate, CompanyName, sum(Quantity*UnitPrice*(1-Discount)) as TotalPrice
from [Order Details] od join Orders o on od.OrderID = o.OrderID
    join Customers c on o.CustomerID = c.CustomerID
group by o.OrderID, OrderDate, c.CustomerID, CompanyName


--3. Dla każdego zamówienia podaj jego pełną wartość (wliczając opłatę za przesyłkę).
-- Zbiór wynikowy powinien zawierać nr zamówienia, datę zamówienia, nazwę klienta oraz pełną
-- wartość zamówienia

select o.OrderID, OrderDate, CompanyName, sum(Quantity*UnitPrice*(1-Discount)) + Freight as TotalPrice
from Orders o join Customers c on o.CustomerID = c.CustomerID
              join [Order Details] od on o.OrderID = od.OrderID
group by o.OrderID, OrderDate, c.CustomerID, CompanyName, Freight
--relacja zamówienie jeśli jest, to przez 1 customera więc OrderDate miał taką samą,
-- jakby to pojedyncze zamówienie i Freight też jedno bo to jedno zamówienie OK :)



-------------str25

--3. Wybierz nazwy i numery telefonów klientów, którzy kupowali produkty z kategorii ‘Confections’
select distinct CompanyName, Phone
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
where CategoryName = 'Confections'



--4. Wybierz nazwy i numery telefonów klientów, którzy nie kupowali produktów z kategorii ‘Confections’

select distinct CompanyName, Phone --to ŹLE, bo jeśli ma inne poza cuksami, albo wgl nie składał zamówień (2) to mamy (91)
from Customers c left join Orders o on c.CustomerID = o.CustomerID
                 left join [Order Details] od on o.OrderID = od.OrderID
    left join Products p on od.ProductID = p.ProductID
    left join Categories cat on p.CategoryID = cat.CategoryID and CategoryName = 'Confections'
where CategoryName is null --tutaj jeśli ktoś miał cukierki a miał inne zamówienie to go i tak liczymy
--tu jeśli damy zamiast distinct group by Comp.... to też 91 bo tu akurat zadziała tak samo jak distinct
-- że odrzuci powtórzone wiersze w wyniku
--left join daje tych co w ogóle nie złożyli, tych co złożyli w cuksach a te co złożyli w innych kategoriach
--to one mają null bo and CategoryName = '...'


SELECT c.CompanyName, c.Phone-------------------odrzuca jeśli nawet miał inne zamówienie poza cukierkami (11) OK
FROM Customers c  ---bo używamy not in
WHERE c.CustomerID NOT IN (
    SELECT
        o.CustomerID
    FROM
        Orders o JOIN [Order Details] od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Categories cat ON p.CategoryID = cat.CategoryID
WHERE
    cat.CategoryName = 'Confections'
    );


SELECT c.CompanyName, c.Phone
FROM Customers c
         LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
         LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
    LEFT JOIN Products p ON od.ProductID = p.ProductID
    LEFT JOIN Categories cat ON p.CategoryID = cat.CategoryID
GROUP BY c.CustomerID, c.CompanyName, c.Phone  ---dotąd ma (91) group by jak distinct w 1. rozwiązaniu
HAVING SUM(CASE WHEN cat.CategoryName = 'Confections' THEN 1 ELSE 0 END) = 0 ---
--Having tutaj sprawdza czy dany CustomerID miał jakiekolwiek zamówienie w cukierkach
--jeśli tak to go wywala (przelatuje po wszystkich jego zamówieniach i ma być 0 zamówień z cuksami)
-- czyli zlicza tylko tych co nie mają żadnego w cukierkach i też (11)
--to jest ok bo mamy zwrócić tych co nie mają w cukierkach żadnego zamówienia
--git bo 11+80 = 91




--5. Wybierz nazwy i numery telefonów klientów, którzy w 1997r nie kupowali produktów
-- z kategorii ‘Confections’

select distinct CompanyName, Phone--, CategoryName -- źle (91) ma być (18)
from Customers c left join Orders o on c.CustomerID = o.CustomerID
                 left join [Order Details] od on o.OrderID = od.OrderID
    left join Products p on od.ProductID = p.ProductID
    left join Categories cat on p.CategoryID = cat.CategoryID and CategoryName = 'Confections'
where (CategoryName is null and YEAR(OrderDate) = 1997) -- w 1997 nie mieli cuksów
   or (CategoryName = 'Confections' and YEAR(OrderDate) <> 1997)-- mieli cuksy w innych latach
   or (CategoryName is null and OrderDate is null) -- wgl nie złożyli
--left join daje tych co w ogóle nie złożyli, tych co złożyli w cuksach a te co złożyli w innych kategoriach
--to one mają null bo and CategoryName = '...'
-- ponownie zawiera tych którzy poza cukierkami mieli jakieś inne zamówienia w 1997 (90)
--razem z or (CategoryName = 'Confections' and YEAR(OrderDate) = 1997) -- daje pełne pokrycie przypadków
--(91) wtedy czyli jedna osoba jest co kupowała tylko same cukierki!!!!!!!!!



SELECT c.CompanyName, c.Phone ---to poprawne bo tylko 1997 (23 git bo musi być więcej niż 18)
FROM Customers c
         LEFT JOIN Orders o ON c.CustomerID = o.CustomerID and YEAR(o.OrderDate) = 1997
    LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
    LEFT JOIN Products p ON od.ProductID = p.ProductID
    LEFT JOIN Categories cat ON p.CategoryID = cat.CategoryID
GROUP BY c.CustomerID, c.CompanyName, c.Phone -- nie trzeba teoretycznie c.CustomerID bo nazwy się nie powtarzają
HAVING SUM(CASE WHEN cat.CategoryName = 'Confections' THEN 1 ELSE 0 END) = 0; --czy dla danego CustomerID (bo tak grupujemy)
--któraś krotka ma Confections ( może mieć tam inne, ale również null (jeśli inne lata) więc 0 daje tym przypadkom)
-- jeśli warunek YEAR(o.OrderDate) byłby w where to nie bierzemy pod uwagę tego jeśli ktoś nic nie zamawiał (2)
-- lub zamawiał coś ale tylko w latach innych niż 1997 (3) i wtedy zostają nam tylko Ci z zamówieniem/niami z roku 1997



--lub z użyciem NOT IN
-- having > 1


----------------------------------
----------------------------------29


--1. Napisz polecenie, które wyświetla pracowników oraz ich podwładnych (baza northwind)
select EmployeeID, FirstName + ' ' +  LastName as FLname, ReportsTo
from Employees
--where ReportsTo is not null -- tylko Ci którzy mają szefa
order by 3 -- same ID szefów, FL podwładnych

--up, dw down
select up.EmployeeID, up.FirstName, up.LastName, dw.EmployeeID, dw.FirstName, dw.LastName
from Employees as up inner join Employees as dw on up.EmployeeID = dw.ReportsTo --do pracownika patrzymy czy ktoś ma go jako szefa
--jeśli tak wypisujemy dw.EmployeeID tego ktośa
order by up.FirstName -- mamy


--2.Napisz polecenie, które wyświetla pracowników, którzy nie mają podwładnych (baza northwind)
SELECT szef.EmployeeID, szef.LastName AS Name
FROM Employees szef left join Employees pod on szef.EmployeeID = pod.ReportsTo
where pod.EmployeeID is null -- jeśli nie miało dopasowania to wstawia tu null, wytłumaczenia analogiczne do wyżej


--3. Napisz polecenie, które wyświetla pracowników, którzy mają podwładnych (baza northwind)

select a.EmployeeID, a.FirstName + ' ' + a.LastName as ImieNazwisko, COUNT(a.EmployeeID) as liczba_podwladnych
from Employees as a left join Employees as b on a.EmployeeID = b.ReportsTo
where b.ReportsTo is not null
group by a.EmployeeID, a.FirstName + ' ' + a.LastName



------------------------------------------Ćwiczenia Join
---------str 1
--1. Dla każdego zamówienia podaj łączną liczbę zamówionych jednostek towaru oraz nazwę klienta.
select o.OrderID, CompanyName, sum(Quantity) as LiczbaJednostek
from Orders o join [Order Details] od on o.OrderID = od.OrderID
    join Customers c on c.CustomerID = o.CustomerID
group by o.OrderID, c.CustomerID, CompanyName --CustomerID trzeba jeśli takie same nazwy firm by były
--akurat OrderID^ jest mocniejsze bo zamówienie przez 0 lub 1 klienta no ale...

--2. Dla każdego zamówienia podaj łączną wartość zamówionych produktów (wartość zamówienia bez
--opłaty za przesyłkę) oraz nazwę klienta.
select o.OrderID, CompanyName, sum(UnitPrice*Quantity*(1-Discount)) as TotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
    join Customers c on c.CustomerID = o.CustomerID
group by o.OrderID, c.CustomerID, CompanyName --CustomerID trzeba

--3. Dla każdego zamówienia podaj łączną wartość tego zamówienia (wartość zamówienia wraz z opłatą
--za przesyłkę) oraz nazwę klienta.

select o.OrderID, CompanyName, sum(UnitPrice*Quantity*(1-Discount)) + o.Freight as TotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
    join Customers c on c.CustomerID = o.CustomerID
group by o.OrderID, CompanyName, o.Freight


--4. Zmodyfikuj poprzednie przykłady tak żeby dodać jeszcze imię i nazwisko pracownika obsługującego zamówień

select o.OrderID, CompanyName, e.LastName, e.FirstName ,sum(UnitPrice*Quantity*(1-Discount)) + o.Freight as TotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
    join Customers c on c.CustomerID = o.CustomerID
    join Employees e on e.EmployeeID = o.EmployeeID
group by o.OrderID, CompanyName, o.Freight, e.LastName, e.FirstName


---------str2
--1. Podaj nazwy przewoźników, którzy w marcu 1998 przewozili produkty z kategorii 'Meat/Poultry'
select CompanyName, CategoryName
from Shippers s join Orders o on s.ShipperID = o.ShipVia
                join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories c on p.CategoryID = c.CategoryID
where OrderDate >= '1998-03-01' and OrderDate < '1998-04-01' and CategoryName = 'Meat/Poultry'
group by ShipperID, CompanyName, CategoryName


--2. Podaj nazwy przewoźników, którzy w marcu 1997r nie przewozili produktów z kategorii 'Meat/Poultry'
select CompanyName
from Shippers s  left join Orders o on s.ShipperID = o.ShipVia
                 left join [Order Details] od on o.OrderID = od.OrderID
    left join Products p on od.ProductID = p.ProductID
    left join Categories c on p.CategoryID = c.CategoryID and CategoryName = 'Meat/Poultry'
where OrderDate >= '1997-03-01' and OrderDate < '1997-04-01'
group by CompanyName--, CategoryName tu nie może być bo inaczej wymieni wszytkich (3) bo
--having nie będzie sprawdzało po grupie tylko pojedyncze wiersze
having sum(case when c.CategoryName = 'Meat/Poultry' then 1 else 0 end) = 0; -- lub Select NOT IN... select


--3. Dla każdego przewoźnika podaj wartość produktów z kategorii 'Meat/Poultry' które ten przewoźnik
-- przewiózł w marcu 1997
select CompanyName, CategoryName, sum(od.Quantity*p.UnitPrice*(1-Discount)) as TotalPrice
from Shippers s join Orders o on s.ShipperID = o.ShipVia
                join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories c on p.CategoryID = c.CategoryID
where OrderDate >= '1997-03-01' and OrderDate < '1997-04-01' and CategoryName = 'Meat/Poultry'
group by CompanyName, CategoryName




------------------str3

--1. Dla każdej kategorii produktu (nazwa), podaj łączną liczbę zamówionych przez klientów jednostek
-- towarów z tej kategorii.
select cat.CategoryName, c.CompanyName, sum(od.Quantity) as ŁącznaLiczbaJednostek
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
group by cat.CategoryName, c.CustomerID, c.CompanyName

--2. Dla każdej kategorii produktu (nazwa), podaj łączną liczbę zamówionych w 1997r jednostek towarów
-- z tej kategorii.
select cat.CategoryName, sum(od.Quantity) as ŁącznaLiczbaJednostek
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
where YEAR(OrderDate) = 1997
group by cat.CategoryName


--z UnitsOnOrder z Products NIEPOPRAWNE bo to liczba zamówionych (przyjedzie tyle) od dostawców
--ale na magazynie mogło już być, chodzi o Quantity zamówionych
select cat.CategoryName, sum(UnitsOnOrder) as ŁącznaLiczbaJednostek
from Products p join Categories cat on p.CategoryID = cat.CategoryID
                join [Order Details] od on p.ProductID = od.ProductID
    join Orders o on od.OrderID = o.OrderID
where YEAR(OrderDate) = 1997
group by cat.CategoryName


--3. Dla każdej kategorii produktu (nazwa), podaj łączną wartość zamówionych towarów z tej kategorii.

select cat.CategoryName, sum(od.Quantity*od.UnitPrice*(1-Discount)) as ŁącznaWartość
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
group by cat.CategoryName


--------------str4

--1. Dla każdego przewoźnika (nazwa) podaj liczbę zamówień które przewieźli w 1997r
select s.CompanyName, COUNT(CompanyName) LiczbaZamówień
from  Orders o join Shippers s on o.ShipVia = s.ShipperID
where YEAR(OrderDate) = 1997
group by s.ShipperID, s.CompanyName


--2. Który z przewoźników był najaktywniejszy (przewiózł największą liczbę zamówień)
-- w 1997r, podaj nazwę tego przewoźnika
select top 1 s.CompanyName, COUNT(CompanyName) LiczbaZamówień
from  Orders o join Shippers s on o.ShipVia = s.ShipperID
where YEAR(OrderDate) = 1997
group by CompanyName
order by 1 desc


--3. Dla każdego przewoźnika podaj łączną wartość "opłat za przesyłkę" przewożonych przez
--niego zamówień od '1998-05-03' do '1998-05-29'
select s.CompanyName, sum(Freight)
from Suppliers s join Orders o on ShipVia = SupplierID
where OrderDate between '1998-05-03' and '1998-05-29'
group by s.CompanyName --ok wystarczy, nie patrzymy na detale czyli pojedynczo zliczamy Freight,
--jeśli trzeba by było jeszcze wartość zamowień to już tak jak około 900-1000 linijki z klientami


--4. Dla każdego pracownika (imię i nazwisko) podaj łączną wartość zamówień obsłużonych
--przez tego pracownika w maju 1996
select e.LastName, e.FirstName, sum(Quantity*UnitPrice*(1-Discount)) as TotalPrice
from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                 join [Order Details] od on o.OrderID = od.OrderID
where OrderDate between '1997-05-01' and '1997-05-31'
group by e.LastName, e.FirstName


--5. Który z pracowników obsłużył największą liczbę zamówień w 1996r, podaj imię i nazwisko
-- takiego pracownika
select top 1 e.LastName, e.FirstName, COUNT(OrderDate) as TotalPrice
from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                 join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by e.LastName, e.FirstName
order by 3 desc


--6. Który z pracowników był najaktywniejszy (obsłużył zamówienia o największej wartości)
-- w 1996r, podaj imię i nazwisko takiego pracownika
select top 1 e.LastName, e.FirstName, sum(Quantity*UnitPrice*(1-Discount)) as TotalPrice
from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                 join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by e.LastName, e.FirstName
order by 3 desc




---------------------str 5
--1. Dla każdego pracownika (imię i nazwisko) podaj łączną wartość zamówień obsłużonych przez
--tego pracownika. Ogranicz wynik tylko do pracowników (utrudniłem + przesyłka)
--a) którzy mają podwładnych -- dwóch
--b) którzy nie mają podwładnych -- 7


--a)
select a.EmployeeID, b.EmployeeID
from Employees a join Employees b on a.EmployeeID = b.ReportsTo --czy ktoś ma go jako szefa, czyli ma podwładnego

select t.LastName, t.FirstName, sum(TotalSumWithoutFreight) + sum(Freight) as TotalSum
from (select e.EmployeeID, e.LastName, e.FirstName, sum(UnitPrice*Quantity*(1-Discount)) as TotalSumWithoutFreight,
             o.Freight as Freight
      from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                       join [Order Details] od on o.OrderID = od.OrderID
      where e.EmployeeID IN (select a.EmployeeID
          from Employees a join Employees b on a.EmployeeID = b.ReportsTo)
      group by e.EmployeeID, o.OrderID, o.Freight, e.LastName, e.FirstName) t
group by t.EmployeeID, t.LastName, t.FirstName
--trzeba group by OrderID!!! jeśli takie samo Freight to policzy za mało razy Freight tak jakby
--to było jedno zamówienie a może być takich np 10

--b) NOT IN do tego wyżej

select t.LastName, t.FirstName, sum(TotalSumWithoutFreight) + sum(Freight) as TotalSum
from (select e.EmployeeID, e.LastName, e.FirstName, sum(UnitPrice*Quantity*(1-Discount)) as TotalSumWithoutFreight,
             o.Freight as Freight
      from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                       join [Order Details] od on o.OrderID = od.OrderID
      where e.EmployeeID NOT IN (select a.EmployeeID
          from Employees a join Employees b on a.EmployeeID = b.ReportsTo)
      group by e.EmployeeID, o.OrderID, o.Freight, e.LastName, e.FirstName) t
group by t.EmployeeID, t.LastName, t.FirstName

--lub
select a.EmployeeID, b.EmployeeID
from Employees a left join Employees b on a.EmployeeID = b.ReportsTo --czy ktoś ma go jako szefa, czyli ma podwładnego
where b.EmployeeID is null -- nie ma podwładnych

select t.LastName, t.FirstName, sum(TotalSumWithoutFreight) + sum(Freight) as TotalSum
from (select e.EmployeeID, e.LastName, e.FirstName, sum(UnitPrice*Quantity*(1-Discount)) as TotalSumWithoutFreight,
             o.Freight as Freight
      from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                       join [Order Details] od on o.OrderID = od.OrderID
      where e.EmployeeID IN (select a.EmployeeID
          from Employees a left join Employees b on a.EmployeeID = b.ReportsTo
          where b.EmployeeID is null)
      group by e.EmployeeID, o.OrderID, o.Freight, e.LastName, e.FirstName) t
group by t.EmployeeID, t.LastName, t.FirstName



--2. Napisz polecenie, które wyświetla klientów z Francji którzy w 1998r złożyli więcej
--niż dwa zamówienia oraz klientów z Niemiec którzy w 1997r złożyli więcej niż trzy zamówienia

select CompanyName, COUNT(OrderID) as LiczbaZamówień
from Customers c join Orders o on c.CustomerID = o.CustomerID
where Country = 'France' and YEAR(OrderDate) = 1998
group by c.CustomerID, CompanyName
having COUNT(OrderID) > 2
UNION
select CompanyName, COUNT(OrderID) as LiczbaZamówień
from Customers c join Orders o on c.CustomerID = o.CustomerID
where Country = 'Germany' and YEAR(OrderDate) = 1997
group by c.CustomerID, CompanyName
having COUNT(OrderID) > 3


--------------
select firstname + ' ' + LastName as name, city, PostalCode, 'klient'
from Employees
UNION
select CompanyName, city, PostalCode, 'pracownik'
from Customers
--ewentualnie union all i wtedy np ojca i syna tak samo nazwanych nie złączy (bez dania 'klient', 'pracownik')

select cast(EmployeeID as varchar(100)), firstname + ' ' + LastName as name, city, PostalCode, 'klient'
from Employees
UNION all
select CustomerID,CompanyName, city, PostalCode, 'pracownik'
from Customers




----------------------
---------------------
--------------------
-------------------
------------------
-----------------
----------------
---------------
--------------------Subquery

select productname, unitprice
     , (select avg(unitprice) from products) as average
from products;

select productname, unitprice
     , (select avg(unitprice) from products) as average
     , unitprice - (select avg(unitprice) from products) as diff
from products;

-- select productname, unitprice, avg(UnitPrice) as average
--from Products
--group by productname, unitprice--TO nie bo średnia wg danej nazwy
--a chcemy avg wszystkich produktów


select productname, unitprice
     , (select avg(unitprice) from products) as average
     , unitprice - (select avg(unitprice) from products) as diff
from products
where unitprice > (select avg(unitprice) from products)


select *, unitPrice - average as diff
from
    (select productname, unitprice
          , (select avg(unitprice) from products) as average
     from products) t --(831-833) jako tablica t
where unitPrice > average;


-----skorelowane

select *, UnitPrice - average as diff
from (select productname, categoryid, unitprice
           ,(select avg(unitprice)
             from products as p_in
             where p_in.categoryid = p_out.categoryid ) as average
      from products as p_out) t


--with
;with t as (
    select productname, categoryid, unitprice
         ,( select avg(unitprice)
            from products as p_in
            where p_in.categoryid = p_out.categoryid ) as average
    from products as p_out
)
 select *, UnitPrice - average as diff from t


--lub z join
select p.ProductName, p.CategoryID, p.UnitPrice,
       p.UnitPrice - av.avegage as diff
from products p
         join (select categoryid, avg(unitprice) avegage
               from products
               group by categoryid) av
              on p.CategoryID = av.CategoryID




----------------
----------------
---str 1 ćwiczenia
--1. Podaj łączną wartość zamówienia o numerze 10250 (uwzględnij cenę za przesyłkę)
select o.OrderID, sum(Quantity*UnitPrice*(1-Discount)) + Freight as Total
from [Order Details] join Orders o on [Order Details].OrderID = o.OrderID
where o.OrderID = 10250
group by o.OrderID, Freight
--relacja zamówienie jeśli jest, to przez 1 customera więc OrderDate miał taką samą,
-- jakby to pojedyncze zamówienie i Freight też jedno bo to jedno zamówienie OK :)

--LUB

select o.OrderID, (select sum(Quantity*UnitPrice*(1-Discount))
                   from [Order Details] od where o.OrderID = od.OrderID) + o.Freight as Total
from Orders o
where OrderID = '10250'



--2. Podaj łączną wartość każdego zamówienia (uwzględnij cenę za przesyłkę)
select o.OrderID, (select sum(Quantity*UnitPrice*(1-Discount))
                   from [Order Details] od where o.OrderID = od.OrderID) + o.Freight as Total
from Orders o
order by 1
--lub
select o.OrderID, sum(Quantity*UnitPrice*(1-Discount)) + Freight as Total
from [Order Details] join Orders o on [Order Details].OrderID = o.OrderID
group by o.OrderID, Freight
order by 1



--3. Dla każdego produktu podaj maksymalną wartość zakupu tego produktu
select od.ProductID, max(UnitPrice*Quantity*(1-Discount)) as MaxOrderPrice
from [Order Details] od
group by od.ProductID
order by 1

--lub subquery
select od.ProductID, (select max(UnitPrice*Quantity*(1-Discount))
                      from [Order Details] odv where od.ProductID = odv.ProductID) as MaxOrderPrice
from [Order Details] od
group by od.ProductID
order by 1



--4. Dla każdego produktu podaj maksymalną wartość zakupu tego produktu w 1997r
select od.ProductID, max(UnitPrice*Quantity*(1-Discount)) as MaxOrderPrice
from [Order Details] od join Orders o on od.OrderID = o.OrderID
where YEAR(OrderDate) = 1997
group by od.ProductID
order by 1



----str 2 ćwiczenia
--1. Dla każdego klienta podaj łączną wartość jego zamówień (bez opłaty za przesyłkę) z 1996r
select CustomerID, sum(UnitPrice*Quantity*(1-Discount)) as CustomerTotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by CustomerID

--edycja dla każdego miesiąca w 1996
select CustomerID, MONTH(OrderDate) as Month, sum(UnitPrice*Quantity*(1-Discount)) as CustomerTotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by CustomerID, MONTH(OrderDate)


SELECT
    m.Month AS Month,
    SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS CustomerTotalPrice
FROM
    (VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12)) AS m(Month)
    LEFT JOIN Orders o ON MONTH(o.OrderDate) = m.Month AND YEAR(o.OrderDate) = 1996
    LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY m.Month
ORDER BY m.Month




--2. Dla każdego klienta podaj łączną wartość jego zamówień (uwzględnij opłatę za przesyłkę) z 1996r
select CustomerID, sum(UnitPrice*Quantity*(1-Discount)) + sum(DISTINCT o.Freight) as CustomerTotalPrice
from Orders o join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by CustomerID
-----------------------------------ŹLE bo może być różne OrderID u tego samego CustomerID
-- mające takie samo Freight i zliczy raz zamiast 2 razy!!!!!!!!!!!

EXCEPT

--zatem podzapytanie
select t.CustomerID, TotalSumOfFreight + TotalSumWithoutFreight as TotalValue
from (select o.CustomerID, sum(Quantity*UnitPrice*(1-Discount)) as TotalSumWithoutFreight
      from Orders o join [Order Details] od on o.OrderID = od.OrderID
      where YEAR(OrderDate) = 1996
      group by o.CustomerID) as t --dla danego CustomerID suma wartości zamówień
         join
     (select o.CustomerID, sum(o.Freight) as TotalSumOfFreight from Orders o
      where YEAR(OrderDate) = 1996 --dla danego CustomerID suma wartości freight
      group by o.CustomerID) as y on t.CustomerID = y.CustomerID
--OBA TAKI SAM WYNIK (to i niżej) ALE Z DOKŁADNOŚCIĄ DO UNIKALNYCH FREIGHT!!!
--jak damy o.OrderID w group by to za dużo rozdzieli na poziomie sumowania i trzeba by obłożyć jeszcze jednym selectem
--żeby potem sumowało już po CustomerID ale dodatkowo as y on t.CustomerID = y.CustomerID oraz t.OrderID = y.OrderID
--żeby połączyło tabele poprawnie nie tylko po samych CustomerID ale też zamówieniach :)

--lub
EXCEPT
select CustomerID, sum(TotalSumWithoutFreight) + sum(FreightTotal) as TotalValue --lub sum( + )
from (select o.CustomerID, sum(Quantity*UnitPrice*(1-Discount)) as TotalSumWithoutFreight,
             o.Freight as FreightTotal
      from Orders o join [Order Details] od on o.OrderID = od.OrderID
      where YEAR(OrderDate) = 1996
      group by o.CustomerID, o.OrderID, o.Freight) t -- najpiew klient kilka zamówień
--ale już unikalne OrderID i do nich jednorazowo freight, a potem dopiero sumujemy całość :)
--group by OrderID warto bo możemy stracić informację jeśli różne OrderID a takie same Freight
--dla tego samego CustomerID i za mało razy zliczymy Freight
group by CustomerID



--------TO ŹLE BO JEŚLI USUNIEMY GROUP BY OrderID i OrderDate w celu grupowania po klientach
--to Freight w group by spowoduje podział klienta jeśli miał różne Freight więc trzeba by było
--to obrać w selecta na zewnątrz i będzie git, a jeśli w group by usuniemy Freight to nie może on być
--w select luźno bez agregacji i źle
select o.OrderID, OrderDate, CompanyName, sum(Quantity*UnitPrice*(1-Discount)) + Freight as TotalPrice
from Orders o join Customers c on o.CustomerID = c.CustomerID
              join [Order Details] od on o.OrderID = od.OrderID
where YEAR(OrderDate) = 1996
group by o.OrderID, OrderDate, c.CustomerID, CompanyName, Freight


--tak już ok naprawione to wyżej :):):)
select t.CustomerID, sum(t.TotalPriceButDividedInternally) as TotalPrice
from  (select c.CustomerID, sum(Quantity*UnitPrice*(1-Discount)) + Freight as TotalPriceButDividedInternally
       from Orders o join Customers c on o.CustomerID = c.CustomerID
                     join [Order Details] od on o.OrderID = od.OrderID
       where YEAR(OrderDate) = 1996
       group by c.CustomerID, CompanyName, Freight) t
group by t.CustomerID
--różnica w EXCEPT bo zaokrągla np .49967 na .4997, jest dobrze <3





--3. Dla każdego klienta podaj maksymalną wartość zamówienia złożonego przez tego klienta w 1997r
select CustomerID, max(UnitPrice*Quantity*(1-Discount))
from Orders o join [Order Details] od on o.OrderID = od.OrderID
group by CustomerID -- oblicza tylko składowe zamówienia maksymalne
order by 2 desc -- trzeba by max (sum ()) ale się nie da

--zatem subquery trzeba
select CustomerID, max(OrderValue)  as MaxOrderValue
from (select o.CustomerID, o.OrderID, sum(Quantity*UnitPrice*(1-Discount)) as OrderValue
      from Orders o join [Order Details] od on o.OrderID = od.OrderID
      group by o.CustomerID, o.OrderID) as t
group by CustomerID
order by 2 desc


----------str4
--1. Czy są jacyś klienci którzy nie złożyli żadnego zamówienia w 1997 roku, jeśli tak to pokaż ich dane adresowe
select c.CustomerID, Address
from Customers c left join Orders o on c.CustomerID = o.CustomerID and YEAR(OrderDate) = 1997
where OrderID is null
--lub
select c.CustomerID, Address
from Customers c
where c.CustomerID not in (select o.CustomerID from Orders o
                           where YEAR(OrderDate) = 1997)

select c.CustomerID, Address
from Customers c
where not exists (select * from Orders o
                  where c.CustomerID = o.CustomerID and YEAR(OrderDate) = 1997)



--2. Wybierz nazwy i numery telefonów klientów , którym w 1997 roku przesyłki dostarczała firma United Package.
select DISTINCT c.CompanyName, c.Phone
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join Shippers s on o.ShipVia = s.ShipperID
where YEAR(OrderDate) = 1997 and s.CompanyName = 'United Package'
group by c.CustomerID, c.CompanyName, c.Phone -- CustomerID gdyby takie samy nazwy były


--lub
select c.CompanyName, c.Phone
from Customers c
where c.CustomerID in (select o.CustomerID
                       from Orders o join Shippers s on o.ShipVia = s.ShipperID
                       where YEAR(OrderDate) = 1997 and s.CompanyName = 'United Package' )



---jeśli np c.CompanyName jak i s.CompanyName mogą się powtarzać ale inne ID to można tak
SELECT DISTINCT c.CompanyName, c.Phone
FROM Customers c
WHERE c.CustomerID IN (
    SELECT o.CustomerID
    FROM Orders o
    WHERE YEAR(o.OrderDate) = 1997
  AND o.ShipVia IN (
SELECT s.ShipperID
FROM Shippers s
WHERE s.CompanyName = 'United Package'
    )
    );



--3. Wybierz nazwy i numery telefonów klientów , którym w 1997 roku przesyłek nie dostarczała firma United Package.
--ZAKŁADAM ŻE CHODZI O SHIPPEDDATE
select DISTINCT c.CompanyName, c.Phone
from Customers c left join Orders o on c.CustomerID = o.CustomerID
                 left join Shippers s on o.ShipVia = s.ShipperID and s.CompanyName = 'United Package'
    and YEAR(ShippedDate) = 1997
where s.CompanyName is null --źle bo w 1997 nie dostarczała ale w innych mogła...


--POPRAWNE
select c.CustomerID
from Customers c
where c.CustomerID not in ( select o.CustomerID
                            from Orders o join Shippers s on o.ShipVia = s.ShipperID
                            where s.CompanyName = 'United Package' and YEAR(ShippedDate) = 1997)
EXCEPT


--lub
select c.CustomerID, c.CompanyName, c.Phone
from Customers join Orders o on Customers.CustomerID = O.CustomerID
               join Shippers S on o.ShipVia = S.ShipperID and year(ShippedDate) = 1997
    and S.CompanyName = 'United Package'--którzy mają zamówienia
    right outer join Customers as c on c.CustomerID = Customers.CustomerID
--i do tego na KONIEC right join bierze dopełnienie razem z tymi co nie mają w ogóle
--          i tych którym right join dał nulla) takie trochę NOT IN
where Customers.CustomerID is null
EXCEPT

select c.CustomerID, c.CompanyName, c.Phone
from Customers c left join Orders o on c.CustomerID = o.CustomerID
                 left join Shippers s on o.ShipVia = s.ShipperID and YEAR(ShippedDate) = 1997
group by c.CustomerID, c.CompanyName, c.Phone
having sum(CASE WHEN s.CompanyName = 'United Package' THEN 1 ELSE 0 END) = 0




--4. Wybierz nazwy i numery telefonów klientów, którzy kupowali produkty z kategorii Confections.
select DISTINCT c.CompanyName, c.Phone
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
where CategoryName = 'Confections'

--lub XD

select distinct c.companyname, c.phone
from customers as c
where c.customerid in (
    select o.customerid
    from orders as o
    where o.orderid in (
        select od.orderid
        from [order details] as od
where od.productid in (
    select p.productid
    from products as p
    where p.categoryid in (
    select cat.categoryid
    from categories as cat
    where cat.categoryname = 'confections'
    )
    )
    )
    );


--5. Wybierz nazwy i numery telefonów klientów, którzy nie kupowali produktów z kategorii Confections.
SELECT c.CompanyName, c.Phone
FROM Customers c
WHERE c.CustomerID NOT IN (
    SELECT
        o.CustomerID
    FROM
        Orders o JOIN [Order Details] od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Categories cat ON p.CategoryID = cat.CategoryID
WHERE
    cat.CategoryName = 'Confections'
    );

--lub

SELECT c.CompanyName, c.Phone
FROM Customers c
         LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
         LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
    LEFT JOIN Products p ON od.ProductID = p.ProductID
    LEFT JOIN Categories cat ON p.CategoryID = cat.CategoryID
GROUP BY c.CompanyName, c.Phone  ---dotąd ma (91) group by jak distinct w 1. rozwiązaniu
HAVING SUM(CASE WHEN cat.CategoryName = 'Confections' THEN 1 ELSE 0 END) = 0

--lub
select DISTINCT c.CompanyName, c.Phone
from Customers join Orders o on Customers.CustomerID = o.CustomerID
               join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID and cat.CategoryName = 'Confections'
    right join Customers c on c.CustomerID = Customers.CustomerID -- dopełnienie tamtego ^
where Customers.CustomerID is null




--6. Wybierz nazwy i numery telefonów klientów, którzy w 1997r nie kupowali produktów z kategorii Confections.
select c.CompanyName, c.Phone
from Customers c
where c.CustomerID not in ( select o.CustomerID from Orders o
                            where YEAR(o.OrderDate) = 1997 and o.OrderID in (select od.OrderID from [Order Details] od
where od.ProductID in (select p.ProductID from Products p
    where p.CategoryID in (select cat.CategoryID from Categories cat
    where CategoryName = 'Confections' ))))

SELECT c.CompanyName, c.Phone ---to poprawne bo tylko 1997
FROM Customers c
         LEFT JOIN Orders o ON c.CustomerID = o.CustomerID and YEAR(o.OrderDate) = 1997
    LEFT JOIN [Order Details] od ON o.OrderID = od.OrderID
    LEFT JOIN Products p ON od.ProductID = p.ProductID
    LEFT JOIN Categories cat ON p.CategoryID = cat.CategoryID
GROUP BY c.CompanyName, c.Phone
HAVING SUM(CASE WHEN cat.CategoryName = 'Confections' THEN 1 ELSE 0 END) = 0;
--jeśli dalibyśmy poza left join warunek where YEAR(o.OrderDate) = 1997
--to wtedy wymuszam że klient musiał mieć jakieś zamówienie w 1997
--więc wynik (18) a nie musi mieć w ogóle w 1997 więc tak nie można i wynik poprawny (23)



---------------------------------- str 5
--1. Podaj wszystkie produkty których cena jest mniejsza niż średnia cena produktu
select  ProductID, ProductName, UnitPrice, (select avg(p.UnitPrice) from Products p) as Average
from Products
where Products.UnitPrice < (select avg(p.UnitPrice) from Products p)

--lub
select t.ProductID, t.ProductName, t.UnitPrice, Average
from (select ProductID, ProductName, UnitPrice,
             (select avg(p.UnitPrice) from Products p) as Average from Products) t
where UnitPrice < Average


--2. Podaj wszystkie produkty których cena jest mniejsza niż średnia cena produktu danej kategorii
select t.ProductName, t.CategoryID, UnitPrice, average
from (select p.ProductName, p.CategoryID, UnitPrice,
             (select avg(UnitPrice) from Products po where p.CategoryID = po.CategoryID) as average from Products p ) t
where t.UnitPrice < average


--3. Dla każdego produktu podaj jego nazwę, cenę, średnią cenę wszystkich produktów
-- oraz różnicę między ceną produktu a średnią ceną wszystkich produktów
select t.ProductName, t.UnitPrice, average, t.UnitPrice - average as TotalDiff
from (select ProductName, UnitPrice, (select avg(p.UnitPrice) from Products p) as average from Products) t


--4. Dla każdego produktu podaj jego nazwę kategorii, nazwę produktu, cenę, średnią cenę wszystkich
-- produktów danej kategorii oraz różnicę między ceną produktu a średnią ceną wszystkich produktów danej kategorii
select t.ProductName, t.UnitPrice, CategoryName, CatAverage, t.UnitPrice - CatAverage as CatDiff
from (select p.ProductName, p.UnitPrice, CategoryID, (select avg(UnitPrice) from Products po
                                                      where p.CategoryID = po.CategoryID ) as CatAverage from Products p) t
         join Categories c on t.CategoryID = c.CategoryID
Order by t.ProductName


select ProductID, ProductName, UnitPrice, average, UnitPrice - average as diff, CatName
from (select pout.ProductID, pout.ProductName, pout.UnitPrice,
             (select avg(UnitPrice) from Products pin where pout.CategoryID = pin.CategoryID ) as average,
             (select CategoryName from Categories cat where cat.CategoryID = pout.CategoryID ) as CatName from Products pout) t


SELECT p.ProductName, c.CategoryName, p.UnitPrice, AVG(p2.UnitPrice) AS CatAverage,
       p.UnitPrice - AVG(p2.UnitPrice) AS CatDiff
FROM Products p join Categories c ON p.CategoryID = c.CategoryID
                JOIN Products p2 ON p.CategoryID = p2.CategoryID --łączymy te same na podstawie CategoryID
GROUP BY p.CategoryID, p.ProductName, c.CategoryName, p.UnitPrice
ORDER BY c.CategoryName, p.ProductName; -- trzeba na innej tablicy bo na tej AVG(p.UnitPrice)
--będzie liczyło z jednego produktu i CatDiff = 0..., podobnie jak kiedyś z a.employee i b.employee





------------- str6
--1. Podaj produkty kupowane przez więcej niż jednego klienta
select t.ProductID, COUNT(DISTINCT t.CustomerID) as IluKlientówKupowało
from (select c.CustomerID, p.ProductID from Customers c join Orders o on c.CustomerID = o.CustomerID
                                                        join [Order Details] od on o.OrderID = od.OrderID
          join Products p on od.ProductID = p.ProductID) t
group by t.ProductID
having COUNT(DISTINCT t.CustomerID) > 1
ORDER BY 1

SELECT p.ProductID, p.ProductName, COUNT(DISTINCT o.CustomerID) AS NumberOfCustomers
FROM Products p JOIN [Order Details] od ON p.ProductID = od.ProductID
    JOIN Orders o ON od.OrderID = o.OrderID
GROUP BY p.ProductID, p.ProductName
HAVING COUNT(DISTINCT o.CustomerID) > 1;


--2. Podaj produkty kupowane w 1997r przez więcej niż jednego klienta
select t.ProductID, COUNT(DISTINCT t.CustomerID) as IluKlientówKupowało
from (select c.CustomerID, p.ProductID from Customers c join Orders o on c.CustomerID = o.CustomerID and YEAR(OrderDate) = 1997
                                                        join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID) t
group by t.ProductID
having COUNT(DISTINCT t.CustomerID) > 1
ORDER BY 1

SELECT p.ProductID, p.ProductName, COUNT(DISTINCT o.CustomerID) AS NumberOfCustomers
FROM Products p JOIN [Order Details] od ON p.ProductID = od.ProductID
    JOIN Orders o ON od.OrderID = o.OrderID and YEAR(OrderDate) = 1997
GROUP BY p.ProductID, p.ProductName
HAVING COUNT(DISTINCT o.CustomerID) > 1;


--3. Podaj nazwy klientów którzy w 1997r kupili co najmniej dwa różne produkty z kategorii 'Confections'
select t.CompanyName
from (select c.CompanyName from Customers c join Orders o on c.CustomerID = o.CustomerID
                                            join [Order Details] od on o.OrderID = od.OrderID
          join Products p on od.ProductID = p.ProductID
          join Categories cat on p.CategoryID = cat.CategoryID
      where CategoryName = 'Confections' and YEAR(OrderDate) = 1997
      group by c.CompanyName
      having COUNT(DISTINCT p.ProductID) > 1) t

--ten zapis wyżej trochę sztuczny

select c.CompanyName
from Customers c join Orders o on c.CustomerID = o.CustomerID and YEAR(OrderDate) = 1997
    join [Order Details] od on o.OrderID = od.OrderID
    join Products p on od.ProductID = p.ProductID
    join Categories cat on p.CategoryID = cat.CategoryID
where YEAR(OrderDate) = 1997 and cat.CategoryName = 'Confections'
group by c.CompanyName
having COUNT(DISTINCT p.ProductID) > 1




--------------------str 7
--1. Dla każdego pracownika (imię i nazwisko) podaj łączną wartość zamówień obsłużonych
-- przez tego pracownika, przy obliczaniu wartości zamówień uwzględnij cenę za przesyłkę
select FirstName, LastName, sum(PriceDividedOnEmployees) as TotalPrice
from ( select e.EmployeeID, FirstName, LastName, sum(UnitPrice*Quantity*(1-Discount)) + o.Freight as PriceDividedOnEmployees
       from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                        join [Order Details] od on o.OrderID = od.OrderID
       group by e.EmployeeID, FirstName, LastName, o.Freight, o.OrderID ) as t
group by EmployeeID, FirstName, LastName
-------ŹLE ZA DUŻO ZLICZA PROBLEM Z FREIGHT

-- OK :):):)
select FirstName, LastName, sum(ValueOfFreight) + sum(ValueWithoutFreight) as TotalValue --lub sum (.. + ..)
from (  select e.EmployeeID, FirstName, LastName, sum(UnitPrice*Quantity*(1-Discount)) as ValueWithoutFreight,
               o.Freight ValueOfFreight
        from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                         join [Order Details] od on o.OrderID = od.OrderID
        group by e.EmployeeID, o.OrderID, FirstName, LastName, o.Freight ) t
group by EmployeeID, FirstName, LastName
--!!!!Musi być o.OrderID inaczej jeśli takie samo Freight to policzy za mało razy Freight tak jakby
--to było jedno zamówienie a może być takich np 10

-------------------------------------------------------

--DIY
--Wybierz nazwy i numery telefonów klientów , którym w 1997 roku przesyłki dostarczała tylko firma United Package.
select c.CompanyName, c.Phone
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join Shippers s on o.ShipVia = s.ShipperID and YEAR(OrderDate) = 1997
group by c.CustomerID, c.CompanyName, c.Phone
having sum(CASE WHEN s.CompanyName = 'United Package' then 0 else 1 end) = 0

select c.CompanyName, ShipVia, YEAR(OrderDate)
from Customers c join Orders o on c.CustomerID = o.CustomerID
    join Shippers s on o.ShipVia = s.ShipperID
where c.CompanyName = 'Split Rail Beer & Ale' --sprawdzenie

--jeśli we wszystkich latach tylko firma United Package to
select c.CompanyName, c.Phone
from Customers c join Orders o on c.CustomerID = o.CustomerID
                 join Shippers s on o.ShipVia = s.ShipperID
group by c.CustomerID, c.CompanyName, c.Phone
having sum(CASE WHEN s.CompanyName = 'United Package' then 0 else 1 end) = 0


select c.CompanyName, ShipVia, YEAR(OrderDate)
from Customers c join Orders o on c.CustomerID = o.CustomerID
    join Shippers s on o.ShipVia = s.ShipperID
where c.CompanyName = 'Let''s Stop N Shop' --sprawdzenie, rzeczywiście <3




--------------------------
select c.CompanyName, c.Phone
from Customers c left join Orders o on c.CustomerID = o.CustomerID
                 left join Shippers s on o.ShipVia = s.ShipperID and YEAR(OrderDate) = 1997
group by c.CustomerID, c.CompanyName, c.Phone
having sum(CASE WHEN s.CompanyName = 'United Package' THEN 1 ELSE 0 END) = 0



---------


select t.EmployeeID, sum(Total + Freight)
from (select e.EmployeeID, sum(UnitPrice*od.Quantity*(1-Discount)) as Total, o.Freight as Freight
      from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                       join [Order Details] od on o.OrderID = od.OrderID
      group by e.EmployeeID, o.OrderID, o.Freight) t
group by t.EmployeeID


-- Dla każdego pracownika (imię i nazwisko) podaj łączną wartość zamówień obsłużonych przez
--tego pracownika. Ogranicz wynik tylko do pracowników (utrudniłem + przesyłka)
-- c) mają podwładnego i szefa
select b.EmployeeID
from Employees a right join Employees b on a.EmployeeID = b.ReportsTo -- a są szefem b
where a.EmployeeID is null-- nie ma szefa (w ReportsTo '2' ma nulla bo nie ma szefa, więc
--dla tej krotki w b.ReporstTo null, b.EmployeeID = 2, a.EmployeeID null)


select t.EmployeeID, t.LastName, t.FirstName, sum(TotalSumWithoutFreight) + sum(Freight) as TotalSum
from (select e.EmployeeID, e.LastName, e.FirstName, sum(UnitPrice*Quantity*(1-Discount)) as TotalSumWithoutFreight,
             o.Freight as Freight
      from Employees e join Orders o on e.EmployeeID = o.EmployeeID
                       join [Order Details] od on o.OrderID = od.OrderID
      where e.EmployeeID IN ((select a.EmployeeID
          from Employees a join Employees b on a.EmployeeID = b.ReportsTo) --mają podwładnych
          INTERSECT
          (select b.EmployeeID
          from Employees a right join Employees b on a.EmployeeID = b.ReportsTo -- a są szefem b
          where a.EmployeeID is not null)) -- ma szefa
      group by e.EmployeeID, o.OrderID, o.Freight, e.LastName, e.FirstName) t
group by t.EmployeeID, t.LastName, t.FirstName


--kolos
select t.CustomerID, sum(PriceWithoutFreight + AmountFreight) as WartośćZamówień, COUNT(t.CustomerID) as LiczbaZamówień
from (select c.CompanyName, c.CustomerID, sum(Quantity*UnitPrice*(1-Discount)) as PriceWithoutFreight,
             o.Freight as AmountFreight
      from Customers c join Orders o on c.CustomerID = o.CustomerID
                       join [Order Details] od on o.OrderID = od.OrderID
          and YEAR(OrderDate) = 1997 and MONTH(OrderDate) = 2
      group by c.CompanyName, c.CustomerID, o.OrderID, o.Freight ) t
group by t.CustomerID
UNION
select cust.CompanyName , 0 as WartośćZamówień, 0 as LiczbaZamówień
from Customers cust left join Orders o on cust.CustomerID = o.CustomerID
    and YEAR(OrderDate) = 1997 and MONTH(OrderDate) = 2
where o.CustomerID is null

