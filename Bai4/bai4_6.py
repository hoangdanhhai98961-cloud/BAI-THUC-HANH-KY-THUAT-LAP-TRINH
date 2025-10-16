# Nhập tên đầy đủ
full_name = input("Nhập họ và tên: ").strip()

# Tách thành danh sách các từ
parts = full_name.split()

# Giả thiết chỉ có 2 phần: họ và tên
if len(parts) == 2:
    ho = parts[0]
    ten = parts[1]
    print(f"Họ: {ho}")
    print(f"Tên: {ten}")
else:
    print("Vui lòng nhập đúng định dạng: họ và tên, mỗi phần một âm.")
