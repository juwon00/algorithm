select CAR_ID, CAR_TYPE, floor(DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100) as FEE
from CAR_RENTAL_COMPANY_CAR
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    using(CAR_TYPE)
where DURATION_TYPE = "30일 이상"
    and CAR_TYPE in ("세단", "SUV")
    and CAR_ID not in (
        select CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE END_DATE >= "2022-11-01" and START_DATE <= "2022-11-30"
    )
having FEE >= 500000 and FEE < 2000000
order by FEE desc, CAR_TYPE asc, CAR_ID desc