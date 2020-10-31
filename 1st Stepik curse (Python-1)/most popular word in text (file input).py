text = []
dict = {}
with open("/home/ilya/Desktop/test_input.txt") as inf:
    for line in inf:
        text += line.strip().lower().split()
print(text)
for k in text:
    if k not in dict:
        dict[k] = 1
    else:
        dict[k] += 1
print(dict)
final_value = '0'
final_key =''
for key, value in dict.items():
    if str(value) > final_value:
        final_value = str(value)
        final_key = key
    elif str(value) == final_value:
        final_value += ' ' + str(value)
        final_key += ' ' + key
final_key, final_value = final_key.split(), final_value.split()
min_key = final_key[0]
for j in final_key:
    if j < min_key:
        min_key = j
print(final_key)
print(final_key[0], final_value[0])