SELECT MEMBER_ID,MEMBER_NAME,GENDER,SUBSTR(DATE_OF_BIRTH,1,10) as DATE_OF_BIRTH
from MEMBER_PROFILE
where DATE_OF_BIRTH LIKE '%-03-%' 
and TLNO is not null 
and GENDER = 'W'
order by MEMBER_ID