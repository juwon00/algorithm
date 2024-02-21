select y as YEAR, m as MONTH, count(*) as PUCHASED_USERS,
round(count(*) / (
    select count(*)
    from USER_INFO
    where JOINED like "2021%"
), 1) as PUCHASED_RATIO
from (
    select USER_ID, count(*) as c, YEAR(SALES_DATE) as y, MONTH(SALES_DATE) as m
    from ONLINE_SALE
    where USER_ID in (
        select USER_ID
        from USER_INFO
        where JOINED like "2021%"
    )
    group by USER_ID, YEAR(SALES_DATE), MONTH(SALES_DATE)
) as t1
group by y, m
order by YEAR asc, MONTH asc
