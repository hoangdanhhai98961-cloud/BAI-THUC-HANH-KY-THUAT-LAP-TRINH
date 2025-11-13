source_file = "vanban.txt"
destination_file = "sao_chep.txt" 
try:
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()
    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)
    print(f"Đã sao chép nội dung từ '{source_file}' sang '{destination_file}' thành công.")
except FileNotFoundError:
    print(f"Tệp nguồn '{source_file}' không tồn tại.")
