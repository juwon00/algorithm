select INGREDIENT_TYPE, sum(TOTAL_ORDER)
from FIRST_HALF
join ICECREAM_INFO
    using(FLAVOR)
group by INGREDIENT_TYPE