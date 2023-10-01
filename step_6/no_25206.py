total_hack = 0
total_score = 0
for i in range(20) :
    o, hack, score = input().split()
    hack = int(hack[0])
    total_hack += hack
    if score == "P" :
        total_hack -= hack
        continue
    elif score == 'A+' :
        total_score += hack * 4.5
    elif score == 'A0' :
        total_score += hack * 4.0
    elif score == 'B+' :
        total_score += hack * 3.5
    elif score == 'B0' :
        total_score += hack * 3.0
    elif score == 'C+' :
        total_score += hack * 2.5
    elif score == 'C0' :
        total_score += hack * 2.0
    elif score == 'D+' :
        total_score += hack * 1.5
    elif score == 'D0' :
        total_score += hack * 1.0
    else :
        total_score += hack * 0.0
print(total_score / total_hack)