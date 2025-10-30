# Nhập danh sách số
chuoi = input("Nhập các số, cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách các chuỗi con, rồi chuyển sang số nguyên
ds = [int(x) for x in chuoi.split(',')]

# Lọc các số lẻ
so_le = [str(x) for x in ds if x % 2 != 0]

# In ra các số lẻ, ngăn cách bằng dấu phẩy
print(",".join(so_le))
