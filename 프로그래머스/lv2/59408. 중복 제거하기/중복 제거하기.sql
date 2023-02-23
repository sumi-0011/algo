-- 코드를 입력하세요
SELECT count(a.name)
from (
select name 
from ANIMAL_INS
group by name
) as a
where a.NAME is not null