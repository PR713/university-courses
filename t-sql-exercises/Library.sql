
--------------------
-------------------- 0 lab ćwiczenia str 1

--Napisz polecenie select za pomocą którego uzyskasz identyfikator/numer
--tytułu oraz tytuł książki

select title, title_no
from title

---Napisz polecenie, które wybiera tytuł o numerze/identyfikatorze 10
select title, title_no
from title
where title_no = 10

--Napisz polecenie select, za pomocą którego uzyskasz numer książki (nr tyułu)
--i autora dla wszystkich książek, których autorem jest Charles Dickens
--lub Jane Austen
select title_no, author
from title
where author in ('Charles Dickens', 'Jane Austen')

---- str 2
--Napisz polecenie, które wybiera numer tytułu i tytuł dla wszystkich  książek,
-- których tytuły zawierających słowo 'adventure'

select title_no, title
from title
where title like '%adventure%'

--Napisz polecenie, które wybiera numer czytelnika, oraz zapłaconą karę dla
--wszystkich książek, ktore zostały zwrócone w listopadzie 2001

select member_no, fine_paid, in_date, due_date
from loanhist
where in_date >= '2001-11-01' and in_date < '2001-12-01'
  and fine_paid is not null

--Napisz polecenie, które wybiera wszystkie unikalne pary
--miast i stanów z tablicy adult.

select DISTINCT city, state
from adult

--Napisz polecenie, które wybiera wszystkie tytuły z tablicy
-- title i wyświetla je w porządku alfabetycznym.

select title
from title
order by 1


-- str 3
--Napisz polecenie, które: wybiera numer członka biblioteki (member_no),
--isbn książki (isbn) i wartość naliczonej kary (fine_assessed) z tablicy
--loanhist  dla wszystkich wypożyczeń/zwrotów, dla których naliczono karę
--(wartość nie NULL w kolumnie fine_assessed)

select member_no, isbn, fine_assessed, fine_assessed * 2 as double_fine,
       (fine_assessed * 2) - fine_assessed as diff
from loanhist
where fine_assessed is not null and (fine_assessed * 2) - fine_assessed > 3

---str 4
--Napisz polecenie, które generuje pojedynczą kolumnę, która zawiera kolumny:
--firstname (imię członka biblioteki), middleinitial (inicjał drugiego imienia)
--i lastname (nazwisko) z tablicy member dla wszystkich członków biblioteki,
--którzy nazywają się Anderson nazwij tak powstałą kolumnę email_name (użyj
--aliasu email_name dla kolumny)

select concat(firstname,', ', middleinitial, ', ', lastname) as email_name
from member
where lastname = 'Anderson'

--zmodyfikuj polecenie, tak by zwróciło 'listę proponowanych loginów e-mail'
--utworzonych przez połączenie imienia członka biblioteki, z inicjałem drugiego
--imienia i pierwszymi dwoma literami nazwiska (wszystko małymi małymi literami).
--wykorzystaj funkcję SUBSTRING do uzyskania części kolumny znakowej oraz LOWER do
--zwrócenia wyniku małymi literami. Wykorzystaj operator (+) do połączenia napisów.

select concat(firstname,', ', middleinitial, ', ', lastname) as email_name,
       REPLACE(LOWER(firstname + middleinitial + SUBSTRING(lastname,1,2) + '@gmail.com'), ' ', '') as login_email
from member


--- str 5
--Napisz polecenie, które wybiera title i title_no z tablicy title. wynikiem powinna
--być pojedyncza kolumna o formacie jak w przykładzie poniżej: The title is: Poems,
--title number 7 czyli zapytanie powinno zwracać pojedynczą kolumnę w oparciu o wyrażenie,
--które łączy 4 elementy: stała znakowa ‘The title is:’ , wartość kolumny title, stała
--znakowa ‘title number’ , wartość kolumny title_no
--jeśli się użyje + title_no to trzeba str(title_no) ale się rozjeżdża wynik: title number     3
SELECT CONCAT('The title is: ', title, ', title number ', title_no) AS TitleNumber
FROM title;



-----------
----------- Ćwiczenia group by

----------- str 2

-- 1. Ilu jest dorosłych czytelników?

select COUNT(member_no)
from adult

-- 2. Ile jest dzieci zapisanych do biblioteki
select adult_member_no, COUNT(adult_member_no)
from juvenile
group by adult_member_no

-- 3. Ilu z dorosłych czytelników mieszka w Kaliforni (CA)
select count(member_no) as Adult
from adult
where state = 'CA'

-- 4. Dla każdego dorosłego czytelnika podaj liczbę jego dzieci.
select adult_member_no, COUNT(member_no) as LiczbaDzieci
from juvenile
group by adult_member_no

-- 5. Dla każdego dorosłego czytelnika podaj liczbę jego dzieci
-- urodzonych przed 1998r

select adult_member_no, COUNT(member_no) as LiczbaDzieciPrzed98
from juvenile
where birth_date < '1998-01-01'
group by adult_member_no


-------- str 3

-- 1. Dla każdego czytelnika podaj liczbę zarezerwowanych przez niego książek
select member_no, COUNT(member_no) as LiczbaZarezewKsiążek
from reservation
group by member_no

-- 2. Dla każdego czytelnika podaj liczbę wypożyczonych przez niego książek
select member_no, COUNT(copy_no) as WypożyczoneKsiążki
from loan
group by member_no


-- 3. Dla każdego czytelnika podaj liczbę książek zwróconych przez niego w 2001r.
select member_no, COUNT(in_date) as ZwróconeKsiążki
from loanhist
where in_date >= '2001-01-01' and in_date < '2002-01-01'
group by member_no

-- 4. Dla każdego czytelnika podaj sumę kar jakie zapłacił w 2001r

select member_no, sum(fine_paid) as TotalFinePaid
from loanhist
where in_date >= '2001-01-01' and in_date < '2002-01-01' and fine_paid is not null
group by member_no

-- 5. Ile książek wypożyczono w maju 2001
select COUNT(out_date) as WypożyczoneWMaju01
from loanhist
where out_date >= '2001-05-01' and out_date < '2001-06-01'


--select due_date, in_date, out_date
--from loanhist
--where in_date > due_date --> then fine to pay

-- 6. Na jak długo średnio były wypożyczane książki w maju 2001
select avg(DATEDIFF(day,out_date,in_date)) as ŚredniCzasWypożycz
from loanhist
where out_date >= '2001-05-01' and out_date < '2001-06-01'



-----------------------str 18

--1.Napisz polecenie, które wyświetla listę dzieci będących członkami biblioteki (baza library).
-- Interesuje nas imię, nazwisko i data urodzenia dziecka.
select firstname, lastname, juvenile.birth_date
from member inner join juvenile
                       on member.member_no = juvenile.member_no;


--2.Napisz polecenie, które podaje tytuły aktualnie wypożyczonych książek

select distinct title, on_loan
from copy c join title t on t.title_no = c.title_no
where on_loan = 'Y'


--3. Podaj informacje o karach zapłaconych za przetrzymywanie książki o tytule
-- ‘Tao Teh King’. Interesuje nas data oddania książki, ile dni była przetrzymywana
-- i jaką zapłacono karę

select title, fine_paid, due_date, in_date
from loanhist l join title t on l.title_no = t.title_no
where title = 'Tao Teh King' and fine_paid is not null and DATEDIFF(DAY, in_date,due_date) > 0
--in_date to data do kiedy można było oddać, due_date to kiedy oddano
--a due date w loan to już do kiedy można oddać, więc pomieszane...

--4. Napisz polecenie które podaje listę książek (numery ISBN) zarezerwowanych przez osobę
-- o nazwisku: Stephen A. Graff

select isbn, lastname, firstname
from reservation r join member m on m.member_no = r.member_no
where firstname = 'Stephen' and middleinitial = 'A' and lastname = 'Graff'


---------------------------str26
--1. Napisz polecenie, które wyświetla listę dzieci będących członkami biblioteki (baza library).
-- Interesuje nas imię, nazwisko, data urodzenia dziecka i adres zamieszkania dziecka.
select firstname, lastname, birth_date, (state + ' ' + city + ' ' +  street + ' ' + zip) as Address
from member join juvenile on member.member_no = juvenile.member_no
            join adult on juvenile.adult_member_no = adult.member_no


--2. Napisz polecenie, które wyświetla listę dzieci będących członkami biblioteki (baza library).
-- Interesuje nas imię, nazwisko, data urodzenia dziecka, adres zamieszkania dziecka oraz imię i nazwisko rodzica.

select membjuveni.firstname as FirstName, membjuveni.lastname as LastName, birth_date, (state + ' ' + city + ' ' +  street + ' ' + zip) as Address,
       membadul.firstname as AdultFirstName, membadul.lastname as AdultLastName, adult.member_no
from juvenile
         join member as membjuveni on juvenile.member_no = membjuveni.member_no
         join adult on adult.member_no = juvenile.adult_member_no -- normalnie te dwa dla 3 tablic
         join member as membadul on membadul.member_no = adult.member_no -- ale dodatkowo to



----------------str 34
--1. Podaj listę członków biblioteki mieszkających w Arizonie (AZ) mają
-- więcej niż dwoje dzieci zapisanych do biblioteki
select state, ma.firstname + ' ' + ma.lastname as FullName, COUNT(adult_member_no) as LiczbaDzieci
from adult join member ma on adult.member_no = ma.member_no
           join juvenile on adult.member_no = juvenile.adult_member_no
where state = 'AZ'
group by state, ma.firstname, ma.lastname
having COUNT(adult_member_no) > 2


--2. Podaj listę członków biblioteki mieszkających w Arizonie (AZ) którzy mają  więcej niż dwoje dzieci
--zapisanych do biblioteki oraz takich którzy mieszkają w Kaliforni (CA) i mają więcej niż troje dzieci
-- zapisanych do biblioteki

select state, ma.firstname + ' ' + ma.lastname as FullName, COUNT(adult_member_no) as LiczbaDzieci
from adult join member ma on adult.member_no = ma.member_no
           join juvenile on adult.member_no = juvenile.adult_member_no
where state = 'AZ'
group by state, ma.firstname, ma.lastname
having COUNT(adult_member_no) > 2
UNION
select state, ma.firstname + ' ' + ma.lastname as FullName, COUNT(adult_member_no) as LiczbaDzieci
from adult join member ma on adult.member_no = ma.member_no
           join juvenile on adult.member_no = juvenile.adult_member_no
where state = 'CA'
group by state, ma.firstname, ma.lastname
having COUNT(adult_member_no) > 3




---albo tak:
select state, ma.firstname + ' ' + ma.lastname as FullName, COUNT(adult_member_no) as LiczbaDzieci
from adult join member ma on adult.member_no = ma.member_no
           join juvenile on adult.member_no = juvenile.adult_member_no
where state = 'AZ' or state = 'CA'
group by state, ma.firstname, ma.lastname
having (state = 'AZ' and COUNT(adult_member_no) > 2) or (state = 'CA' and COUNT(adult_member_no) > 3)





-----------------------------subquery




-----------str3
--1. Dla każdego dorosłego członka biblioteki podaj jego imię, nazwisko oraz liczbę jego dzieci.
select LastName, FirstName, (select COUNT(j.adult_member_no)
                             from juvenile j where a.member_no = j.adult_member_no) as LiczbaDzieci
from member m join adult a on m.member_no = a.member_no
--adult i member są połączone OK
--!!!ALL rows inaczej pokaże różne liczby dzieci

select a.member_no, m.FirstName, m.LastName, COUNT(j.adult_member_no) as LiczbaDzieci
from adult a join member m on a.member_no = m.member_no
             join juvenile j on a.member_no = j.adult_member_no
group by a.member_no, m.FirstName, m.LastName
order by a.member_no



--2. Dla każdego dorosłego członka biblioteki podaj jego imię, nazwisko, liczbę jego dzieci,
-- liczbę zarezerwowanych książek oraz liczbę wypożyczonych książek.
select LastName, FirstName, (select COUNT(j.adult_member_no)
                             from juvenile j where a.member_no = j.adult_member_no) as LiczbaDzieci,
       (select COUNT(r.member_no)
        from reservation r where a.member_no = r.member_no) as LiczbaRezerwacji,
       (select COUNT(l.member_no)
        from loan l where a.member_no = l.member_no) as LiczbaWypożyczonych
from member m join adult a on m.member_no = a.member_no

--lub
SELECT m.member_no, COUNT(DISTINCT j.member_no) AS LiczbaDzieci, COUNT(DISTINCT r.member_no) AS LiczbaRezerwacji,
       COUNT(DISTINCT l.member_no) AS LiczbaWypożyczonych
FROM member m JOIN adult a ON m.member_no = a.member_no
              LEFT JOIN juvenile j ON a.member_no = j.adult_member_no
              LEFT JOIN reservation r ON a.member_no = r.member_no
              LEFT JOIN loan l ON a.member_no = l.member_no
group by m.member_no
order by 2 desc




--3. Dla każdego dorosłego członka biblioteki podaj jego imię, nazwisko, liczbę jego dzieci,
-- oraz liczbę książek zarezerwowanych i wypożyczonych przez niego i jego dzieci.
--------------nie mam


--4. Dla każdego tytułu książki podaj ile razy ten tytuł był wypożyczany w 2001r
select title, sum(LiczbaWypożyczeń) as LiczbaWypożyczeń
from (   select title, COUNT(l.title_no) as LiczbaWypożyczeń
         from title t left join loan l on t.title_no = l.title_no
         where YEAR(l.out_date) = 2001
         group by title
         UNION
         select title, COUNT(lh.title_no) as LiczbaWypożyczeń
         from title t left join loanhist lh on t.title_no = lh.title_no
         where YEAR(lh.out_date) = 2001
         group by title) as LiczbaWypożyczeń
group by title

--select title, COUNT(l.title_no) as LiczbaWypożyczeń
--from title t left join loan l on t.title_no = l.title_no
--left join loanhist lh on t.title_no = lh.title_no
--where YEAR(l.out_date) = 2001 or YEAR(lh.out_date) = 2001
--group by title NIEPOPRAWNE ŁĄCZENIE PEWNIE JAKOŚ

--5. Dla każdego tytułu książki podaj ile razy ten tytuł był wypożyczany w 2002r
select title, sum(LiczbaWypożyczeń) as LiczbaWypożyczeń
from (   select title, COUNT(l.title_no) as LiczbaWypożyczeń
         from title t left join loan l on t.title_no = l.title_no
         where YEAR(l.out_date) = 2002
         group by title
         UNION
         select title, COUNT(lh.title_no) as LiczbaWypożyczeń
         from title t left join loanhist lh on t.title_no = lh.title_no
         where YEAR(lh.out_date) = 2002
         group by title) as LiczbaWypożyczeń
group by title




--kolos
select firstname, lastname, (state + ', ' + city + ', ' + street + ', ' + zip) as FullAddress
from juvenile j1 join member m on j1.member_no = m.member_no
                 join adult a on j1.adult_member_no = a.member_no
where j1.member_no NOT IN (
    select j.member_no
    from member m join juvenile j on m.member_no = j.member_no
                  join loanhist lh on lh.member_no = j.member_no
                  join title t on lh.title_no = t.title_no
    where CAST(in_date as date) = '2001-12-14' and title = 'Walking'
)
group by j1.member_no, firstname, lastname, (state + ', ' + city + ', ' + street + ', ' + zip)
