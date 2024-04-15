number = 10
print(type(number))

print(id(10)) # id() -> 주소값 출력
print(id(number)) # 리터럴값(10) 참조하는 변수 -> 주소같음

number += 1
print(id(number))
print(id(11))

number -= 1
print(id(number))

print(type("test")) # str

print(type([])) # list
print(type(())) # tuple
print(type({})) # dictionary

print([1,2,3,4])
print((1,2,3,4))
print({"id": 1, "name": "박화목"})

list1 = [1,2,3,4]
tp = (5,6,7,8)
dict1 = {"id": 1, "name": "박화목"}

print(list1[0])
print(tp[0])
print(dict1["id"])

list2 = list(tp)
print(list2)
print(list(dict1))
print(dict1.keys())
print(dict1.values())
print(list(dict1.items())[0])

print(True)
print(False)