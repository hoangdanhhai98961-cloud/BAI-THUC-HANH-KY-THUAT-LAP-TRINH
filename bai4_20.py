n = int(input("Nhập n: "))

tam_giac = []

for i in range(n):
    # mỗi dòng bắt đầu bằng [1]
    hang = [1]
    if i > 0:
        for j in range(1, i):
            hang.append(tam_giac[i-1][j-1] + tam_giac[i-1][j])
        hang.append(1)
    tam_giac.append(hang)

# In tam giác Pascal
for hang in tam_giac:
    print(*hang)
