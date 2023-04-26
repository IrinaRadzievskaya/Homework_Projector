import random

"""Practice 1"""

# en_ua_dictionary = {}
#
# en_ua_dictionary['red'] = 'червоний'
# en_ua_dictionary['green'] = 'зелений'
# en_ua_dictionary['blue'] = 'синій'
#
# if 'blue' not in en_ua_dictionary:
#     en_ua_dictionary['blue'] = 'unknown'
# if 'purple' not in en_ua_dictionary:
#     en_ua_dictionary['purple'] = 'unknown'
#
# for color_name, color_translation in en_ua_dictionary.items():
#     print(f"{color_name} in Ukrainian is {color_translation}")
#
# for color_name, color_translation in en_ua_dictionary.items():
#     if len(color_translation) < 5:
#         del en_ua_dictionary[color_name]
#
# print(en_ua_dictionary)


capitals = {
	'Ukraine': 'Kyiv',
	'France': 'Paris',
	'Germany': 'Berlin',
	'Italy': 'Rome',
	'USA': 'Washington',
	'Canada': 'Ottawa',
	'Switzerland': 'Bern',
	'Austria': 'Vienna',
	'Belgium': 'Brussels',
	'Sweden': 'Stockholm',
	'Norway': 'Oslo',
	'Denmark': 'Copenhagen',
	'Finland': 'Helsinki',
	'Poland': 'Warsaw',
	'Romania': 'Bucharest',
	'Bulgaria': 'Sofia',
	'Greece': 'Athens'
}


score = 0

print("Welcome to the Capital Guessing Game! Type 'exit' to quit.")
while True:
    # Get a random country and its capital from the dictionary
    country, capital = random.choice(list(capitals.items()))

    # Ask the user to guess the capital
    guess = input(f"What is the capital of {country}? ")

    # Check if the user wants to quit
    if guess.lower() == 'exit':
        break

    # Check if the user's guess is correct
    if guess == capital:
        print("You are right!")
        score += 1
    else:
        print(f"Sorry, the capital of {country} is {capital}.")

    # Print the current score
    print(f"Your score is {score}.\n")

# Print the final score
print(f"Your final score is {score}!")
