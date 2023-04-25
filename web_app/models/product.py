
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Strawberries', 'description': 'Juicy organic strawberries.', 'price': 4.99, 'url': 'https://picsum.photos/id/1080/360/200'},
    {'id': 2, 'name': 'Cup of Tea', 'description': 'An individually-prepared tea or coffee of choice.', 'price': 3.49, 'url': 'https://picsum.photos/id/225/360/200'},
    {'id': 3, 'name': 'Textbook', 'description': 'It has all the answers.', 'price': 129.99, 'url': 'https://picsum.photos/id/24/360/200'},
    #{'id': 4, 'name': 'Online Course', 'description': 'Level up your programming skills.', 'price': 129.99, 'url': 'https://picsum.photos/id/180/360/200'},
    #{'id': 5, 'name': '________', 'description': '___________.', 'price': 0.99, 'url': '__________'},
    #{'id': 6, 'name': '________', 'description': '___________.', 'price': 0.99, 'url': '__________'},
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
