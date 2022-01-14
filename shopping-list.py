shopping_list = [ 
    {'item' : 'lettuce', 'category': 'food', 'price': 5.50 },
    {'item' : 'mac n cheese', 'category': 'food', 'price': 2.00 },
    {'item' : 'soda', 'category': 'snacks', 'price': 1.50 },
    {'item' : 'milk', 'category': 'food', 'price': 3.75 },
    {'item' : 'fruits', 'category': 'food', 'price': 5.60 },
    {'item' : 'scrabble', 'category': 'toy', 'price': 10.50 },
    {'item' : 'dodge ball', 'category': 'toy', 'price': 5.89 },
    ]

def remove_toys(obj):
    if (obj['category'] == 'toy'):
        return False
    return True


def apply_tax(obj):
    obj['price'] = obj['price'] * 1.11
    return obj



# Filter out items that are toys
shopping_list = list(filter(remove_toys, shopping_list))
print("Toys removed from shopping list" , shopping_list)

# Map to apply sales tax to the remainder items 
shopping_list = list(map(apply_tax, shopping_list))
print("Sales tax applied", shopping_list)
