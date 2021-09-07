positions = ["first", "second", "third"]
scores = []

for i in range(3):
    print("What is the name of the " + positions[i] + " team?")
    team = input("")
    print("How many games did the " + team + " win?")
    games = input("")
    scores.append([team, games])
    
scores = sorted(scores, key = lambda x:x[1], reverse=True)
# print(scores)

if scores[0][1] == scores[1][1]:
    print(str(scores[0][0]) + " and " + str(scores[1][0]) + " are tied. Who won the playoff?")
    winner = input("")
    print(winner + " won the league in a playoff.")
    
else:
    print(str(scores[0][0]) + " won the league with " + scores[0][1] + " wins.")