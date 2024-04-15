def add(num1, num2):
    return num1 + num2

result1 = add(10,20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4

# result2 = add(10,20,30,40)
# print(result2)

# r1, r2 = (1, 2)
# print(r1, r2)

# nums = [5,2,7,3,1]
# nums.sort()
# nums.reverse()
# print(nums)

# name = "박화목"
# print(name.index("목"))
# print(nums.index(3))
# print(name.find("모"))


user = {
    "username": "testuser",
    "password": "1234",
    "name": "박화목",
    "email": "elikese@gmail.com"
}

print(user)
user.update({"phone": "010-1234-1234"})
user["age"] = 33
print(user)