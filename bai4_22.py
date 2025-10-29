ket_qua = []

for num in range(1000, 3001):  # bao gồm cả 3000
    s = str(num)
    if all(int(ch) % 2 == 0 for ch in s):  # kiểm tra tất cả các chữ số chẵn
        ket_qua.append(s)

print(",".join(ket_qua))
