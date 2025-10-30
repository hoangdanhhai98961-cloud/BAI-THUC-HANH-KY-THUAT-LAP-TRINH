def sang_eratosthenes(n):
    """Trả về danh sách các số nguyên tố nhỏ hơn n"""
    prime = [True] * n
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):
                prime[j] = False

    return [i for i in range(n) if prime[i]]

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu
P = tuple(sang_eratosthenes(1_000_000))

print("Số lượng số nguyên tố nhỏ hơn 1 triệu là:", len(P))
print("10 số nguyên tố đầu tiên:", P[:10])
