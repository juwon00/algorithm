select distinct(HISTORY_ID),
    case
        when DATEDIFF(END_DATE, START_DATE) + 1 >= 90
        then round((DATEDIFF(END_DATE, START_DATE) + 1) * DAILY_FEE * (
            select (100-DISCOUNT_RATE)/100
            from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            where car_type = '트럭' and duration_type = '90일 이상')
        )
        when DATEDIFF(END_DATE, START_DATE) + 1 between 30 and 89
        then round((DATEDIFF(END_DATE, START_DATE) + 1) * DAILY_FEE *(
            select (100-DISCOUNT_RATE)/100
            from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            where car_type = '트럭' and duration_type = '30일 이상')
        )
        when DATEDIFF(END_DATE, START_DATE) + 1 between 7 and 29
        then round((DATEDIFF(END_DATE, START_DATE) + 1) * DAILY_FEE *(
            select (100-DISCOUNT_RATE)/100
            from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            where CAR_TYPE = '트럭' and DURATION_TYPE = '7일 이상')
        )
        else round((DATEDIFF(END_DATE, START_DATE) + 1) * DAILY_FEE)
    end as FEE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
join CAR_RENTAL_COMPANY_CAR
    using(CAR_ID)
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    using(CAR_TYPE)
where CAR_TYPE = "트럭"
order by FEE desc, HISTORY_ID desc