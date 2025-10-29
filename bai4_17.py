def tong_uoc(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong

n = int(input("Nhập n: "))
print(f"Các số nhỏ hơn {n} có tổng các ước số lớn hơn chính nó là:")

for x in range(1, n):
    if tong_uoc(x) > x:
        print(x, end=" ")
