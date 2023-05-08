
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Hot Coffee', 'description': '$3.25', 'price': 3.25, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/coffee.jpg'},
    {'id': 2, 'name': 'Iced Coffee', 'description': '$3.50', 'price': 3.50, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/coffee_iced.jpg'},
    {'id': 3, 'name': 'Hot Half and Half', 'description': '$4.15', 'price': 4.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/half_and_half_2.jpg'},
    {'id': 4, 'name': 'Iced Half and Half', 'description': '$4.50', 'price': 4.50, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/iced_half_and_half.jpg'},
    {'id': 5, 'name': 'Hot Matcha Latte', 'description': '$5.40', 'price': 5.40, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/matcha_latte.webp'},
    {'id': 6, 'name': 'Iced Matcha Latte', 'description': '$5.50', 'price': 5.50, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/iced_matcha.jpg'},
    {'id': 7, 'name': 'Cafe Au Lait', 'description': '$4.00', 'price': 4.00, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/cafe_au_lait.jpg'},
    {'id': 8, 'name': 'Hot Tea', 'description': '$3.15', 'price': 3.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/tea.jpg'},
    {'id': 9, 'name': 'Iced Tea', 'description': '$3.45', 'price': 3.45, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/iced_tea.jpg'},
    {'id': 10, 'name': 'Hot Chocolate', 'description': '$4.25', 'price': 4.25, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/hot_chocolate.webp'},
    {'id': 11, 'name': 'Hot Chai Latte', 'description': '$5.15', 'price': 5.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/chai_latte.jpg'},
    {'id': 12, 'name': 'Iced Chai Latte', 'description': '$5.25', 'price': 5.25, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/iced_chai.webp'},
    {'id': 13, 'name': 'Italian Soda', 'description': '$4.00', 'price': 4.00, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/italian_soda.jpg'},
    {'id': 14, 'name': 'Espresso', 'description': '$3.25', 'price': 3.25, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/espresso.jpg'},
    {'id': 15, 'name': 'Latte', 'description': '$3.15', 'price': 3.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/latte.jpeg'},
    {'id': 16, 'name': 'Cappuccino', 'description': '$4.15', 'price': 4.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/cappuccino.jpeg'},
    {'id': 17, 'name': 'Red Eye', 'description': '$4.25', 'price': 4.25, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/redeye.jpg'},
    {'id': 18, 'name': 'Americano', 'description': '$5.40', 'price': 5.40, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/americano_2.jpg'},
    {'id': 19, 'name': 'Macchiato', 'description': '$5.15', 'price': 5.15, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/macchiato.webp'},
    {'id': 20, 'name': 'Mocha', 'description': '$4.00', 'price': 4.00, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/mocha_2.jpg'},
    {'id': 21, 'name': 'Dirty Chai', 'description': '$3.75', 'price': 3.75, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/dirty_chai.jpg'},
    {'id': 22, 'name': 'Smoothies', 'description': '$5.99', 'price': 5.99, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/smoothie.jpg'},
]


class Product:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.description = attrs.get("description")
        self.price = attrs.get("price")
        self.url = attrs.get("url")
        self.created_at = attrs.get("created_at")

    @property
    def to_row(self):
        return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
