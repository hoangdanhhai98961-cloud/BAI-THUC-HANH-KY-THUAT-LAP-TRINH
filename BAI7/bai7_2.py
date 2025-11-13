def file_statistics(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()  # Đọc toàn bộ nội dung

        # Số ký tự
        num_characters = len(content)

        # Số từ (tách bằng khoảng trắng)
        words = content.split()
        num_words = len(words)

        # Số dòng
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        num_lines = len(lines)

        # In kết quả
        print(f"Thống kê file '{filename}':")
        print(f"Số ký tự: {num_characters}")
        print(f"Số từ: {num_words}")
        print(f"Số dòng: {num_lines}")

    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")

# Main
if __name__ == "__main__":
    filename = "input.txt"  # Đặt tên file muốn đọc
    file_statistics(filename)
