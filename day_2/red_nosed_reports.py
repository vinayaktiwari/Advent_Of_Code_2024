list_of_lists = [] 
with open("day_2/text.txt", "r") as file:
    for line in file:
        if line.strip():
            numbers = list(map(int, line.split()))
            list_of_lists.append(numbers)


print(len(list_of_lists))


def count_safe(list_of_lists: list[list[int]]) -> int:
    safe = 0
    for l in list_of_lists:
        is_safe = True 
        for i in range(len(l) - 1):
            if not (1 <= abs(l[i] - l[i+1]) <= 3) or not(l[i]<l[i+1]):
                is_safe = False  
                break
        if is_safe:
            safe += 1
    return safe


def count_safe(list_of_lists: list[list[int]]) -> int:
    safe = 0
    for l in list_of_lists:
        is_increasing = True
        is_decreasing = True
        is_safe = True

        for i in range(len(l) - 1):
            if abs(l[i] - l[i + 1]) < 1 or abs(l[i] - l[i + 1]) > 3:
                is_safe = False
                break 
            if l[i] >= l[i + 1]:  
                is_increasing = False
            if l[i] <= l[i + 1]:  
                is_decreasing = False
         
        if (is_increasing or is_decreasing) and is_safe:
            safe += 1
    return safe


print("Day_2_ans",count_safe(list_of_lists=list_of_lists))


#====================== PART 2 =====================================s
def count_safe_with_dampner(list_of_lists: list[list[int]]) -> int:
    def is_safe(report: list[int]) -> bool:
        is_increasing = True
        is_decreasing = True
        for i in range(len(report) - 1):
            if report[i] >= report[i + 1]:  
                is_increasing = False
            if report[i] <= report[i + 1]:  
                is_decreasing = False
            if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
                return False
        return is_increasing or is_decreasing

    safe_count = 0
    for report in list_of_lists:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    safe_count += 1
                    break  
    return safe_count



print("Day_2_ans",count_safe_with_dampner(list_of_lists=list_of_lists))
