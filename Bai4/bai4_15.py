# Nhập chuỗi từ bàn phím
line = input("Nhập các từ tiếng Anh, cách nhau bởi dấu cách: ")

# Tách chuỗi thành danh sách các từ
words = line.split()

# Sắp xếp danh sách theo thứ tự từ điển (mặc định sắp xếp tăng dần)
words_sorted = sorted(words)

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
print(" ".join(words_sorted))
