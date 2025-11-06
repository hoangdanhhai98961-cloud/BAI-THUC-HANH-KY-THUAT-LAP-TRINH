class Nguoi:
    def getGender(self):
        pass  

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
a = Nam()
b = Nu()

print(a.getGender())  # In: Nam
print(b.getGender())  # In: Nữ
