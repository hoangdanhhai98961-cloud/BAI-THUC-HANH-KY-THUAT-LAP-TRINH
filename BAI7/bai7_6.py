filename = "vanban.txt"
n = int(input("Nhập số dòng cuối cần đọc: "))
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()
last_lines = lines[-n:]

print(f"\n{n} dòng cuối cùng trong tệp '{filename}':")
for line in last_lines:
    print(line.strip())
