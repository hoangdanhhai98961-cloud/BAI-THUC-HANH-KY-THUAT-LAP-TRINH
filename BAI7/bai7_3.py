n_tep = "duong_dan/input.txt"

# Mở tệp ở chế độ đọc ('r') và đọc toàn bộ nội dung
try:
    with open(input, 'r', encoding='utf-8') as tep:
        noi_dung = tep.read()
    print("Nội dung của tệp là:")
    print(noi_dung)
except FileNotFoundError:
    print(f"Tệp '{input}' không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
