import mymodule_5_6
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = [int(input(f"Nhập phần tử thứ {i}: ")) for i in range(n)]
max_value = mymodule_5_6.find_max(lst)
sorted_lst = mymodule_5_6.sort_list(lst)
min_value = sorted_lst
pos_max = lst.index(max_value)
pos_min = lst.index(min_value)
print(f"Phần tử lớn nhất: {max_value}, tại vị trí: {pos_max}")
print(f"Phần tử nhỏ nhất: {min_value}, tại vị trí: {pos_min}")


