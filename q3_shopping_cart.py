#Spotting the Bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Buggy Function Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Expected Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

# Explanation:
# The default list cart=[] is created ONLY ONCE when the function is defined.
# So the same list is reused in future calls.
# That is why "apple", "banana", and "eggs" end up in the same list.


#Fixing
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nFixed Function Output:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))



#Shopping Cart Program
# Function to create a cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Function to add items to cart
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Function to attempt tuple modification
def update_price(price_tuple, new_price):

    # Tuples are immutable.
    # Attempting to modify them raises TypeError.

    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print("\nTuple Error:")
        print(e)


# Function to calculate total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)

    final_total = total - discount_amount

    return final_total


#MAIN PROGRAM
# Create carts for two customers
cart1 = create_cart("Rahul", 10)
cart2 = create_cart("Sneha", 5)

# Add items to Rahul's cart
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 800, 2)

# Add items to Sneha's cart
add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1000, 1)

# Display carts
print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

# Calculate totals
print("\nRahul's Final Total:", calculate_total(cart1))
print("Sneha's Final Total:", calculate_total(cart2))

# Tuple example
price_data = ("Laptop", 50000)

update_price(price_data, 60000)



# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared
# across function calls.


# 2. Difference between rebinding and mutating
#
# Rebinding:
# variable points to a completely new object.
#
# Example:
# x = [1, 2]
# x = [3, 4]
#
# Mutating:
# changing the existing object itself.
#
# Example:
# x.append(5)


# 3. Which are mutable?
#
# Mutable:
# list, dict, set
#
# Immutable:
# tuple, str, int


# 4. If a list is passed into a function and modified,
# do changes reflect outside?
#
# Yes.
# Because lists are mutable and passed by object reference.
# So modifying the same list inside the function changes
# the original list too.
