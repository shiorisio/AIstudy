#-----
#Latest Update: 2016-07-12
#-----

def insertsort(List):
    for j in range(1,len(List)):
        key = List[j]
        i = j-1
        while i >= 0 and List[i] > key:
            List[i+1] = List[i]
            i = i - 1
        List[i+1] = key
    return List

def insertsortreverse(List):
    for j in range(1,len(List)):
        key = List[j]
        i = j-1
        while i >= 0 and List[i] < key:
            List[i+1] = List[i]
            i = i - 1
        List[i+1] = key
    return List

def linearsearch(List,v):
    for i in range(len(List)):
        if List[i] == v:
            return i
    return None

def add(A, B):
    n = len(A)
    C = [0] * (n+1)
    carry = 0
    for i in range(n-1,-1,-1):
        s = A[i] + B[i] + carry
        if s >= 2:
            s -= 2
            carry = 1
        else:
            carry = 0
        C[i+1] = s
    C[0] = carry
    return C

if __name__ == '__main__':
    import time
    start = time.time()
    print insertsort([31,41,59,26,41,58])
    print insertsortreverse([31,41,59,26,41,58])
    print add([1,1,1,0],[0,1,0,1])
    end = time.time() - start
    print "Execution time: " + str(end)
