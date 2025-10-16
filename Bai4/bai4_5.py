# Nhập một dòng chứa các từ, các từ cách nhau bằng dấu space hoặc tab
line = input("Nhập các từ: ")

# Tách chuỗi thành danh sách các từ
words = line.split()

# Đảo ngược danh sách các từ
words_reversed = words[::-1]

# In ra các từ theo thứ tự ngược lại, cách nhau bằng dấu cách
print(" ".join(words_reversed))
