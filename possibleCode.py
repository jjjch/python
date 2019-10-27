import sys
import time
from itertools import permutations 

start_time = time.time()

n = '11' if not sys.argv[1:] else sys.argv[1]
n = int(n)
print("n=",n);
allperm = permutations(range(1, n+1))

sizeOfPermutation = 0
countMap = {}
for oneperm in allperm:
    sizeOfPermutation = sizeOfPermutation + 1

    numberOfInterest = 0
    numberOfConnect = 0
    for idx, v in enumerate(oneperm, start=1):
        if idx == 1:
            preV = v;
        else:
            if (preV==1 and v==2) or \
               (preV==1 and v==3) or \
               (preV==1 and v==4) or \
               (preV==2 and v==3) or \
               (preV==2 and v==4) or \
               (preV==3 and v==4) or \
               (preV==2 and v==1) or \
               (preV==3 and v==1) or \
               (preV==4 and v==1) or \
               (preV==3 and v==2) or \
               (preV==4 and v==2) or \
               (preV==4 and v==3) :
                numberOfConnect = numberOfConnect + 1
            else :
                numberOfConnect = 0
            if numberOfConnect > numberOfInterest:
                numberOfInterest = numberOfConnect;
            preV = v;

    if numberOfInterest not in countMap.keys():
        countMap[numberOfInterest] = 1
    else:
        countMap[numberOfInterest] = countMap[numberOfInterest] + 1

print("sizeOfPermutation=",sizeOfPermutation);
for numberOfInterest, count in countMap.items():
    print("numberOfInterest=",numberOfInterest,"; count=",count,"; %=",100*count/sizeOfPermutation);

print("--- the program took %s seconds to run.---" % (time.time() - start_time))
