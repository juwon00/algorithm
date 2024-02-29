select DEPT_ID, DEPT_NAME_EN, round(sum(SAL) / count(*), 0) as AVG_SAL
from HR_EMPLOYEES
join HR_DEPARTMENT
    using(DEPT_ID)
group by DEPT_ID
order by AVG_SAL desc