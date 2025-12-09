import turtle
import random

# Danh sách màu
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Khởi tạo turtle
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)  # Tăng tốc vẽ

# Vẽ 10 hình tròn nhiều màu
for i in range(10):
    color = random.choice(colors)  # Chọn màu ngẫu nhiên từ danh sách
    painter.color(color)
    painter.circle(100)  # Vẽ hình tròn bán kính 100
    painter.right(30)    # Quay 30 độ
    painter.left(60)     # Quay lại 60 độ
    painter.setposition(0, 0)  # Quay về gốc

# Kết thúc
turtle.done()
