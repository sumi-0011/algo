-- 코드를 입력하세요
SELECT BOOK_ID,	left(PUBLISHED_DATE, 10)
from BOOK
where PUBLISHED_DATE like '2021%'
and CATEGORY ='인문'
order by PUBLISHED_DATE