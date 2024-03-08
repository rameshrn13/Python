# Define a dictionary of items and their prices
items = {
    "apple": 10,
    "banana": 50,
    "bread": 20,
    "milk": 50,
    "eggs": 25,
    # Add more items and prices as needed
}
print("\n=== Supermarket ===")
print("""
         apple
         banaba
         milk
         eggs
         bread """)
# Initialize an empty cart
cart = {}

# Function to add items to the cart
def add_to_cart(item, quantity):
    if item in items:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to the cart.")
    else:
        print("Item not found in the store.")

# Function to generate the bill
def generate_bill():
    total_cost = 0
    print("\n=== Your Bill ===")
    for item, quantity in cart.items():
        if item in items:
            item_price = items[item]
            item_total = item_price * quantity
            total_cost += item_total
            print(f"{item}: {quantity} x {item_price:.2f} = {item_total:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print("Thank you for shopping with us!")

# Main program loop
while True:
    
    print("1. Add item to cart")
    print("2. Generate bill")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        item_name = input("Enter the item name: ").lower()
        item_quantity = int(input("Enter the quantity: "))
        add_to_cart(item_name, item_quantity)
    elif choice == "2":
        generate_bill()
        break
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3).")
