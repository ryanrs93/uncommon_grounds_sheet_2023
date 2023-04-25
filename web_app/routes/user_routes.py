
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from web_app.routes.auth_helpers import authenticated_route

user_routes = Blueprint("user_routes", __name__)

#
# USER PROFILE
#

@user_routes.route("/user/profile")
@authenticated_route
def profile():
    print("USER PROFILE...")
    current_user = session.get("current_user")
    return render_template("user_profile.html", user=current_user) # user=user


#
# USER ORDERS
#


@user_routes.route("/user/orders/create", methods=["POST"])
@authenticated_route
def create_order():
    print("CREATE USER ORDER...")

    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    product_id = form_data["product_id"]
    product_name = form_data["product_name"]
    product_price = form_data["product_price"]

    current_user = session.get("current_user")
    user_email = current_user["email"]

    # TODO: implement ordering
    flash(f"OOPS, Ordering not yet implemented!", "warning")
    return redirect("/user/orders")

    #service = current_app.config["SPREADSHEET_SERVICE"]
    #try:
    #    new_order = {
    #        "user_email": user_email,
    #        "product_id": int(product_id),
    #        "product_name": product_name,
    #        "product_price": float(product_price)
    #    }
    #    service.create_order(new_order)
    #    flash(f"Order received!", "success")
    #    return redirect("/user/orders")
    #except Exception as err:
    #    print(err)
    #    flash(f"Oops, something went wrong: {err}", "warning")
    #    return redirect("/products")


@user_routes.route("/user/orders")
@authenticated_route
def orders():
    print("USER ORDERS...")

    current_user = session.get("current_user")
    user_email = current_user["email"]

    service = current_app.config["SPREADSHEET_SERVICE"]
    orders = service.get_user_orders(user_email)

    return render_template("user_orders.html", orders=orders)
