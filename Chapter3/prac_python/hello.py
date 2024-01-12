print('Hello, jungle')

a = 3        # 3을 a에 넣는다
print(a)
b = a        # b에 3을 넣는다.
print(b)
a = 5        # a에 5라는 새로운 값을 넣는다.
print(a, b)  # 5 3

a = 7
b = 2

print(a+b)   # 9 
print(a-b)   # 5
print(a*b)   # 14
print(a/b)   # 3.5
print(a//b)  # 3 (몫)
print(a%b)   # 1 (나머지)
print(a**b)  # 49 (거듭제곱)

print(a+3*b) # 13 (여러 연산을 한 줄에 할 경우 사칙연산의 순서를 따른다.)

def f(x) : 
    return 2*x+3
print(f(2))

def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

result = sum_all(1,2,3) + mul(10,10)

# result라는 변수의 값은?
print(result)

#아래부터는 조건문
#1. if / else
def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(oddeven(20)) # True

#else if는 elif로 줄여씁니다.
def is_adult(age):
    if age > 20:
        print('성인입니다') 
    elif age >= 13:
        print('청소년이에요')  
    else:
        print('어린이네요!')

is_adult(30)  # 성인입니다

#반복문
fruits = ['사과','배','감','귤']

for fruit in fruits:
    print(fruit)
# 사과
# 배
# 감
# 귤 
"""
자바스크립트에서 이를 표현하면
fruits = ['사과','배','감','귤']

for i in range(len(fruits)):  # i 가 0, 1, 2, 3일 때 
    fruit = fruits[i]	
    print(fruit)

# 사과
# 배
# 감
# 귤
"""