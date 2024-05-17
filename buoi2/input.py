# input trả về 1 kiểu chuỗi
full_name = input("Nhập vào tên của bạn : ")
print(full_name)
print(f"Kiểu dữ liệu của full_name là : {type(full_name)}")

# Nhập vào số nguyên ( nếu chỉ dùng input thì chỉ trả về kiểu chuỗi, int(input()) thì mới chuyển thành kiểu số nguyên )

number = int(input("Nhập số nguyên : "))
print(f"Số nguyên là : {number}")
print(f"Kiểu số nguyên là : {type(number)}")

#Nhập vào số thực
number_float = float(input("Nhập số thực : "))
print(f"Số thực là : {number_float}")

print(type("")) # kiểu str
print(type(.5))

print(dir(int))