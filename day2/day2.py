import functools
INPUT = "input1.txt"

def main():
    mat = get_mat_from_file(INPUT)
    num_safe= count_safe(mat)
    print(f"num safe is: {num_safe}")
    
def count_safe(mat):
    num_safe = 0
    for row, row_num in zip(mat, range(len(mat))):
        is_safe = is_safe_row(row)
        
        if is_safe:
            num_safe += 1
        print(f"{row_num+1} is safe row: {is_safe}")
    
    return num_safe

def is_safe_row(row):
    increasing, i_indexes = is_increasing(row)
    decreasing, d_indexes = is_decreasing(row)
    is_differ, df_indexes = is_right_differ(row)
    
    # if increasing == decreasing and not increasing:
    #     if len(i_indexes) == 1:
    #         increasing = True
    #     elif len(d_indexes) == 1:
    #         decreasing =True
            
    if not is_differ and len(df_indexes) == 1:
        is_differ = True
        print(f"fixable: {df_indexes}")
            
    return (increasing or decreasing) and is_differ
        
def is_right_differ(row, min_differ=1, max_differ=3):
    is_differ = True
    wrong_indexes = []
    for num, index in zip(row, range(len(row))):
        if index+1 < len(row):
            diff = abs(num - row[index + 1])
            is_differ = is_differ and (diff <= max_differ and diff >= min_differ)
            
            if not is_differ and not wrong_indexes.count(num):
                wrong_indexes.append(row[index + 1])
                
    return is_differ, wrong_indexes
            
        
def is_increasing(row):  
    sorted_row = sorted(row)
    return is_non_monotonous(row, sorted_row)

def is_non_monotonous(row, sorted_row):
    wrong_indexes = []
    monotonous = True
    for x,y in zip(row, sorted_row):
        if x != y and not wrong_indexes.count(y):
            wrong_indexes.append(x)
        monotonous = monotonous and (x==y)
    
    return monotonous, wrong_indexes
    # return functools.reduce(lambda x,y: x and y, [x == y for x, y in zip(row, sorted_row)])

def is_decreasing(row):
    sorted_row = sorted(row, reverse=True)
    return is_non_monotonous(row, sorted_row)

def rotate_row(row, step=1):
    return row[step:]+row[:step]

def get_mat_from_file(file):
    input_f = open(file, "r")
    
    mat = []
    
    for line in input_f.readlines():
        row = []
        for item in line.split():
            row.append(int(item))
        mat.append(row)
        
    return mat

if __name__ == "__main__":
    main()