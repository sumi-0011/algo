-- 코드를 입력하세요
SELECT *
from FOOD_PRODUCT
where price = (SELECT max(price) as price from food_product);