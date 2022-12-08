f = open("day1/calories_input.txt", "r")

# create data objects to store data
elf_list = []
elf_dict = {}
total_weight = []
elf_number = 1

calories_input = f.read()
f.close()

# Split input based on double newline
calories_split = calories_input.split('\n\n')

# split list into elves based on list
calories_split = [elf.rsplit('\n') for elf in calories_split]

# create list of elves and convert to ints for compute
for elf in calories_split:
    elf_list.append([int(x) for x in elf])

# create dictionary to track elves by number and their weights
for elf in elf_list:
    elf_dict[elf_number] = sum(elf)
    elf_number += 1

# add total weights to a list to sort
for elf in elf_dict.values():
    total_weight.append(elf)
    
answer = max(total_weight)

# ding dong the witch is dead
print(answer)

# Give me the top 3 total weights
total_weight_sorted = sorted(total_weight, reverse=True)
second_answer = sum(total_weight_sorted[:3])

# wassup baby
print(second_answer)

