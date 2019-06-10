# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

N = int(input())
output_lst = []
for i in range(0, N):
    lst_input=[]
    input_cmnd = input()
    if input_cmnd.startswith("insert") == True:
        lst_input = input_cmnd.split()
        output_lst.insert(int(lst_input[1]), int(lst_input[2]))
    elif input_cmnd.startswith("print") == True:
        print(output_lst)
    elif input_cmnd.startswith("append") == True:
        lst_input = input_cmnd.split()
        output_lst.append(int(lst_input[1]))
    elif input_cmnd.startswith("pop") == True:
        output_lst.pop()
    elif input_cmnd.startswith("sort") == True:
        output_lst.sort()
    elif input_cmnd.startswith("reverse") == True:
        output_lst.reverse()
    elif input_cmnd.startswith("remove")==True:
        lst_input = input_cmnd.split()
        output_lst.remove(int(lst_input[1]))