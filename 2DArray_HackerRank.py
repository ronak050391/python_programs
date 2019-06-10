#30Days of Code: Day 11
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


sum_arr=[]

for i in range(0,4):
    for j in range(0,4):
        new_arr = []
        for k in range(j,j+3):
            new_arr.append(arr[i][k])
            new_arr.append(arr[i+2][k])
        new_arr.append(arr[i+1][j+1])
        sumarr = 0
        for l in new_arr:
            sumarr = sumarr + l
        sum_arr.append(sumarr)

print(max(sum_arr))