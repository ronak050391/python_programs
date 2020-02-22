def second_largest(l):
    uniq_num = set()
    sorted_lst = []
    for i in l:
        if i not in uniq_num:
            sorted_lst.append(i)
            uniq_num.add(i)
    sorted_lst.sort()
    return sorted_lst[-2]

l=[]
size=int(input("Enter the size of list: "))
for i in range(1,size+1):
    l.append(int(input("Enter the value " + str(i) + ":")))
print("\nEntered list is: ",l)
print("Second Largest no in list is: ",second_largest(l))