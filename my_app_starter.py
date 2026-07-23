# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Danyah Alarqaban
#
# My store sells: Video Games and Game Add-ons
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
class Game:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    # TICKET 3: The price guard
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be below $0.")
        else:
            self.price = amount

    # TICKET 5: Each item's own action
    def deliver(self):
        print(f"Downloading game: {self.name}!")


# TICKET 4: A second kind of item
class AddOn(Game):
    def deliver(self):
        print(f"Installing add-on: {self.name}!")


# EXPLAIN:
# The same method name (deliver) works differently because
# each class has its own version of the method.


# TICKET 2: Make your real items
item1 = Game("Minecraft", 30)
item2 = Game("NBA 2K26", 70)
item3 = AddOn("Minecraft Skin Pack", 10)

# PREDICT:
# print(item1.name) will show: Minecraft
print(item1.name)

# BREAK ON PURPOSE
# PREDICT:
# The price should not change because -5 is invalid.
item1.set_price(-5)

# Message:
# Price cannot be below $0.
# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name, "added!")

    # TICKET 9: Checkout
    def checkout(self):
        total = 0

        print("\nChecking out...\n")

        for item in self.items:
            item.deliver()
            total += item.price

        print("----------------")
        print("Total: $" + str(total))


# TICKET 7: My menu and my cart
store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()

print("\nWelcome to the Video Game Store!")
print("1 - Minecraft ($30)")
print("2 - NBA 2K26 ($70)")
print("3 - Minecraft Skin Pack ($10)")


# TICKET 8: Let customers shop
# PREDICT:
# Picking 1 will add Minecraft to the cart.

while True:
    choice = input("Pick 1, 2, 3, or 'done': ")

    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
    else:
        print("Invalid choice.")
# TICKET 10: Test the whole app
# PREDICT:
# If I choose 1, 3, done:
#
# Minecraft added!
# Minecraft Skin Pack added!
# Downloading game: Minecraft!
# Installing add-on: Minecraft Skin Pack!
# Total: $40

cart.checkout()


# ============================================================
# CHALLENGE
# Added a third item (Minecraft Skin Pack) to the menu.
# ============================================================


