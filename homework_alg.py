cats = [False] * 100  # Initially, no cat has a hat

for i in range(1, 101):  # Walk around the circle 100 times
    for j in range(i - 1, 100, i):  # Stop at every ith cat
        cats[j] = not cats[j]  # Put a hat on if it doesn't have one, or take it off if it does

# Output the cats that have hats
for i, has_hat in enumerate(cats):
    if has_hat:
        print(f"Cat #{i+1} has a hat.")