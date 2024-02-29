with FRONT as (
    select sum(CODE) as CODE
    from SKILLCODES
    where CATEGORY = 'FRONT END'
)

select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (select CODE from FRONT)
order by ID