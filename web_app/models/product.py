
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Coffee', 'description': 'its a good coffee', 'price': 5.99, 'url': 'https://picsum.photos/id/1080/360/200'},
    {'id': 2, 'name': 'Tea', 'description': 'its a good coffee', 'price': 4.49, 'url': 'https://picsum.photos/id/225/360/200'},
    {'id': 3, 'name': 'Espresso', 'description': 'its a good coffee', 'price': 3.99, 'url': 'https://picsum.photos/id/24/360/200'},
    {'id': 4, 'name': 'Latte', 'description': 'its a good coffee', 'price': 8.99, 'url': 'https://picsum.photos/id/180/360/200'},
    {'id': 5, 'name': 'Cappuccino', 'description': 'its a good coffee', 'price': 3.99, 'url': 'https://picsum.photos/id/72/360/200'},
    {'id': 6, 'name': 'Mocha', 'description': 'its a good coffee', 'price': 4.99, 'url': 'https://raw.githubusercontent.com/ryanrs93/pics_uncommon_grounds/main/mocha.jpg'},
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
