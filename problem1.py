from unicodedata import category


menu_items = [{
    'name': 'Sprite',
    'category': 'drink',
    'price': 3
},
{
    'name': ' Turkey Sandwich',
    'category': 'food',
    'price': 6
},
{
    'name': 'Hot Cheetos',
    'category': 'food',
    'price': 2
},
{
    'name': 'Tea',
    'category': 'drink',
    'price': 2
},
{
    'name': 'Water',
    'category': 'drink',
    'price': 4
},
{
    'name': 'Coffee',
    'category': 'drink',
    'price': 5
},
{
    'name': 'Pens',
    'category': 'supply',
    'price': 10
}
]

def drinks_only(obj):
    if obj['category'] == 'drink':
        return True 
    else:
        return False

def add_crv(obj):
    obj['price'] += .10
    return obj 

show_drinks = list(filter(drinks_only, menu_items))
drink_crv = map(add_crv, show_drinks)
print('ONLY DRINKS',show_drinks)
print('DRINK CRV...', list(drink_crv))

