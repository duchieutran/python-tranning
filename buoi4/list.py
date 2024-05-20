number = [1, 2, 1, 3, 4, 5]
print(type(number))
print(number)

print(number[-1]) # lấy từ cuối lên đầu

number.append(12) # thêm 1 giá trị vào cuối cùng của danh sách

number.remove(1) # xóa số 1 đầu tiên

last_value = number.pop() # xóa vị trí cuối cùng và trả ra giá trị
print(last_value)

number.extend([2, 2, 2, 2]) # thêm vào cuối của list ban đầu, [1, 2, 1, 3, 4, 5, 2, 2, 2, 2]

number[1] = 73 # thay đổi giá trị đầu thành 75

amount = number.count(2) # ví dụ : số 1 xuất hiện bao nhiêu lần
print(amount)

count = len(number) # số lượng phần tử trong list
print(count)

# number.clear() # chuyển về list rỗng

print(number)
