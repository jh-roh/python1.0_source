#Chapter02-1
#파이썬 완전 기초
#Print 사용법


#기본출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')

print()
print("""Python Start!""")


#seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777','7777', sep='-')
print('python', 'google', sep='@')

print()

#end 옵션


print('Welcom to', end=' ')
print('IT News', end='')
print('Web Site')


#file 옵션
import sys

print('Learn Python', file=sys.stdout)


#format(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))


#%s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

#왼쪽을 +로 채우기
print('{:+>10}'.format('nice'))
print('{:^10}'.format('nice'))


#. 사용시 데이터를 자른다
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))


#%d 
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print(('%4d' % (42)))
print('{:4d}'.format(42))


#%f

print('%f' % (3.1434343434))
print('%5.18f' % (3.1434343434))
print('{:f}'.format(3.1434343434))
print('%06.2f' % (3.1434343434))
print('%06.7f' % (3.1434343434))

print('{:06.2f}'.format(3.1434343434))


