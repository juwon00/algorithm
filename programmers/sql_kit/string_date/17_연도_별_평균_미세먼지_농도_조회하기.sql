select YEAR(YM) as 'YEAR',
    round(sum(PM_VAL1) / count(*), 2) as 'PM10',
    round(sum(PM_VAL2) / count(*), 2) as 'PM2.5'
from AIR_POLLUTION
where LOCATION2 = '수원'
group by YEAR(YM)
order by YEAR