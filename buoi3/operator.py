# Operators
# + - * /  // ** %
print(1 + 2) # cộng
print(1 - 2) # trừ
print(1 * 2) # nhân
print(3 / 2) # chia(float)
print(3 % 2) # chia lấy dư
print(3 // 2) # lấy số nguyên
print(5**2) # lũy thừa


# > < >= <= == !=
print(1 > 2) # false
print(1 < -1) # false
print(3.0 == 3) # true(khác kiểu dữ liệu nhưng mặt giá trị bằng nhau)
print('a' != 'a') # vì vẫn cùng giá trị


# and, or , not
print(True and True) # đúng và đúng ==)) đúng
print(True and False) # sai
print(False and False) # sai

print(True or True) # đúng hoặc đúng ==)) đúng
print(True or False) # đúng
print(False or False) # sai

print(not True) # không phỉa đúng -> Sai
print(not False) # không phải sai -> Đúng

print(1 and 2)

print(bool(0))
print(bool(1))

print(bool(0.0))

print(bool([]))


# định dạng chuỗi
age = 30
# age_as = str(age)
print("i am " + str(age))
print(f"i am {age}")
print("I am {}".format(age))
