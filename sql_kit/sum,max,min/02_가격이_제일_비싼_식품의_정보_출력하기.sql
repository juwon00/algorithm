select *
from FOOD_PRODUCT
where price = (
    select max(price)
    from FOOD_PRODUCT
)