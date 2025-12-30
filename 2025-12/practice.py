
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

aa = set()
aa.update([1,2,3,4])
# aa.remove(5)
aa.discard(5)
print(type(aa.discard(5)))
print(aa)
