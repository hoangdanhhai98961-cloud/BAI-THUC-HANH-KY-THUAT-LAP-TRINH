# Nhập chuỗi đầu vào
data = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")

# Tách thành danh sách
nums = data.split(',')

# Lọc ra các số chia hết cho 5
ket_qua = []
for n in nums:
    thap_phan = int(n, 2)  # chuyển nhị phân sang thập phân
    if thap_phan % 5 == 0:
        ket_qua.append(n)

# In kết quả
print(",".join(ket_qua))
