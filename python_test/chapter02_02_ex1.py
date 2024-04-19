#Print 사용법
#파이썬 3가지 Print Formatting
#자주 나오는 질문

"""
참고 : Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : Null 문자
...
"""

x = 50
y = 100
text = 308276567
n = 'Lee'

#출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n,text,(x+y))
print(ex1)

ex2 = 'n={}, s={}, sum={}'.format(n,text,(x+y))
print(ex2)

ex3 = 'n = {n}, s = {s}, sum={sum}'.format(n=n,s=text,sum=x+y)
print(ex3)

ex4 = f'n={n}. s={text}, sum={x+y}'
print(ex4)

#구분기호
m = 100000000

print(f'm : {m:,}')
print()
print()

#정렬
# ^ 가운데 정렬, < : 왼쪽, > : 오른쪽

t=20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")


print()
print()

print(f"t center : {t:-^10}")
print(f"t center : {t:#^10}")
print(f"t left : {t:#<10}")

