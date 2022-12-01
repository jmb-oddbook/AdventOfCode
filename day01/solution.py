# Input parameters:
# one positive integer value per line representing calories
# values are grouped by a blank line, each group represents one elf

# Returns:
# the number of the elf carrying the highest total of calories and the total number of calories

elf_backpack = []
total = 0

with open ("day01/input_data.txt", "r") as inventory:
    for line in inventory:
        if line != "\n":
            num = int(line)
            total += num
        else:
            elf_backpack.append(total)
            total = 0

print(f"Elf {elf_backpack.index(max(elf_backpack))+1} is carrying the highest amount of calories. They have {max(elf_backpack)}. Go raid them.")


# Returns:
# the total number of calories the top 3 elves are carrying

elf_backpack.sort()
print(f"The top three elves are carrying {sum(elf_backpack[-3:])} calories. Don't worry, you're set.")
