

import os
from datetime import datetime, timezone
from pprint import pprint

from dotenv import load_dotenv
import gspread
from gspread.exceptions import SpreadsheetNotFound

from web_app.models.product import Product, DEFAULT_PRODUCTS
from web_app.models.order import Order


load_dotenv()

DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)

GOOGLE_SHEETS_DOCUMENT_ID = os.getenv("GOOGLE_SHEETS_DOCUMENT_ID", default="OOPS Please get the spreadsheet identifier from its URL, and set the 'GOOGLE_SHEETS_DOCUMENT_ID' environment variable accordingly...")

SHEETS_MODELS_MAP = {
    # "sheet_name": ModelName
    "products": Product,
    "orders": Order,
}


class SpreadsheetService:
    # TODO: consider implementing a locking mechanism on sheet writes, to prevent overwriting (if it becomes an issue)
    # ... however we know that if we want a more serious database solution, we would choose SQL database (and this app is just a small scale demo)

    def __init__(self, credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH, document_id=GOOGLE_SHEETS_DOCUMENT_ID):
        print("INITIALIZING NEW SPREADSHEET SERVICE...")

        self.client = gspread.service_account(filename=credentials_filepath)

        self.document_id = document_id


    @staticmethod
    def generate_timestamp():
        return datetime.now(tz=timezone.utc)

    @staticmethod
    def parse_timestamp(ts:str):
        """
            ts (str) : a timestamp string like '2023-03-08 19:59:16.471152+00:00'
        """
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        return datetime.strptime(ts, date_format)

    #
    # READING DATA
    #

    @property
    def doc(self):
        """note: this will make an API call each time, to get the new data"""
        return self.client.open_by_key(self.document_id) #> <class 'gspread.models.Spreadsheet'>

    def get_sheet(self, sheet_name):
        return self.doc.worksheet(sheet_name)

    def get_records(self, sheet_name):
        """Gets all records from a sheet,
            converts datetime columns back to Python datetime objects
        """
        #print(f"GETTING RECORDS FROM SHEET: '{sheet_name}'")
        sheet = self.get_sheet(sheet_name) #> <class 'gspread.models.Worksheet'>
        records = sheet.get_all_records() #> <class 'list'>
        for record in records:
            if record.get("created_at"):
                record["created_at"] = self.parse_timestamp(record["created_at"])
        return sheet, records

    def get_products(self):
        _, products = self.get_records("products")
        return products

    def get_orders(self):
        _, orders = self.get_records("orders")
        return records

    def get_user_orders(self, user_email):
        _, orders = self.get_records("orders")
        return [order for order in orders if order["user_email"] == user_email]

    #
    # DELETING DATA
    #

    def destroy_all(self, sheet_name):
        """Removes all records from a given sheet, except the header row."""
        sheet, records = self.get_records(sheet_name)
        # start on the second row, and delete one more than the number of records,
        # ... to account for the header row
        sheet.delete_rows(start_index=2, end_index=len(records)+1)

    #
    # WRITING DATA
    #

    def create_records(self, sheet_name:str, new_records:list):
        sheet, records = self.get_records(sheet_name)
        next_row_number = len(records) + 2 # plus headers plus one

        # auto-increment integer identifier
        if any(records):
            existing_ids = [r["id"] for r in records]
            next_id = max(existing_ids) + 1
        else:
            next_id = 1

        new_rows = []
        model_class = SHEETS_MODELS_MAP[sheet_name]
        for new_record in new_records:
            new_record["id"] = next_id
            new_record["created_at"] = self.generate_timestamp()
            new_row = model_class(new_record).to_row
            new_rows.append(new_row)

            next_id += 1

        sheet.insert_rows(new_rows, row=next_row_number)

    def create_products(self, new_products:list):
        self.create_records("products", new_products)

    def create_product(self, new_product:dict):
        self.create_records("products", [new_product])

    def create_orders(self, new_orders:list):
        self.create_records("orders", new_orders)

    def create_order(self, new_order:dict):
        self.create_records("orders", [new_order])

    def seed_products(self):
        sheet, products = self.get_records("products")
        if not any(products):
            print("WRITING DEFAULT PRODUCTS...")
            self.create_products(DEFAULT_PRODUCTS)



if __name__ == "__main__":

    ss = SpreadsheetService()

    ss.seed_products()

    print("READING PRODUCTS...")
    sheet, records = ss.get_records("products")

    for record in records:
        print("-----")
        pprint(record)
