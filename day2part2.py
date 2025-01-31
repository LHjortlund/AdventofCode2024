# X, Y og Z angiver ikke længere Sten, paper og scissor, men 
# X angiver at du skal tabe
# Y angiver at det skal være uafgjort
# z angiver at du skal vinde

# strategi board
# Modstanderens valg:   du skal tabe(X)     du uafgjort(Y)      Du vinde(Z)
# A (Rock)              Scissors(C)         Rock(A)             Paper(B)
# B (paper)             Rock(A)             Paper (B)           Scissors (C)
# C (Scissors)          Paper(B)            Scissors(c)         Rock (A)

#Point for valg af form
shape_scores = {'A': 1, 'B': 2, 'C': 3} #Rock = 1, Paper = 2, Scissors = 3

#Valg for at opnå det ønskede resultat
choose_move = {
    ('A', 'X'): 'C', #Skal tabe mod Rock -> vælg Scissors (C)
    ('A', 'Y'): 'A', #skal være uafgjort -> vælg rock (A)
    ('A', 'Z'): 'B',#skal vinde --> vælg

    ('B', 'X'): 'A',#du skal tabe mod paper -> vælg rock
    ('B', 'Y'): 'B',#du skal uagjort -> vælg paper
    ('B', 'Z'): 'C', #du skal vinde -> vælg scissors

    ('C', 'X'): 'B', #du skal tabe mod scissors -> vælg paper
    ('C', 'Y'): 'C', #du skal uafgjort -> scissors 
    ('C', 'Z'): 'A', #du skal vinde -> vælg rock
}

#Point for udfaldet (tab = 0, uafgjort = 3, win = 6)
outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}

total_score = 0

#læs day2_data.txt og sum af total scores
with open("day2_data.txt", encoding="utf-8") as file:
    for line in file:
        opponent, outcome = line.strip().split()
        my_choice = choose_move[(opponent, outcome)] #find ud af hvad vi skal vælge
        total_score += shape_scores[my_choice] + outcome_scores[outcome]

print("Total score: ", total_score)