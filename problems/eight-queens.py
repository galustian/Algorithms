import pickle

def check_row(row=0, row_exclude=None): # depth-first search
        if row == 7: return 8 - len(row_exclude[7])
        sum_ = 0
        for i in range(8):
            if i in row_exclude[row]: continue

            row_exclude_cpy = pickle.loads(pickle.dumps(row_exclude))
            for row_i in range(1, 8-row): # add row_i exclusions
                if i+row_i < 8: row_exclude_cpy[row+row_i].add(i+row_i)
                if i-row_i >= 0: row_exclude_cpy[row+row_i].add(i-row_i)
                row_exclude_cpy[row+row_i].add(i)

            sum_ += check_row(row+1, row_exclude_cpy)

        return sum_

if __name__ == '__main__':
    print(check_row(row=0, row_exclude=[set() for i in range(8)]))
