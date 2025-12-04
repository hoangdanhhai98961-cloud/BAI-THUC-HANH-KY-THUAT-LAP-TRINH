import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu chi tiết của học sinh
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print("Original array:")
print(students)

# Sắp xếp theo chiều cao
sorted_students = np.sort(students, order='height')
print("\nSorted by height:")
print(sorted_students)
