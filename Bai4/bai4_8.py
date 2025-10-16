# Nhập dãy từ, các từ cách nhau bằng space hoặc tab
line = input("Nhập các từ: ")

# Tách chuỗi thành danh sách các từ
words = line.split()

if not words:
    print("Bạn chưa nhập từ nào.")
else:
    # Tìm độ dài lớn nhất
    max_len = max(len(word) for word in words)
    
    # Lấy tất cả từ có độ dài bằng max_len
    longest_words = [word for word in words if len(word) == max_len]
    
    # In ra các từ dài nhất
    print("Từ dài nhất và các từ cùng độ dài:")
    print(" ".join(longest_words))
