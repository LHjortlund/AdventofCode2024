#AdventOfCode-Challenge day 1 part 1
#For reading the lines each side and store them in seperate lines
#then sum of differences

left =[]
right = []

with open("my_data.txt", encoding='utf-8') as file:
    for line in file:
        nums = line.strip().split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

#sort the left and right lists
left.sort()
right.sort()

#Compare the two smallest number form left and right lists, and store the differences
differences = []
for i in range(len(left)):
    difference = abs(left[i] - right[i])
    differences.append(difference)

#calculate the sum of the differences
sum_of_differences = sum(differences)

#print the differences
for diff in differences:
    print(diff)

print("sum of differences:", sum_of_differences)

    #contents = file.read()
    #print(content)

