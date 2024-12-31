#파이썬 변수

#기본선언
n = 700

#출력
print(n * 700)
print(type(n))

x = y = z = 700
print(x,y,z)

#선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var))


#Object References
#변수값 할당 상태
#1. 타입에 맞는 오브젝트생성
#2. 값 생성
#3. 콘솔 출력

#예1)
print(300)
print(int(300))

#예2)
# n -> 777
n = 777
print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

#id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

#object의 고유값
print(id(m), id(n))
print(id(m) == id(n))
print() 

#같은 오브젝트의 값을 참조함
m = 800
n = 800
z = 800
i = 800
#4개는 똑같은 인스턴스로 생성됨

#object의 고유값
print(id(m), id(n))
print(id(m) == id(n))
print() 

#다양한 변수 선언
#Camel Case : numberOfCollegeGraduates => Method
#Pascal Case : NumberOfCollegeGraduates => Class
#Snake Case : number_of_college_graduates => Variable

student_grade = 3

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3



# Python only has a few dozen reserved words:
# False , None , True , and , as , assert , async , await , break , class , continue ,
# def , del , elif , else , except , finally , for , from , global , if , 
# import , in , is , lambda , nonlocal , not , or , pass , raise , return , try , while , with , yield 


