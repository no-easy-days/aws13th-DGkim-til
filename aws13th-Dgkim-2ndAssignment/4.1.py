#4-1

# scores = int(input("점수를 입력하세요"))
#
# if scores > 100 or scores < 0:
#     print("유효하지 않는 범위 0~100까지의 숫자만 입력하세요")
# elif scores >= 90:
#     print("a등급")
# elif scores >= 80:
#     print("b등급")
# elif scores >= 70:
#     print("c등급")
# elif scores >= 60:
#     print("d등급")
# else: print("f등급")

#4-2 구구단
# my_num = int(input("숫자를 입력하세여"))
# num =0
# for n in range(1, 10):
#     num = my_num * n
#     print(f"{my_num} * {n} = {num}")

# #4.3
# prime_list=[]
# for n in range(2, 101):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         prime_list.append(n)
# print(prime_list)

# #4.4
# import random
# random_num = random.randint(1, 100)
# print("1부터 100 사이의 숫자를 맞춰보세요!")
# attempt = 0
#
# while True:
#     attempt += 1
#     print(f"{attempt} 회입니다." )
#     guess = int(input("숫자를 입력하세요: "))
#
#     if guess < random_num:
#         print("너무 작습니다. 더 큰 숫자를 입력해보세요.")
#     elif guess > random_num:
#         print("너무 큽니다. 더 작은 숫자를 입력해보세요.")
#     else:
#         print("정답입니다! 🎉")
#         break
#     if attempt >4:
#         print(f"정답은 : {str(random_num)} 입니다.")



