def finding(son_maybe_in, parent_maybe_in):
    # print(son_maybe_in, 'in', parent_maybe_in, '?' )
    if son_maybe_in in dict[parent_maybe_in]:
        return True
    else:
        k = 0
        next_step = []
        for key, value in dict.items():
            if son_maybe_in in value:
                k += 1
                next_step.append(key)
                # print(k)
                # print(next_step)
        if k == 1:
            return finding(*next_step, parent_maybe_in)
        elif k == 0:
            return False
        else:
            # print(next_step)
            for step in next_step:
                if finding(step, parent_maybe_in):
                    return True
            return False





dict = {}
n = int(input())
for i in range(n):
    inf = input().split(' : ')
    if len(inf) == 1:
        if inf[0] not in dict:
            dict[inf[0]] = []
    else:
        class_ = inf[0]
        if class_ not in dict:
            dict[class_] = []
        parents = inf[1].split(' ')
        for parent in parents:
            if parent not in dict:
                dict[parent] = []
            (dict[parent]).append(class_)
# print(dict)
q = int(input())
for i in range(q):
    question = input().split(' ')
    parent_maybe = question[0]
    son_maybe = question[1]
    if parent_maybe == son_maybe:
        print('Yes')
    else:
        ans = finding(son_maybe, parent_maybe)
        if ans == True:
            print('Yes')
        else:
            print('No')

