class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Tách chuỗi thành danh sách từ, đảo ngược danh sách, rồi nối lại
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
input_text = 'hello .py'
reverser = StringReverser(input_text)
output_text = reverser.reverse_words()
print(output_text)
