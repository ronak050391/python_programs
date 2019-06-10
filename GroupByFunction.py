# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)
# Explanation
#
# First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
#
# Also, note the single space within each compression and between the compressions.

import itertools
data=input()
groups = []
uniquekeys = []
#data = sorted(data, key=int)
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

output=""
for i in range(0,len(groups)):
    output = output + "({}, {}) ".format(len(groups[i]),int(uniquekeys[i]))
print(output)
