from mymodule_5_5 import sort_list, find_max, find_min
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(num)
sorted_lst = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)
print("\nDanh sách đã sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
