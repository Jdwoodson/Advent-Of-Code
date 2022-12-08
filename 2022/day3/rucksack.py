'''
Take a string, split in half
Find common letter in two halves
a-z : 1-26
A-Z : 27-52
Get priority for each line
Add sums of priorities
'''

import string

priority = {}
priority_num = 0
priority_totals_p1 = []
priority_totals_p2 = []

with open('2022/day3/rucksack_input.txt', 'r', encoding="utf8") as file:
    rucksacks = file.read()
    rucksacks = rucksacks.strip().split('\n')

for letter in string.ascii_letters:
    priority_num += 1
    priority[letter] = priority_num
    
    
for rucksack in rucksacks:
    ruck_len = int(len(rucksack)/2)
    compartment_1 = set(rucksack[:ruck_len])
    compartment_2 = set(rucksack[ruck_len:])
    ruck_set = compartment_1 & compartment_2
    for item in ruck_set:
        priority_totals_p1.append(priority[item])
        
print(sum(priority_totals_p1))

elve_groups = [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]

for elf in elve_groups:
    set1 = set(elf[0])
    set2 = set(elf[1])
    set3 = set(elf[2])
    megaset = set1 & set2 & set3
    for item in megaset:
        priority_totals_p2.append(priority[item])

print(sum(priority_totals_p2))