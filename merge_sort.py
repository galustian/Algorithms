def merge_sort(arr):
    if len(arr) != 1:
        half = int(len(arr) / 2)
        sorted_1 = merge_sort(arr[:half])
        sorted_2 = merge_sort(arr[half:])
        
        len_1 = len(sorted_1)
        len_2 = len(sorted_2)
        i1 = 0
        i2 = 0
        merge_sorted = []
        
        while len(merge_sorted) != len_1 + len_2:
            while (i2 >= len_2 and i1 < len_1) or (i1 < len_1 and sorted_1[i1] <= sorted_2[i2]):
                merge_sorted.append(sorted_1[i1])
                i1 += 1
        
            while (i1 >= len_1 and i2 < len_2) or (i2 < len_2 and sorted_2[i2] <= sorted_1[i1]):
                merge_sorted.append(sorted_2[i2])
                i2 += 1

        return merge_sorted
        
    else:
        return arr
    
arr = [3, 3, 6, 0, -1, 1234, 44, -0.54, 45345455, 1, 10, -1, 42]
print(merge_sort(arr))