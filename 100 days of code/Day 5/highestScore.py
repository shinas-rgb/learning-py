scores = [34, 78, 93, 56, 87, 26]
highest_score = 0

for score in scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score is: {highest_score}")