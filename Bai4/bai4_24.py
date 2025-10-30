chuoi = input("Nhập câu: ")

chu_hoa = 0
chu_thuong = 0

for ch in chuoi:
    if ch.isupper():      # kiểm tra chữ hoa (A–Z)
        chu_hoa += 1
    elif ch.islower():    # kiểm tra chữ thường (a–z)
        chu_thuong += 1

print("Chữ hoa:", chu_hoa)
print("Chữ thường:", chu_thuong)
