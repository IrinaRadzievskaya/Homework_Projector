import random as rd

"""Practice block 1:"""


# def outer_function(a, b):
# 	def inner_function():
# 		return a + b
#
# 	addition = inner_function() + 5
# 	return addition
#
#
# result = outer_function(2, 3)
# print(result)


"""Practice block 2"""

# while True:
#     try:
#         num = int(input("Please enter an integer: "))
#         print("You entered:", num)
#         break
#     except ValueError:
#         print("Invalid input! Please enter an integer.")


# while True:
#     try:
#         string = input("Please enter a string: ")
#         index = int(input("Please enter an integer index: "))
#         char = string[index]
#         print("The character at index", index, "is:", char)
#         break
#     except ValueError:
#         print("Invalid input! Please enter an integer index.")
#     except IndexError:
#         print("Index out of range! Please enter a valid index.")


"""Practice block 3"""


# def random():
# 	return rd.randint(1, 6)
# 	result = roll_dice()
# 	print("You rolled a: ", result)
#
#
# print(random())



# def simulate_rolls(num_rolls):
#     rolls = [0, 0, 0, 0, 0, 0] # initialize list to count each roll
#     for i in range(num_rolls):
#         roll = rd.randint(1, 6) # simulate a single roll
#         rolls[roll-1] += 1 # increment count for the corresponding value
#     return rolls
#
#
# counts = simulate_rolls(10000)
# print("Counts for each dice value:", counts)


# def simulate_election(num_regions, candidate_ratings):
#     total_votes = 0
#     candidate_votes = 0
#     for i in range(num_regions):
#         region_rating = candidate_ratings[i]
#         region_votes = {"candidate1": 0, "candidate2": 0}
#         for j in range(10000):
#             vote = rd.random() * 100
#             if vote < region_rating:
#                 region_votes["candidate1"] += 1
#             else:
#                 region_votes["candidate2"] += 1
#         total_votes += sum(region_votes.values())
#         region_winner = max(region_votes, key=region_votes.get)
#         print(f"Region {i+1}: {region_votes['candidate1']} votes for candidate 1, {region_votes['candidate2']} votes for candidate 2")
#         if region_winner == "candidate1":
#             candidate_votes += region_votes["candidate1"]
#         else:
#             candidate_votes += region_votes["candidate2"]
#     winner = "candidate1" if candidate_votes > (total_votes / 2) else "candidate2"
#     print(f"\nResult: {winner} won with {candidate_votes} votes and {round((candidate_votes / total_votes)*100, 1)}% of all votes")
#
#
#
#
# simulate_election(2, [34, 56])





"""Practice block 4"""

my_tuple = ("Iren", "Radz", 27)
last_name = my_tuple[1]
print(last_name)

first_name, last_name, age = my_tuple
for letter in my_tuple[0]:
    print(letter)
for letter in my_tuple[1]:
    print(letter)

new_tuple = tuple(s[1:] if isinstance(s, str) else s for s in my_tuple)
print(new_tuple)

my_new_tuple = ((1, 2), (3, 4))

my_tuple = (1, 2, 3, 4, 5)
total = sum(my_tuple)
print(total)











