def read_from_file(file: str) -> list:
    with open(file, "r") as file:
        all_array_num = []
        for line in file.readlines():
            numbers = [int(num) for num in line.split()]
            all_array_num.append(numbers)
        return all_array_num
    
def extract_good_list(all_array_num: list) -> list:
    extracted_numbers = []
    for row_num in all_array_num:
        min_num = min(row_num)
        len_set_num = len(row_num) - 1 
        if row_num.index(min_num) == len_set_num:    
            row_num.reverse()
        if row_num.index(min_num) == 0:
            extracted_numbers.append(row_num)
    return extracted_numbers

def check_step(all_num: list) -> int:
    safe_reports = 0
    for pack in all_num:
        previous = 0
        for i, n in enumerate(pack):
            try:
                if previous > n:
                    break
                next_n = pack[i + 1]
                abs_value = abs(n - next_n)
                previous = n
                if abs_value == 0:
                    break
                if abs_value <= 3:
                    continue
               
                else:
                    break
            except IndexError:
                safe_reports += 1
    return safe_reports

if __name__ == "__main__":
    list_number = extract_good_list(read_from_file("2_1.txt"))
    print(check_step(list_number))
        
    



















