select ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i
join ANIMAL_OUTS
    using(ANIMAL_ID)
where SEX_UPON_INTAKE like "Intact%"
    and (SEX_UPON_OUTCOME like "Spayed%" or SEX_UPON_OUTCOME like "Neutered%")
order by ANIMAL_ID