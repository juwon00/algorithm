select u.USER_ID, u.NICKNAME,
concat(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) as 전체주소,
concat(SUBSTRING(TLNO from 1 for 3), '-' ,SUBSTRING(TLNO from 4 for 4), '-' ,SUBSTRING(TLNO from 8 for 4)) as 전화번호
from USED_GOODS_BOARD as b
join USED_GOODS_USER as u
on b.WRITER_ID = u.USER_ID
group by u.USER_ID
having count(*) >= 3
order by u.USER_ID desc