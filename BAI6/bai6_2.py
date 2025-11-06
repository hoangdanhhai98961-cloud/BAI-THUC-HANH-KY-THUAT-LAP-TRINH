class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dientich(self):
        return self.chieu_dai * self.chieu_rong
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))

hcn = Hinhchunhat(dai, rong)
print(f"Diện tích hình chữ nhật là: {hcn.dientich():.2f}")
