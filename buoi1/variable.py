#các kiểu dữ liệu : int, float, string, boolean, obj
# print , type,

x = 5 # biến có thể thay đổi trong suốt quá trình

print(type(x)) #  kiểu của giá trị, không phải của biến

x= 5.6 # thay đổi giá trị x

print(type(x)) # (float)

a = 5
b = 2
print(a + b) # phép cộng
print(a - b) # phép trừ
print(a / b) # phép chia, chia ra số lẻ
print(a // b) # chia ra số nguyên
print(a ** b) # phép lũy thừa
print(bool(1))

print(1 and 2)
print(0 and 2)

s = 'tran Duc Hieu'
print(s * 3) # in ra 3 lần chuỗi s
print(s.upper()) # in hoa toàn bộ chữ cái
print(s)
print(s.lower()) # in thường toàn bộ chữ cái đầu
print(s.title()) # in hoa từng chữ cái đầu
print(s.capitalize()) # in hoa chữ cái đầu tiên trong chuỗi
# format
age = 23
print(f"Tran duc hieu, tuoi = {23}") # f string là sử dụng nhiều từ python 3.6
print("Tran Duc Hieu, tuoi =", 23)
print("Tran Duc Hieu , tuoi = " + str(23))
print("Tran Duc Hieu, tuoi = {}" .format(23))