
"""
질문 모음
1.
dict 자료 구조상 delete는 잘 쓰지 않으며
컨스트럭팅, 키매핑, dto-entitiy, entitiy-dto 등의 방식을 우선한다. 이 말의 의미가 무엇인지요?

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
dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dict.get("value1"))
print(dict["key3"])

#del dict["key3"]
print(dict)

for k in dict.keys():
    print(k)

for k,v in dict.items():
    print(k,v)

