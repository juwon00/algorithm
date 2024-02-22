select distinct(CAR_ID)
from CAR_RENTAL_COMPANY_CAR
join CAR_RENTAL_COMPANY_RENTAL_HISTORY
    using(CAR_ID)
where START_DATE like "2022-10%" and CAR_TYPE = "세단"
order by CAR_ID desc