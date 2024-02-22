select ANIMAL_ID, i.NAME #, datediff(o.DATETIME, i.DATETIME) + 1
from ANIMAL_INS as i
join ANIMAL_OUTS as o
    using(ANIMAL_ID)
order by datediff(o.DATETIME, i.DATETIME) + 1 desc
limit 2