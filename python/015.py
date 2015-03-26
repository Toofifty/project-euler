from itertools import permutations
from time import clock
import sys

stime = clock()

grid_size = int(sys.argv[1])
    
#print str(grid_size)+"*"+str(grid_size),"moves:",len(set(permutations("rd"*grid_size)))

print (clock() - stime) * 1000,"ms"

def getPerms(list):
    if len(list) == 2:
        return [list[0], list[1]], [list[1], list[0]]
    outlist = []
    for i in getPerms(list[1:]):
        i.append(list[0])
        outlist.append(i)
    print outlist
    return outlist
    
print getPerms("abc")


# "ab" 2
# "ab" "ba" 2
# "abab" 4
# "abab" "abba" "aabb" "baba" "bbaa" "baab" 6 
# "aba"
# "aba" "aab" "baa"
# "ababab"
# "ababab" "aabbab" "aabbba" "aaabbb" "abbaba" "abbbaa" "abbaab" "abaabb"
# "aababb" "ababba" {...}

# "ababa"
# "ababa" "abbaa" "aaabb" "aabab" "aabba" "abaab"
# "babaa" "baaba" "bbaaa" "baaab"

# 1c > 1l
# 2c > 2l
# 3c > 3l
# 4c > 6l
# 5c > 10l
# 6c > 20l 