# 1. 변수

# 1.1 - 변수저장과 출력 실습
name = "김동균"
age = 18
fav_num = 25
print(f"{name} - {age} - {fav_num}")

# 1.2 - 파이썬의 다중할당 실습
first = "A"
second = "B"
first,second = second,first
print(f"{first} - {second}")

# 1.3 - 파이썬의 복합 연산자 실습
balance = 10000
# new_balance = (balance - 3000 ) * 2
# print(new_balance)
balance -= 3000
balance *= 2
print(f"{balance}")

# 1.4 변수 오류 수정
# 2nd_place = "은메달" - 변수의 첫번째는 숫자로 지정할수없다.
second_place = "은메달"
# user name  = "홍길동" - 변수 중간의 띄어쓰기는 불가하다
user_name = "홍길동"
# class = "1학년" 파이썬에서 규정하는 예약어는 변수로 불가하다
my_class ="1학년"

# 2. 자료형

# 2.1 자료형 type 확인해보기
print(type(42))
# <class 'int'> int형, 정수형 객체의 클래스 - 파이썬에 정의된 데이터는 단순한 데이터 값이 아니라 객체형으로 담긴다
print(type(3.14)) #<class 'float'>
print(type("hello")) #<class 'str'>
print(type(True)) #<class 'bool'>
print(type(None)) #<class 'NoneType'> none은 nonetype클래스로 정의된 유일 객체(싱글톤)이다.

# 2.2
num1 = int(input("숫자1을 입력하세요"))
num2 = int(input("숫자2를 입력하세요"))
new_num = num1 + num2
print(f"{new_num} - 두 숫자의 합")

# 2.3
name = input("이름은?")
age = int(input("나이는?"))
height = int(input("키는?"))
print(f"{name} - 현재 나이 :{age} / 내년 나이 :{age+1},  키 :{height}")

# 2.4
num1 = int(input("숫자1을 입력하세요"))
num2 = int(input("숫자2를 입력하세요"))
cal = input("계산할 기호를 입력하세요")

if cal == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif cal == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif cal == "*":
    print(f"{num1} - {num2} = {num1 * num2}")
elif cal == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif cal == "//":
    print(f"{num1} // {num2} = {num1 // num2}")
elif cal == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("지원하지 않는 연산 기호입니다.")

