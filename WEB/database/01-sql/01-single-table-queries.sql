-- 01. Querying data
-- select Name, Milliseconds/60000 as '재생 시간(분)' from tracks;

-- 02. Sorting data
-- select FirstName from employees order by FirstName DESC ;
-- select Country, City from customers order by Country DESC, City;
-- select tracks.Name, Milliseconds/60000 as '재생 시간(분)' from tracks order by Milliseconds DESC ;
-- select ReportsTo from employees order by ReportsTo;

-- NULL 정렬 예시

-- 03. Filtering data
-- select distinct Country from customers order by Country;
-- select LastName, FirstName, City from customers where City = 'Prague';
-- select customers.LastName, customers.FirstName, customers.City from customers where City != 'Prague';
-- select customers.LastName, customers.FirstName, customers.Company, customers.Country
-- from customers
-- where Company is NULL
--   and Country = 'USA';

-- select c.LastName, c.FirstName, c.Company, c.Country
-- from customers c
-- where c.Company is null or
--       c.Country = 'USA';

-- select t.name, t.Bytes
-- from tracks t
-- where Bytes between 10000 and 500000;
-- where t.Bytes >= 10000 and
--       t.Bytes <= 500000;

-- select Name, Bytes
-- from tracks
-- where Bytes between 10000 and 500000
-- order by Bytes;

-- select LastName, FirstName, Country
-- from customers
-- where Country in ('Canada', 'Germany', 'France');
-- where Country = 'Canada' or Country = 'Germany' or Country = 'France';

-- select LastName, FirstName, Country
-- from customers
-- where Country not in ('Canada', 'Germany', 'France');

-- select LastName, FirstName
-- from customers
-- where LastName like '%son';


-- select LastName, FirstName
-- from customers
-- where FirstName like '___a';

-- select TrackId, name, Bytes
-- from tracks
-- order by Bytes DESC
-- limit 7;

-- select TrackId, Name, Bytes
-- from tracks
-- order by Bytes DESC
-- limit 3, 4;

-- 04. Grouping data
-- select Composer, avg(Bytes) as avgOfBytes
-- from tracks
-- group by Composer
-- order by avgOfBytes desc;

select Composer, avg(Milliseconds/60000) as avgOfMinute
from tracks
group by Composer
having avgOfMinute < 10;
