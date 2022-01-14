businesses = [ 
    {'name' : 'Walgreens', 'phone number': '5105412562', 'type': 'drug store' },
    {'name' : 'Best Buy', 'phone number': '5156987452', 'type': 'drug store' },
    {'name' : 'local market', 'phone number': '', 'type': 'grocery store' },
    {'name' : 'corner store', 'phone number': '', 'type': 'liquor' },
    {'name' : 'walmart', 'phone number': '6325625215', 'type': 'grocery' },
    {'name' : 'facebook', 'phone number': '', 'type': 'social' },
    ]

# filter out businesses without a phone number 
businesses = list(filter(lambda business: business['phone number'] != '', businesses))
print("Filtered out businesses without a phone number" , businesses)

# map to only show the business name and phone number
businesses = map(lambda business: {'name':business['name'], 'phone number': business['phone number']}, businesses)
print("Show only business name and number" , list(businesses))