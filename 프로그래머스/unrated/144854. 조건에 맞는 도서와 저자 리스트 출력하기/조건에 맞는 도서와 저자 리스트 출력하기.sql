-- 코드를 입력하세요
SELECT b.BOOK_ID ,a.AUTHOR_NAME,	left(b.PUBLISHED_DATE,10) as PUBLISHED_DATE
from BOOK b inner join author a
on b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY ='경제'
order by b.PUBLISHED_DATE
 