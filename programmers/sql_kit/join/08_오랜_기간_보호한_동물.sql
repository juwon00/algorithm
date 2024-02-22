select NAME, DATETIME
from ANIMAL_INS
where ANIMAL_ID not in (
    select ANIMAL_ID
    from ANIMAL_INS
    join ANIMAL_OUTS
        using(ANIMAL_ID)
)
order by DATETIME
limit 3