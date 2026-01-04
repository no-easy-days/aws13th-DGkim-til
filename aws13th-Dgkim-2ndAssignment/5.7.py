# #1
# def calculator(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '*':
#         return a * b
#     elif operator == '/':
#         if b == 0:
#             return "0으로 나눌 수 없습니다"
#         return a / b
#     else:
#         return "지원하지 않는 연산자입니다"
#
# print(calculator(10, 5, '+'))  # 15
# print(calculator(10, 5, '-'))  # 5
# print(calculator(10, 5, '*'))  # 50
# print(calculator(10, 5, '/'))  # 2.0
# print(calculator(10, 0, '/'))  # 0으로 나눌 수 없습니다
# print(calculator(10, 5, '%'))

# #2
# def print_report(name, scores):
#     average = sum(scores) / len(scores)
#     maximum = max(scores)
#     minimum = min(scores)
#
#     if average >= 90:
#         grade = "A"
#     elif average >= 80:
#         grade = "B"
#     elif average >= 70:
#         grade = "C"
#     elif average >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#
#     print(f"점수: {scores}")
#     print(f"평균: {average:.1f}점")
#     print(f"최고점: {maximum}점")
#     print(f"최저점: {minimum}점")
#     print(f"등급: {grade}")
#
# print_report("김철수", [85, 92, 78, 96, 88])

#3
def validate_password(password):
    if len(password) < 8:
        return (False, "8자 이상이어야 합니다")

    # has_digit = False
    # for char in password:
    #     if char.isdigit():
    #         has_digit = True
    #         break
    #
    # if not has_digit:
    #     return (False, "숫자를 포함해야 합니다")

    if not any(char.isdigit() for char in password):
        return False, "숫자를 포함해야 합니다"

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        return (False, "대문자를 포함해야 합니다")

    return (True, "유효한 비밀번호입니다")

print(validate_password("abc"))  # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))  # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))  # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))  # (True, "유효한 비밀번호입니다")