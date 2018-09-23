import time
import pickle

SIZE = 8

def check_row(row=0, row_exclude=None): # depth-first search
        if row == SIZE-1: return SIZE - len(row_exclude[SIZE-1])
        sum_ = 0
        for i in range(SIZE):
            if i in row_exclude[row]: continue

            row_exclude_cpy = pickle.loads(pickle.dumps(row_exclude))
            for row_i in range(1, SIZE-row): # add row_i exclusions
                if i+row_i < SIZE: row_exclude_cpy[row+row_i].add(i+row_i)
                if i-row_i >= 0: row_exclude_cpy[row+row_i].add(i-row_i)
                row_exclude_cpy[row+row_i].add(i)

            sum_ += check_row(row+1, row_exclude_cpy)

        return sum_

if __name__ == '__main__':
    start = time.process_time()
    print(check_row(row=0, row_exclude=[set() for i in range(SIZE)]))
    print(time.process_time() - start)

