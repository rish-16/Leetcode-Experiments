def median(xs, ys):
    xs.extend(ys)
    xs = sorted(xs)
    print (xs)

    if len(xs) % 2 != 0: # odd
        mid = (len(xs) + 1) / 2
        return xs[mid]
    else: # even
        mid1 = (len(xs)/2)
        mid2 = (len(xs) / 2) - 1
        res = float(xs[mid1] + xs[mid2])
        return res / 2

print (median([1, 3, 5], [2, 4, 6]))