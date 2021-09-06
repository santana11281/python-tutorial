# num1 = 11
# num2 = num1
#
# print("before value is updated")
# print(f"num1 = {num1}")
# print(f"num2 = {num2}")
#
# num1 = 22
#
# print("after value is updated")
# print(f"num1 = {num1}")
# print(f"num2 = {num2}")

dic1 = {'value': 11}
dic2 = dic1

print("before value is updated")
print(f"dict1 is = {dic1}")
print(f"dict2 is = {dic2}")

dic1['value'] = 22

print("\nafter value is updated")
print(f"dict1 is = {dic1}")
print(f"dict2 is = {dic2}")