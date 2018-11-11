def idx_perms(char, string_list):
    new_perms_list = []
    for string in string_list:
        for i in range(len(string)+1):
            new_perms_list.append(string[:i] + char + string[i:])
    return new_perms_list


def get_all_perms(string):
    if len(string) == 1: return [string]
    return idx_perms(string[0], get_all_perms(string[1:]))


def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)


def exclude_substrings_in_permutations(permutations, substring_list):
    filtered_perms = []
    for str_perm in permutations:
        add = True
        for substr in substring_list:
            if substr in str_perm:
                add = False
                break
        if add: filtered_perms.append(str_perm)
    return filtered_perms

# you can compute this in constant time with the inclusion-exclusion principle.
# this was just to check if my homework was indeed correct :)
if __name__ == '__main__':
    string = 'abcdefgh'
    string_permutations = get_all_perms(string)
    
    print("All, permutations:", len(string_permutations), "=", factorial(len(string)))

    filtered_string_perms = exclude_substrings_in_permutations(string_permutations, ['acg', 'cgbe'])

    print("Filtered permutations:", len(filtered_string_perms))

