#Del hver linje i to dele (det er en rugsack)
#Find det bogstav der er på begge halvdele
#Giv hvert bogstav en værdi for hvilken prioritet det har 
#Beregn summen for alle prioriteter 


#step 1: tildel bogstaverne en prioritet efter alfabetet 
#step 2: indlæs data fra day3_data
#step 3: del hver linje i 2 halvdele
#step 4: find fællesnævneren
#step 5: beregn summen af prioriteterne

def get_priority(item):
    """Konverter et bogstav til en prioritet""" #docstring
    if 'a' <= item <= 'z': #lower-case bogstaver (a-z) = 26
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z': #upper case bogstaver (A-Z) = 27-52
        return ord(item) - ord('A') + 27
    return 0 #skal ikke ske, men en sikring


