import time
import memory_profiler as mem_profile # pip install memory_profiler



print('Memory (Before) : {}Mb'.format(mem_profile.memory_usage()))
def naturalNoList(n):
    result = []
    for i in range(1,n):
        result.append(i)
    return result

def naturalNoGen(n):
    for i in range(1,n):
        yield n

t1 = time.time()
#listNatural=naturalNoList(10000000)
listNatural=naturalNoGen(10000000)
t2 = time.time()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Total Time Takes By the Function is ', (t2-t1)*1000)


