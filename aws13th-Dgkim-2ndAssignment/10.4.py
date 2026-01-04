#1
"""
왜 위험한가? fstring문자열을 직접 사용하면, 사용자가 직접 값을 입력하고, 입력값에 sql구문같은것을 넣어 버릴수 있다.
변수값에 특정 sql문구를 집어넣으면 sql의 데이터 베이스가 손상될수 있다.

Placeholder를 사용하여 코드 수정하기

name = input("이름: ")
age = input("나이: ")

sql = "INSERT INTO students (name, age) VALUES (?, ?)"
cursor.execute(sql, (name, age))

"""