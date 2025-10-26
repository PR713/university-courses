
select * from Produce
select * from Buyers
select * from sales


select buyer_name, s.buyer_id, qty
from buyers b inner join sales s
                         on b.buyer_id = s.buyer_id


select buyer_name, s.buyer_id, qty -- widzimy też tych co nic nie kupili Sean
from buyers b left outer join sales s --kolejność ma znaczenie, jeśli sales po prawej to RIGHT
                              on b.buyer_id = s.buyer_id
--where s.buyer_id is null


-------------------------
select buyer_name, prod_name, qty
from buyers b inner join sales s
                         on b.buyer_id = s.buyer_id
              inner join produce p
                         on s.prod_id = p.prod_id
--lub
select buyer_name, prod_name, qty
from buyers b, sales s, produce p
where b.buyer_id = s.buyer_id and s.prod_id = p.prod_id