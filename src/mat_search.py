mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

def mat_search(mat, target):
    i = 0
    while i < len(mat):
        if target > mat[i][-1]: # move to next row
            i += 1
        else: # target maybe in this row
            cur = mat[i]

            def binary_search(a):
                lo = 0
                hi = len(a) - 1

                while lo < hi:
                    mid = (hi + lo) // 2
                    pivot = a[mid]

                    if pivot == target:
                        return True
                    elif target > pivot:
                        lo = mid + 1
                    elif target < pivot:
                        hi = mid - 1

                return False

            return binary_search(cur)

    return False

print (mat_search(mat, 13))


