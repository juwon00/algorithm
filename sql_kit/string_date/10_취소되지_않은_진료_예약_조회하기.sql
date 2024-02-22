select APNT_NO, PT_NAME, PT_NO, a.MCDP_CD, DR_NAME, APNT_YMD
from APPOINTMENT a
join PATIENT
    using(PT_NO)
join DOCTOR d
on a.MDDR_ID = d.DR_ID
where APNT_YMD like "2022-04-13%" and APNT_CNCL_YN = "N" and a.MCDP_CD = "CS"
order by APNT_YMD