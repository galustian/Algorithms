import sys

nums = ".0123456789"
operators = "+-*/^%"

def valid_str(equ):
    valid_chars = nums + operators + '()'
    for c in equ:
        if c not in valid_chars: return False
    return True

def normalize_preceding_plus_minus_operators(equ):
    double_op = {'--': '', '++': '', '+-': '-', '-+': '-'}
    for dop in double_op:
        while dop in equ: equ = equ.replace(dop, double_op[dop])
    i = 0
    while i < len(equ):
        if equ[i] in '+-' and (i == 0 or equ[i-1] in operators + '('):
            if equ[i+1] == '(':
                idx = get_idx_of_closing_parentheses(equ, i+1)
            else:
                idx = get_idx_of_last_digit(equ, i+1)
            
            equ = equ[:i] + '(0' + equ[i:idx+1] + ')' + equ[idx+1:]
        i += 1
    return equ

def get_idx_of_last_digit(equ, first_digit_i):
    j = first_digit_i
    while j < len(equ) and equ[j] in nums: 
        j += 1
    return j-1

def get_idx_of_closing_parentheses(equ, first_parentheses_i):
    j = first_parentheses_i + 1
    count_n_closing_parentheses = 1
    while j < len(equ):
        if equ[j] == '(': count_n_closing_parentheses += 1
        elif equ[j] == ')':
            count_n_closing_parentheses -= 1
            if count_n_closing_parentheses == 0: return j
        j += 1
    # missing closing parentheses: raise error
    raise ValueError

def evaluate_result(vals, ops):
    if len(vals) - 1 != len(ops): raise ValueError
    # ^ has hightest precedence
    while '^' in ops:
        idx = ops.index('^')
        vals[idx] = vals[idx] ** vals[idx+1]
        del vals[idx+1]; del ops[idx]
    # *, /, % have same precedence, after ^
    i = 0
    while i < len(ops):
        if ops[i] in '+-':
            i += 1
            continue
        if ops[i] == '*':
            vals[i] = vals[i] * vals[i+1]
            del vals[i+1]; del ops[i]
        elif ops[i] == '/':
            if vals[i+1] == 0: raise ValueError
            vals[i] = vals[i] / vals[i+1]
            del vals[i+1]; del ops[i]
        elif ops[i] == '%':
            vals[i] = vals[i] % vals[i+1]
            del vals[i+1]; del ops[i]
    # +, - have same, lowest precedence
    while len(ops) != 0:
        if ops[0] == '+':
            vals[0] = vals[0] + vals[1]
            del vals[1]; del ops[0]
        else:
            vals[0] = vals[0] - vals[1]
            del vals[1]; del ops[0]

    return vals[0]

def calculate(equ):
    global nums, operators
    curr_vals, curr_ops = [], []
    
    i = 0
    while i < len(equ):
        if equ[i] == ')': raise ValueError # closing parentheses without opening
        if equ[i] in nums:            
            j = get_idx_of_last_digit(equ, i)
            num_str = equ[i:j+1]
            curr_vals.append(float(num_str))
            i = j+1
            continue
        if equ[i] in operators:
            curr_ops.append(equ[i])
            i += 1
        elif equ[i] == '(':
            c_i = get_idx_of_closing_parentheses(equ, i)
            parentheses_result = calculate(equ[i+1:c_i])
            curr_vals.append(parentheses_result)
            i = c_i+1

    return evaluate_result(curr_vals, curr_ops)

if __name__ == '__main__':
    equ = normalize_preceding_plus_minus_operators(sys.argv[1].replace(' ', '').replace(',', '.'))
    if not valid_str(equ): raise ValueError
    print(calculate(equ))
