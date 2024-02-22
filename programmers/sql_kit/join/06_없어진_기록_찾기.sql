select ANIMAL_ID, NAME
from ANIMAL_OUTS
where ANIMAL_ID not in (
    select ANIMAL_ID
    from ANIMAL_INS
    join ANIMAL_OUTS
        using(ANIMAL_ID)
    order by ANIMAL_ID
)