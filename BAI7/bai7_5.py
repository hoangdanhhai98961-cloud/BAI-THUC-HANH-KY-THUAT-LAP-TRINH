
filename = "vanban.txt"
text = input("Nhập văn bản cần nối vào tệp: ")
with open(filename, "a", encoding="utf-8") as file:
    file.write(text + "\n") 

print("\nNội dung hiện có trong tệp:")
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
