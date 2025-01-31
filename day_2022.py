#In case the Elves get hungry and need extra snacks, 
#they need to know which Elf to ask: they'd like to know 
# how many Calories are being carried by the Elf carrying the most Calories. 
# In the example above, this is 24000 (carried by the fourth Elf).
#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

#Read data from file calories_data.text og grupper calories pr. nisse
elves = []
current_elf = []

with open("calories_data.txt", encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line: #hvis linjen ikke er tom
            current_elf.append(int(line))
        else: #hvis vi møder en tom linje, gem gruppen og start en ny
            if current_elf:
                elves.append(sum(current_elf))
                current_elf = []

#Append den sidste gruppe, if filen ikke slutter med en tom linje
if current_elf:
    elves.append(sum(current_elf))

#Find nissen med flest calories
max_calories = max(elves)

print("Nissen med flest calories bærer:", max_calories)
        