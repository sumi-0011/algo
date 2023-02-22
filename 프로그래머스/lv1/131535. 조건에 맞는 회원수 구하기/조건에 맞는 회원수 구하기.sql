-- 코드를 입력하세요
SELECT count(USER_ID)
from USER_INFO
where JOINED like '2021%' 
and 20 <= AGE and age <= 29