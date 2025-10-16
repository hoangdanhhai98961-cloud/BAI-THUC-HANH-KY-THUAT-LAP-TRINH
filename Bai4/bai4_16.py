binary_input = input("Nhập các số nhị phân, cách nhau bằng dấu phẩy: ")

binary_numbers = [num.strip() for num in binary_input.split(',')]

print("Các số nhị phân bạn nhập là:")
for num in binary_numbers:
    print(num)
