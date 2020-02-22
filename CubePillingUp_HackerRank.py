# Sample Input
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
# Sample Output#
# Yes
# No

# Explanation
# In the first test case, pick in this order: left -4 , right -4 , left -3 , right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.


for i in range(int(input())):
    size = int(input())
    values = list(map(int,input().split()))
    i = 0
    while i<len(values)-1 and values[i]>=values[i+1]:
        i +=1
    while i<len(values)-1 and values[i]<=values[i+1]:
        i +=1
    # print(max_size)
    if i == len(values)-1:
        print("Yes")
    else:
        print("No")