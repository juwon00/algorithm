select f.FLAVOR
from ICECREAM_INFO as i join FIRST_HALF as f
on i.FLAVOR = f.FLAVOR
where f.TOTAL_ORDER >= 3000 and i.INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc