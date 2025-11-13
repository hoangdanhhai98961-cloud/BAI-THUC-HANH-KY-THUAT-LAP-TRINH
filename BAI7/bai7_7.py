filename = "vanban.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        count = sum(1 for line in file)

    print(f"Số dòng trong tệp '{filename}' là: {count}")

except FileNotFoundError:
    print(f"Tệp '{filename}' không tồn tại.")
