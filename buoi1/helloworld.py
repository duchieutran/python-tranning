print("Hello world !")
print(1, 2, 3, 4, 5) # ngăn cách với nhau bởi khoảng trắng

# Vấn đề đặt ra là : không muốn ngăn cách nhau bởi space nữa, mà là dấu phẩy hay 1 kí tự
print("Ngăn cách bởi dấu phẩy (dùng set=''): ")
print(1, 2, 3, 4, 5, sep=',') # ngăn cách với nhau bởi dấu phẩy

# dùng 2 print nhưng vẫn in trên cùng 1 dòng
print(1, 2, 3, 4, 5, end=" ") # \n newline
print(6)


