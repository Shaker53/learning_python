def modify_list(l):
    l = lst
    k = 0
    for i in range(len(l)):
        if l[k] % 2 == 1:
            del l[k]
        elif l[k] % 2 == 0:
            l[k] = l[k] // 2
            k += 1







lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
