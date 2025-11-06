class RomanConverter:
    def __init__(self):
        # Bảng tra cứu giá trị các chữ số La Mã
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in reversed(s.upper()):
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
converter = RomanConverter()
roman_num = input("Nhập số La Mã: ")
integer_num = converter.roman_to_int(roman_num)
print(f"Số nguyên tương ứng: {integer_num}")
