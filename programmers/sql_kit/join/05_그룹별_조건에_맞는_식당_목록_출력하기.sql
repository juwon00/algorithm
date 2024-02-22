select MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from MEMBER_PROFILE
join REST_REVIEW
    using(MEMBER_ID)
where MEMBER_ID in (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    having count(*) = (
        select distinct count(*)
        from REST_REVIEW
        group by MEMBER_ID
        order by count(*) desc
        limit 1
    )
)
order by REVIEW_DATE asc, REVIEW_TEXT asc