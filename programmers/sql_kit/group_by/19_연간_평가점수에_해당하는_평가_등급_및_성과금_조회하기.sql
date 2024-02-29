select EMP_NO, EMP_NAME, GRADE,
    case
        when GRADE = 'S' then SAL * 0.2
        when GRADE = 'A' then SAL * 0.15
        when GRADE = 'B' then SAL * 0.1
        when GRADE = 'C' then 0
    end as BONUS
from (
    select EMP_NO, EMP_NAME, SAL,
        case
            when (sum(SCORE) / 2) >= 96 then 'S'
            when (sum(SCORE) / 2) >= 90 then 'A'
            when (sum(SCORE) / 2) >= 80 then 'B'
            else 'C'
        end as GRADE
    from HR_EMPLOYEES
    join HR_GRADE
        using(EMP_NO)
    group by EMP_NO
) as t
order by EMP_NO
