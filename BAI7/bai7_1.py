def read_and_reverse_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        reversed_content = content[::-1]
        print("Nội dung đảo ngược của file:")
        print(reversed_content)

    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
if __name__ == "__main__":
    filename = "input.txt"
    read_and_reverse_file(filename)

