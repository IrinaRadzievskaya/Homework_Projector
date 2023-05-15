
# class Country:
# 	def __init__(self, name, population, capital):
# 		self.name = name
# 		self.population = population
# 		self.capital = capital
#
# 	def increase_population(self, increase_amount):
# 		self.population += increase_amount
#
# 	def add(self, other_country):
# 		combined_name = f"{self.name} {other_country.name}"
# 		combined_population = self.population + other_country.population
# 		combined_capital = None  # Placeholder for now
# 		return Country(combined_name, combined_population, combined_capital)
#
# japan = Country('Japan', 140_000_000, 'Tokyo')
# print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
#
# japan.increase_population(1_000_000)
# print(f"The new population of {japan.name} is {japan.population}.")
#
# bosnia = Country('Bosnia', 10_000_000, 'Sarajevo')
# herzegovina = Country('Herzegovina', 5_000_000, 'Mostar')
#
# bosnia_herzegovina = bosnia.add(herzegovina)
# print(f"Combined population of Bosnia and Herzegovina is {bosnia_herzegovina.population}.")
# print(f"The combined name of Bosnia and Herzegovina is '{bosnia_herzegovina.name}'.")


# class Car:
# 	def __init__(self, brand, model, year):
# 		self.brand = brand
# 		self.model = model
# 		self.year = year
# 		self.speed = 0
#
# 	def accelerate(self):
# 		self.speed += 5
#
# 	def brake(self):
# 		if self.speed >= 5:
# 			self.speed -= 5
# 		else:
# 			self.speed = 0
#
#
# car = Car('Toyota', 'Camry', 2022)
# print(f"Initial speed: {car.speed}")
#
# car.accelerate()
# print(f"Speed after acceleration: {car.speed}")
#
# car.brake()
# print(f"Speed after braking: {car.speed}")





