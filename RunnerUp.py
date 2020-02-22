n=int(input())
score=input()
scr_lst=score.split()
uniq_scr=set()
uniq_scr_lst=[]
# print(scr_lst)
for i in scr_lst:
    if int(i) not in uniq_scr:
        uniq_scr_lst.append(int(i))
        uniq_scr.add(int(i))
# print(uniq_scr)
uniq_scr_lst.sort()
# print(uniq_scr_lst)
print(uniq_scr_lst[-2])
