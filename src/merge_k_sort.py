mat = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def merge_k_sort(mat):
    if len(mat) == 1:
        return mat[0]
    else:
        # at least 2
        first = mat[0]
        second = mat[1]
        res = merge(first, second)
        i = 2

        while i < len(mat):
            cur = mat[i]
            res = merge(res, cur)

            i += 1

        return res

print (merge_k_sort(mat))        
    

        