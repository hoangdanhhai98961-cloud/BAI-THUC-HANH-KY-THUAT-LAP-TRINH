
# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi: ")

# Loại bỏ tất cả chữ số
s_no_digits = ''.join(c for c in s if not c.isdigit())

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", s_no_digits)
