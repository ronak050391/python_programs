s = input("Enter the company name to be checked: ")
lst = []
for i in s:
    lst.append(i)
order_dict = {}
for i in range(len(lst)):
    if lst[i] not in lst[0:i]:
        occurence = lst.count(lst[i])
        if occurence not in order_dict.keys():
            order_dict[occurence] = [lst[i]]
        else:
            order_dict[occurence].append(lst[i])
            order_dict[occurence].sort()

s = 1
while s < 4:
    max_key = 0
    for i in order_dict.keys():
        if i > max_key:
            max_key = i
    if len(order_dict[max_key]) >= 3:
        if s == 1:
            for i in range(0, 3):
                print(order_dict[max_key][i], max_key)
            break
        else:
            for i in range(0, s):
                print(order_dict[max_key][i], max_key)
            break
    else:
        if s in [1,2]:
            for i in order_dict[max_key]:
                print(i, max_key)
            s += len(order_dict[max_key])
        else:
            for i in range(0, 3-s+1):
                print(order_dict[max_key][i], max_key)
            s += len(order_dict[max_key])
    del order_dict[max_key]
