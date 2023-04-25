


from flask import Blueprint, render_template, current_app #, session

from web_app.models.product import DEFAULT_PRODUCTS


product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/products")
def products():
    # TODO: fetch products from the database instead
    products = DEFAULT_PRODUCTS

    #service = current_app.config["SPREADSHEET_SERVICE"]
    #products = service.get_products()

    return render_template("products.html", products=products)
