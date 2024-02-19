select BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") as "PUBLISHED_DATE"
from BOOK
where category = '인문' and PUBLISHED_DATE like "2021%"
order by PUBLISHED_DATE asc