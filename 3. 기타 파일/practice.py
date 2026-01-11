
"""
질문 모음
1.
dict 자료 구조상 delete를 바로 쓰지 않으며,
컨스트럭팅, 키매핑, dto-entitiy, entitiy-dto 등의 방식을 우선한다. 이 말의 의미가 무엇 인지요?

"""

# count += 1
# print(count)
#
# pi = 3.14159
# print(f"원주율 : {pi : .1f}")
#
# var = ["a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b"]
# #var.remove("a")
# var2= var.pop()
# # print(var2)
#
# dict2 = {"key1":"value1", "key2":"value2", "key3":"value3"}
# print(dict.get("value1"))
# print(dict["key3"])

#del dict["key3"]
# print(dict)
#
# for k in dict.keys():
#     print(k)
#
# for k,v in dict.items():
#     print(k,v)
# #
# del dict2
# print(dict2)

# val = "     안녕     "
# val2 =val.strip()
# print(val2)
# val3 = val2.split("안")
# print(val3)
#
# email = 'eewwqq1@naver.com'
# user = email.split('@')
# print(user[0])
#
# tup = ()
# print(type(tup))

# tup = (1,"2",3)
# print(tup[-1])
# print(tup[1:-1])
# print(len(tup[1:-1]))
#
# text = "안녕하세요"
# print("안" in text)

# aa = set()
# dd = {1,2,3}
#
# print(type(aa))
# print(type(dd))

#
# aa = set()
# # aa.add("asasdad")
# # aa.add("eccmmas")
# # aa.add("csescsd")
# # aa.add("ooadsqu")
# print(aa)

# aa = set()
# aa.update([1,2,3,4])
# # aa.remove(5)
# aa.discard(5)
# print(type(aa.discard(5)))
# print(aa)

# 1 중복된 리스트의 중복을 제거하면서, list의 인덱싱을 유지하는방법
#
# set 강의에서 중복된 리스트를 set화 해서 중복을 제거후 다시 list화 하는 방식으로 리스트의 중복을 제거하는 예시를 보여주셨는데
# 예시와 다르게 리스트의 중복값만 제거하면서 인덱싱을 유지하는 여러 방법중
# (검색결과 :  dict.fromkeys(),sorted(),orderedDict,for문 4개가 유효하다고 나오기는 합니다만) 다른 방식이 있는지? 실무상 선호하는 방식은 무엇인지? 알고 싶습니다.
#

# 2. 파이썬에서 enum의 사용의 이유
#
# enum을 의미있는 상수 집합을 정의한 클래스 객체 라고 정의 하면, 실제 비즈니스 로직에서 상수변수를 선언하여 사용하는것과 어떠한 차이가 있는지요?
# enum으로 구분지어 반드시 써야만 하는 경우가 어떤것이 있는지요?

# 3. 실제 기능 개발을 위해 비즈니스 로직 코드을 작성하면서 ai검색을 진행할때 개발 철학 측면에서 :
#  3-1 : ai도구로 질문을 하면 코드에 대한 여러 예시를 세분화 해서 보여주는데, 실제 개발 트랜드에 맞춰
#
#
#
#  에초에 처음부터 질문 자체를 구체화 하여 세분화의 가능성을 없애버리고 완벽하게 원하는 방식의 코드만 얻는 방식이 좋은지
#  3-2 : 아니면 한개의 개발 로직을 달성하기 위한 검색결과가 다수일지 목적성에 맞는 방식을 찾아서 실제로 적용하고자 할때 어떠한 방식으로 생각을 해야하고,
#
# 적용을 해야하는지 궁금합니다.

my_list = ["영희","영희","영희","철수","철수","철수","선영","선영","선영","지수","지수","지수"]
my_list2 = list(set(my_list))
print(my_list2)

for i, l in enumerate(my_list2,start=1):
    print(i,l)


for i,n in my_list2, range(5):
    print(f"{num}: {i}")
    num = num + 1

num = 1
for i in my_list2:
    print(f"{num}: {i}")
    num = num + 1