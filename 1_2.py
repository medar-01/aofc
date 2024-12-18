from typing import List


class Number():
    def __init__(self, num):
        self.num = num
        self.times = 0

    def __str__(self):
        return f"{self.num}, {self.times}"

left_numbers = []
right_numbers = []
with open("1_1.txt", "r") as file:
    for line in file.readlines():
        numbers = line.split()
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))

left_numbers.sort()
right_numbers.sort()

numbers: List[ Number] = []
for l_num, r_num in zip(left_numbers, right_numbers):
    c_l_num = Number(l_num)
    for num in right_numbers:
        if c_l_num.num == num:
            c_l_num.times += 1
    numbers.append(c_l_num)
sum = 0
for n in numbers:
    sum += n.num * n.times
print(sum)