# 3-1 str활용하기

# split랑 인덱싱 방식
user_email = input("사용자 이메일을 입력하세요")
div = user_email.split("@")
user_name = div[0]
user_domain = div[1]
print(f"{user_name} - 유저이름, {user_domain} - 유저 도메인")

#언페킹 방식
name, domain = user_email.split("@")

# find 방식
at_index = user_email.find("@")
name = user_email[:at_index]
domain = user_email[at_index+1:]

print(f"{name} , {domain}")


# 3-2 len()으로 문자열 길이 파악

passward = input("비밀번호 입력: ")
if len(passward) >= 8:
    print("8자이상 유효")
else:
    print("8자 미만 ")

# 3-3
my_list = []
for num in range(1, 21):
    print(num)
    if num % 3 == 0:
        my_list.append(num)
print(my_list)

# 3-4 set의 활용
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]
#공통점만 뽑기
common = (set(chulsoo) & set(younghee))
print(common)
#공통점만 제거하고 나머지 뽑기
result = (set(chulsoo) ^ set(younghee))
print(result)

# 3.5
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88,
    "현주": 95
}
max_score = max(scores.values())

top_students = []
for key, value in scores.items():
    if value == max_score:
        top_students.append(key)

# top_students = [name for name, score in scores.items() if score == max_score]

print(top_students, max_score)


# for key, value in scores.items():
#
