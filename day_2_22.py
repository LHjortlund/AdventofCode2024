#step 1 read input fra day1_data.txt
#step 2 giv dine valg (x,y,z værdier)
#beregn point for valget og udfald af runden
#step 4 beregn sum for alle runder

#A og X = Rock
#B og Y = Paper
#C og Z = Scissors 

#Tildel værdi/point for hvert bogstav
shape_scores = {'X': 1, 'Y':2, 'Z': 3}

#Score fordelingen (tabt = 0, uafgjort = 3, sejr = 6)
outcome_scores = {
    ('A', 'X'): 3, #Rock vs Rock = Uafgjort
    ('A', 'Y'): 6, #Rock vs Paper = sejr
    ('A', 'Z'): 0, #Rock vs Scissors = tab
    ('B', 'X'): 0, #Paper vs Rock = tab
    ('B', 'Y'): 3, #Paper vs Paper = uafgjort
    ('B', 'Z'): 6, #Paper vs Scissors = Sejr
    ('C', 'X'): 6, #Scissors vs Rock = Sejr
    ('C', 'Y'): 0, #Scissors vs paper = tab
    ('C', 'Z'): 3 #Scissors vs scissors = uafgjort
}

total_score = 0

#indlæs inputtet fra day2_data.txt og beregn total_score
with open("day2_data.txt",encoding='utf-8') as file:
    for line in file:
        opponent, player = line.strip().split()
        total_score += shape_scores[player] + outcome_scores[(opponent, player)]

print("Total scores: ", total_score)