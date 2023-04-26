# """Practice block 1"""
#
#
# def compute_difference(first: list, second: list) -> tuple:
#     first_minus_second = [item for item in first if item not in second]
#     second_minus_first = [item for item in second if item not in first]
#     return (first_minus_second, second_minus_first)
#
#
# def test_compute_difference():
#     result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
#     assert result1 == (['a', 'b'], ['e'])
#
#     result2 = compute_difference([], ['c', 'd', 'e'])
#     assert result2 == ([], ['c', 'd', 'e'])
#
#     result3 = compute_difference([1, 2, 3], [4, 5, 6])
#     assert result3 == ([1, 2, 3], [4, 5, 6])
#
#     result4 = compute_difference([1, 2, 3], [2, 3, 4])
#     assert result4 == ([1], [4])
#
#
# test_compute_difference()



# def sum_of_two(nums: list, target: int) -> list:
#     num_dict = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_dict:
#             return [num_dict[complement], i]
#         num_dict[num] = i
#     return []
#
# def test_sum_of_two():
#     result1 = sum_of_two([2, 7, 11, 15], 9)
#     assert result1 == [0, 1]
#
#     result2 = sum_of_two([3, 2, 4], 6)
#     assert result2 == [1, 2]
#
#     result3 = sum_of_two([3, 3], 6)
#     assert result3 == [0, 1]
#
# test_sum_of_two()



"""Practice block 2"""

# original_list = [1, 4, 2, 5]
# sorted_list = sorted(original_list)
#
# print("Original List:", original_list)
# print("Sorted List:", sorted_list)






cities = [
	('New York City', 8550405),
	('Los Angeles', 3792621),
	('Chicago', 2695598),
	('Houston', 2100263),
	('Philadelphia', 1526006),
	('Phoenix', 1445632),
	('San Antonio', 1327407),
	('San Diego', 1307402),
	('Dallas', 1197816),
	('San Jose', 945942)
]

def get_population(city):
    return city[1]

sorted_cities = sorted(cities, key=get_population)

print("Sorted list of cities by population:")
for city in sorted_cities:
    print(city)

# Calculate total and average population
total_population = sum(city[1] for city in cities)
average_population = total_population / len(cities)

print(f"\nTotal population: {total_population}")
print(f"Average population: {average_population}")