danhsach = ["Xin chào", "Tôi là Hoàng Danh Hải", "Học Python rất thú vị"]

# Tên tệp cần ghi
filename = "vanban.txt"

# Mở tệp ở chế độ ghi ('w') — nếu tệp đã tồn tại, nội dung cũ sẽ bị ghi đè
with open(filename, "w", encoding="utf-8") as file:
    for item in danhsach:
        file.write(item + "\n")
print(f"Đã ghi {len(danhsach)} dòng vào tệp '{filename}'.")
