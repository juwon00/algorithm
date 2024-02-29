-- x & 2  <- x를 2진수로 나타내는데 2가 필요하면 true

with FRONT as (
    select sum(CODE) as CODE
    from SKILLCODES
    where CATEGORY = 'FRONT END'
)

select
    case
        when (d.SKILL_CODE & (select CODE from FRONT)) and (d.SKILL_CODE & (select CODE from SKILLCODES where NAME = 'Python')) then 'A'
        when (d.SKILL_CODE & (select CODE from SKILLCODES where NAME = 'C#')) then 'B'
        when (d.SKILL_CODE & (select CODE from FRONT)) then 'C'
    end as GRADE,
    d.ID, d.EMAIL
from DEVELOPERS d
having GRADE is not null
order by GRADE asc, ID asc