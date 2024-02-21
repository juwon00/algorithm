select HOUR(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
group by HOUR(DATETIME)
having HOUR >= 9 and HOUR < 20
order by HOUR