class BakeryChatbot:
    def _init_(self):
        self.menu = {
            "croissant": 3.50,
            "baguette": 2.00,
            "sourdough": 4.00,
            "cupcake": 2.50,
            "cookie": 1.50,
        }
        self.order = {}

    def welcome_message(self):
        return "Welcome to the bakery! How can I assist you today?"

    def process_message(self, message):
        if message.lower() == "menu":
            return self.display_menu()
        elif message.lower() == "view order":
            return self.display_order()
        elif message.lower() == "quit":
            return self.place_order()
        else:
            return self.add_item_to_order(message)

    def display_menu(self):
        menu_items = "\n".join([f"{item}: ${price}" for item, price in self.menu.items()])
        return f"Our menu today:\n{menu_items}"

    def add_item_to_order(self, item):
        if item.lower() not in self.menu:
            return "Sorry, we don't have that item in our menu. Please choose something from the menu."
        quantity = input("How many would you like to order? ")
        if not quantity.isdigit():
            return "Invalid quantity. Please enter a number."
        self.order[item.lower()] = int(quantity)
        return f"Added {quantity} {item}(s) to your order."

    def display_order(self):
        if not self.order:
            return "Your order is empty."
        order_items = "\n".join([f"{item}: {quantity}" for item, quantity in self.order.items()])
        return f"Your current order:\n{order_items}"

    def place_order(self):
        if not self.order:
            return "Thank you for visiting. Have a great day!"
        total_amount = sum([self.menu[item] * quantity for item, quantity in self.order.items()])
        self.order = {}
        return f"Thank you for your order. Your total amount is ${total_amount}. Enjoy your meal!"


def main():
    chatbot = BakeryChatbot()
    print(chatbot.welcome_message())

    while True:
        message = input("> ")
        response = chatbot.process_message(message)
        print(response)
        if response.startswith("Thank you"):
            break


if _name_ == "_main_":
    main()