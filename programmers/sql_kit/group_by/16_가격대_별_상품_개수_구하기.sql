select (PRICE div 10000) * 10000 as  PRICE_GROUP, count(*) as PRODUCTS
from PRODUCT
group by (PRICE div 10000)
order by PRICE_GROUP