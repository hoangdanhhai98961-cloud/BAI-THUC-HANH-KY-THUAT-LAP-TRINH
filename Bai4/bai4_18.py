n = int(input("Nhập n: "))

# Tạo danh sách Fibonacci nhỏ hơn n
fibo = [0, 1]

# Sinh các số Fibonacci tiếp theo cho đến khi >= n thì dừng
while True:
    next_num = fibo[-1] + fibo[-2]
    if next_num >= n:
        break
    fibo.append(next_num)

print("Dãy Fibonacci nhỏ hơn", n, "là:")
print(fibo)
