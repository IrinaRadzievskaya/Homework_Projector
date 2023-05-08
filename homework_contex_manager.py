import random
import csv



# # Generate 26 file names
# file_names = [chr(i) + ".txt" for i in range(ord('A'), ord('Z') + 1)]
#
# # Generate a random number between 1 and 100 for each file
# file_numbers = [random.randint(1, 100) for _ in range(26)]
#
# # Write the numbers to each file
# for i in range(26):
#     with open(file_names[i], 'w') as f:
#         f.write(str(file_numbers[i]))
#
# # Write the summary to a file
# with open('summary.txt', 'w') as f:
#     for i in range(26):
#         f.write(file_names[i] + ": " + str(file_numbers[i]) + "\n")



# """Create file with some content."""
#
# content = """Тому що ніколи тебе не вирвеш,
# ніколи не забереш,
# тому що вся твоя свобода
# складається з меж,
# тому що в тебе немає
# жодного вантажу,
# тому що ти ніколи не слухаєш,
# оскільки знаєш і так,
# що я скажу,"""
#
# with open('first-file.txt', 'w') as f:
#     f.write(content)
#
# with open('first-file.txt', 'r') as f:
#     content = f.read()
#
# content_uppercase = content.upper()
#
# with open('second-file.txt', 'w') as f:
#     f.write(content_uppercase)


"""Write a program that will simulate user score in a game."""

# Define a list of player names
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

# Simulate 100 games for each player and record their scores
results = []
for player in players:
    for i in range(100):
        score = random.randint(0, 1000)
        results.append((player, score))

# Save the results to a CSV file
with open('game_scores.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Player name", "Score"])
    writer.writerows(results)




# Read the game scores from the CSV file
with open('game_scores.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    scores = {}
    for row in reader:
        player = row[0]
        score = int(row[1])
        if player not in scores or score > scores[player]:
            scores[player] = score

# Sort the scores by descending highest score
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Write the high scores to a new CSV file
with open('high_scores.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Player name", "Highest score"])
    for player, score in sorted_scores:
        writer.writerow([player, score])





