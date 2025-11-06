class StringManipulator:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.text.upper())
s = StringManipulator()
s.get_String()
s.print_String()
