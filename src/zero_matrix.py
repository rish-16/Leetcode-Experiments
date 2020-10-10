import copy

def zero(mat):
    new = []

    for i in range(len(mat)):
        cur_row = mat[i]
        if any(cur_row) == True:
            new_row = copy.deepcopy(cur_row)
            


table = [[True, False, False], [False, False, False], [False, False, False]]