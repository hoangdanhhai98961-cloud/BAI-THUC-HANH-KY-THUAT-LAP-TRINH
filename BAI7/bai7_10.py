filename = "vanban.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    import re
    words = re.findall(r"\b\w+\b", text)

    if not words:
        print("Tệp không chứa từ nào.")
    else:
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]

        print(f"Các từ dài nhất (độ dài {max_length}):")
        for w in set(longest_words):
            print(w)
except FileNotFoundError:
    print(f"Tệp '{filename}' không tồn tại.")
