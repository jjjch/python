import sys
import time
from itertools import permutations 

start_time = time.time()

n = '6' if not sys.argv[1:] else sys.argv[1]
n = int(n)
print("n=",n);
allperm = permutations(range(1, n+1))

sizeOfPermutation = 0
countOfCorrect = {}
for oneperm in allperm:
    sizeOfPermutation = sizeOfPermutation + 1
    numberOfCorrect = 0
    for idx in range(1,n+1):
        if idx == oneperm[idx-1]:
            numberOfCorrect = numberOfCorrect + 1
    if numberOfCorrect not in countOfCorrect.keys():
        countOfCorrect[numberOfCorrect] = 1
    else:
        countOfCorrect[numberOfCorrect] = countOfCorrect[numberOfCorrect] + 1

print("sizeOfPermutation=",sizeOfPermutation);
for numberOfCorrect, count in countOfCorrect.items():
    print("numberOfCorrect=",numberOfCorrect,"; count=",count,"; %=",100*count/sizeOfPermutation);

print("--- the program took %s seconds to run.---" % (time.time() - start_time))
