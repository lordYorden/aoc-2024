
INPUT = "input1.txt"

def main():   
    list1, list2 = get_lists_from_file(INPUT)
        
    part1 = sol_part1(list1, list2)    
    print(f"Part 1 - solution: {part1}")
    
    part2 = sol_part2(list1, list2)    
    print(f"Part 2 - solution: {part2}")
    
def sol_part1(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    sum = 0
    for i,j in zip(list1, list2):
        sum += abs(i-j)
        
    return sum

def sol_part2(list1, list2):
    sum = 0
    for num in list1:
        sum += num * list2.count(num)
        
    return sum
    

def get_lists_from_file(file):
    input_f = open(file, "r")
    
    list1 = []
    list2 = []
    
    for line in input_f.readlines():
        s = line.split()
        list1.append(int(s[0]))
        list2.append(int(s[1]))
    
    return list1, list2
    
    

if __name__ == "__main__":
    main()