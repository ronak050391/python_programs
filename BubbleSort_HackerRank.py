import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
new_lst = []
# Write Your Code Here
no_of_swap = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            new_value = a[i]
            a[i] = a[j]
            a[j] = new_value
            new_lst.append(a[j])
            new_lst.append(a[i])
            no_of_swap += 1
print("Array is sorted in {} swaps.".format(no_of_swap))
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])