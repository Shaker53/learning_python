def finding(arg, namespace):
    if arg in dict[namespace][0]:
        return namespace
    else:
        for key, value in dict.items():
            if namespace in value[1]:
                return finding(arg, key)
        return None





dict = {'global': [[],[]] }
n = int(input())
for i in range(n):
    command, namespace, arg = input().split()
    if command == 'create':
        (dict[arg][1]).append(namespace)
        dict[namespace] = [[],[]]
    elif command == 'add':
        (dict[namespace][0]).append(arg)
    elif command == 'get':
        ans = finding(arg, namespace)
        print(ans)
    elif command == 'kek':
        print(dict)

