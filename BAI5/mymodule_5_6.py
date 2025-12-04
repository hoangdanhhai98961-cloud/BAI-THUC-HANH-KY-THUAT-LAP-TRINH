
def sort_list(lst):
    """Hàm sắp xếp danh sách theo thứ tự tăng dần"""
    return sorted(lst)

def find_max(lst):
    """Hàm tìm phần tử lớn nhất trong danh sách"""
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
