chuoi = input("Nhập câu: ")

chu_cai = 0
chu_so = 0

for ch in chuoi:
    if ch.isalpha():      # kiểm tra ký tự là chữ cái (a-z, A-Z)
        chu_cai += 1
    elif ch.isdigit():    # kiểm tra ký tự là chữ số (0-9)
        chu_so += 1

print("Số chữ cái là:", chu_cai)
print("Số chữ số là:", chu_so)
