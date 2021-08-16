age  = 25
age2 = 14


# while age < 20 :
#     age += 1
#     print (age)



#ninja youtube
# WHILE LOOP STATEMENT
# age = 25
num = 0

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    num += 1
    if num > 10:
        break
else:
    print('outside of condition') #doesn't work when using break