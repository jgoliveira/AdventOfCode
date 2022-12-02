with open('input.txt') as f:
    elfs_foods = f.read().split("\n\n") #slipt on empty lines

elfs_calories = []
for elf in elfs_foods:
    calories = sum(map(int, elf.splitlines()))
    elfs_calories.append(calories)

print(max(elfs_calories))
elfs_calories = sorted(elfs_calories)
print(sum(elfs_calories[-3:]))