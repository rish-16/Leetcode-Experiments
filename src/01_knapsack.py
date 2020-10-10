import math
import pandas as pd

weights = [1, 2, 3]
values = [6, 10, 12]
maxW = 5

def knapsack(values, weights, maxW):
    n_items = len(values)

    mat = [[0 for i in range(maxW + 1)] for j in range(n_items + 1)]

    for item in range(1, n_items+1):
        for cap in range(1, maxW+1):
            max_val_without_item = mat[item - 1][cap]
            max_val_with_item = 0

            cur_weight = weights[item - 1]
            if (cap >= cur_weight):
                max_val_with_item = values[item - 1]

                remaining_weight = cap - cur_weight
                max_val_with_item += mat[item - 1][remaining_weight]

            mat[item][cap] = max(max_val_with_item, max_val_without_item)

    return mat[n_items][maxW], pd.DataFrame(mat, columns=list(range(maxW+1)))

res, mat = knapsack(values, weights, maxW)
print (res)
print (mat)