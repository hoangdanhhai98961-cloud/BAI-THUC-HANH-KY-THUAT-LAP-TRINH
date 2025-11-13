def read_n_lines(filename, n):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Duyệt từng dòng và in ra n dòng đầu
            for i in range(n):
                line = file.readline()
                if not line:  # Nếu file kết thúc trước n dòng
                    break
                print(line.strip())  # .strip() loại bỏ ký tự xuống dòng

    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Main
if __name__ == "__main__":
    filename = "input1.txt"
    n = int(input("Nhập số dòng muốn đọc: "))
    print(f"\n{n} dòng đầu tiên của file '{filename}':\n")
    read_n_lines(filename, n)
