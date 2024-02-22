with recursive time as (
    select 0 as HOUR
    union all
    select HOUR+1 from time where HOUR<23
)

select HOUR, ifnull(COUNT, 0) as COUNT
from (
    select HOUR(DATETIME) as HOUR, count(*) as COUNT
    from ANIMAL_OUTS
    group by HOUR(DATETIME)
    order by HOUR(DATETIME)
) as a
right join time
using(HOUR)