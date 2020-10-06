def powerset(A):
    if A == []:
        yield []
    else:
        a = A[0]
        for tail in powerset(A[1:]):
            yield tail
            yield [a] + tail

arr = [1,2,3]
subs = powerset(arr)
print (list(subs))   