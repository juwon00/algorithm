select ITEM_ID, ITEM_NAME, RARITY
from ITEM_TREE
join ITEM_INFO
    using(ITEM_ID)
where ITEM_ID not in (
    select distinct PARENT_ITEM_ID as ITEM_ID
    from ITEM_TREE
    where PARENT_ITEM_ID is not null
)
order by ITEM_ID desc