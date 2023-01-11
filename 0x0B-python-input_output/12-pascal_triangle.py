def pascal_triangle(n):
    pascal = []
    if n == 0:
        return pascal
    pascal.append([1])
    if n == 1:
        return pascal
    pascal.append([1, 1])
    if n == 2:
        return pascal
    prev_list = 1
    for iterations in range(n-2):
        new_list = [1]
        length = len(pascal[prev_list])
        inx = 0
        inx_add = 1
        for i in range(length - 1):
            new_val = pascal[prev_list][inx] + pascal[prev_list][inx_add]
            new_list.append(new_val)
            inx += 1
            inx_add += 1
        new_list.append(1)
        pascal.append(new_list)
        prev_list += 1
    return (pascal)
