-- group by 정의한 FOOD_TYPE만 그대로 사용할 수 있음

select r1.FOOD_TYPE, r1.REST_ID, r1.REST_NAME, r1.FAVORITES
from REST_INFO r1
join (
    select FOOD_TYPE, max(FAVORITES) as "FAVORITES"
    from REST_INFO
    group by FOOD_TYPE
) r2
on r1.FOOD_TYPE = r2.FOOD_TYPE and r1.FAVORITES = r2.FAVORITES
order by FOOD_TYPE desc