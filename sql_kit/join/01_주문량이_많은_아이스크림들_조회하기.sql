select FLAVOR
from FIRST_HALF
join (
    select FLAVOR, sum(TOTAL_ORDER) as JULY_TOTAL_ORDER
    from JULY
    group by FLAVOR
) as j
    using(FLAVOR)
order by (TOTAL_ORDER + JULY_TOTAL_ORDER) desc
limit 3


