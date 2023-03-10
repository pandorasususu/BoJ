# -- 코드를 입력하세요
# SELECT
# A.FLAVOR AS FLAVOR
# FROM FIRST_HALF AS A, ICECREAM_INFO AS B
# WHERE A.FLAVOR = B.FLAVOR AND A.TOTAL_ORDER >= 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
# ORDER BY A.FLAVOR

-- 코드를 입력하세요
SELECT
A.FLAVOR 
FROM FIRST_HALF AS A JOIN ICECREAM_INFO AS B 
ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER >= 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY A.FLAVOR