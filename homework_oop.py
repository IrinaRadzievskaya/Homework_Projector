"""Task 1."""

# class Product:
# 	def __init__(self, name, price, quantity):
# 		self.name = name
# 		self.price = price
# 		self.quantity = quantity
#
#
# class Book(Product):
# 	def __init__(self, name, price, quantity, author):
# 		super().__init__(name, price, quantity)
# 		self.author = author
#
# 	def read(self):
# 		print(f"Reading {self.name} by {self.author}")
#
#
# p = Product("Widget", 10.0, 5)
# print(p.name) # Widget
# print(p.price) # 10.0
# print(p.quantity) # 5
#
# b = Book("The Hitchhiker's Guide to the Galaxy", 12.0, 3, "Douglas Adams")
# print(b.name)
# print(b.price)
# print(b.quantity)
# print(b.author)
# b.read()



"""Task 2"""


class Restaurant:
	def __init__(self, name, cuisine, menu):
		self.name = name
		self.cuisine = cuisine
		self.menu = menu


class FastFood(Restaurant):
	def __init__(self, name, cuisine, menu, drive_thru):
		super().__init__(name, cuisine, menu)
		self.drive_thru = drive_thru

	def order(self, dish_name, quantity):
		if dish_name in self.menu:
			dish = self.menu[dish_name]
			price = dish['price']
			available_quantity = dish['quantity']

			if available_quantity >= quantity:
				total_cost = price * quantity
				dish['quantity'] -= quantity
				return total_cost
			else:
				return "Requested quantity not available"
		else:
			return "Dish not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
