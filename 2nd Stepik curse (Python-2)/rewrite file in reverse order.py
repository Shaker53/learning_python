with open("test_input.txt") as f, open("test_output.txt", "w") as w:
    x = f.read().splitlines()
    print(x)
    print(len(x))
    for i in range(len(x) -1, -1, -1):
        w.write(x[i] + '\n')
