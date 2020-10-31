def finding(question_in, parent_maybe_in):
    if question_in in dict[parent_maybe_in]:
        return True
    else:
        k = 0
        next_step = []
        for key, value in dict.items():
            if question_in in value:
                k += 1
                next_step.append(key)
        if k == 1:
            return finding(*next_step, parent_maybe_in)
        elif k == 0:
            return False
        else:
            for step in next_step:
                if finding(step, parent_maybe_in):
                    return True
            return False





dict = {}
question_list = []
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
q = int(input())
for i in range(q):
    question = input()
    for parent_maybe in question_list:
        ans = finding(question, parent_maybe)
        if ans == True:
            print(question)
            break
    question_list.append(question)
