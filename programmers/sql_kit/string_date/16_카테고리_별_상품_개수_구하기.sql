select substring(PRODUCT_CODE from 1 for 2) as CATEGORY, count(substring(PRODUCT_CODE from 1 for 2)) as PRODUCTS
from PRODUCT
group by substring(PRODUCT_CODE from 1 for 2)
order by CATEGORY