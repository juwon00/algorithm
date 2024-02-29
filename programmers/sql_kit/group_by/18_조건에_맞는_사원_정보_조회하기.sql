select sum(SCORE) as SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_DEPARTMENT
join HR_EMPLOYEES
    using(DEPT_ID)
join HR_GRADE
    using(EMP_NO)
group by EMP_NO
order by SCORE desc
limit 1