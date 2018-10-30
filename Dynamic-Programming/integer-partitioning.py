from functools import lru_cache

def integer_partition(integers):
    sum_half = sum(integers) / 2
    if not sum_half.is_integer(): return None

    @lru_cache(maxsize=None)
    def recurse(i, sum_):
        if sum_ == 0: return []
        if i == len(integers) - 1:
            if integers[i] == sum_: return [integers[i]]
            return None
        
        r1 = recurse(i+1, sum_)
        r2 = recurse(i+1, sum_ - integers[i])

        if r1 != None: return r1
        if r2 != None: return [integers[i]] + r2
        return None

    return recurse(0, int(sum_half))


def subset_sum(integers, total_sum):
    @lru_cache(maxsize=None)
    def recurse(i, sum_):
        if sum_ == 0: return []
        if i == len(integers) - 1:
            if integers[i] == sum_: return [integers[i]]
            return None
        
        r1 = recurse(i+1, sum_)
        r2 = recurse(i+1, sum_ - integers[i])

        if r1 != None: return r1
        if r2 != None: return [integers[i]] + r2
        return None

    return recurse(0, total_sum)


if __name__ == '__main__':
    print(integer_partition([4, 9, 12, 7, 2, 6]))
    print(integer_partition([62, 83, 121, 281, 486, 734, 771, 854, 885, 1003]))
    print(subset_sum([62, 83, 121, 281, 486, 734, 771, 854, 885, 1003], 975))

