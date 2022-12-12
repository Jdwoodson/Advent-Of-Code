with open('2022/day4/assignment_input.txt', encoding="utf8") as f:
    text = f.read().splitlines()

counter = 0


def elf_compare(elf1, elf2):
    """
    compare elves yo
    """
    for assignment in elf1:
        if assignment in elf2:
            return True
    for assignment in elf2:
        if assignment in elf1:
            return True


for line in text:
    assignments = line.split(',')
    elf1 = assignments[0].split('-')
    elf2 = assignments[1].split('-')
    elf1_start = elf1[0]
    elf1_end = elf1[1]
    elf2_start = int(elf2[0])
    elf2_end = int(elf2[1])
    elf1_range = []
    for x in range(int(elf1_start),int(elf1_end) + 1):
        elf1_range.append(x)
    elf2_range = []
    for x in range(int(elf2_start),int(elf2_end) + 1):
        elf2_range.append(x)
    if elf_compare(elf1_range, elf2_range):
        counter += 1

print(counter)
