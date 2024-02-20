select *
from (
    select WRITER_ID, NICKNAME, sum(PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD b
    join USED_GOODS_USER u
    on b.WRITER_ID = u.USER_ID
    where STATUS = "DONE"
    group by WRITER_ID
) as t
where TOTAL_SALES >= 700000
order by TOTAL_SALES asc
