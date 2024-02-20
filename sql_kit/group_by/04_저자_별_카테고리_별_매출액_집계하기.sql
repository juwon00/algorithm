select AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(price * sales) as TOTAL_SALES
from BOOK
join AUTHOR
    using (AUTHOR_ID)
join BOOK_SALES
    using (BOOK_ID)
where SALES_DATE like "2022-01%"
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID asc, CATEGORY desc