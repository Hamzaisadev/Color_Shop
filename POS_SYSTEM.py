
import tkinter as tk
import csv
import getpass
from typing import Self

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_sales = 0

class Sale:
    def __init__(self, product, quantity_sold):
        self.product = product
        self.quantity_sold = quantity_sold

class POS:
    def __init__(self):
        self.products = []
        self.root = tk.Tk()
        self.root.title("POS System")
        self.root.geometry("400x300")

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        product = Product(name, price, quantity)
        self.products.append(product)
        self.products_list.insert(tk.END, name)

    def record_sale(self):
        product_index = self.products_list.curselection()[0]
        quantity_sold = self.quantity_sold_entry.get()
        product = self.products[product_index]
        product.quantity -= quantity_sold
        product.total_sales += quantity_sold * product.price

    def get_total_sales(self):
        product_index = self.products_list.curselection()[0]
        product = self.products[product_index]
        return product.total_sales

    def load_products(self, file_path):
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # skip the header
            for row in csv_reader:
                self.add_product(row[0], float(row[1]), int(row[2]))

    def run(self):
        self.products_list = tk.Listbox(self.root)
        self.products_list.pack()
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()
        self.quantity_label = tk.Label(self.root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()
        self.quantity_sold_label = tk.Label(self.root, text="Quantity Sold:")
        self.quantity_sold_label.pack()
        self.quantity_sold_entry = tk.Entry(self.root)
        self.quantity_sold_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.add_button.pack()
        self.record_button = tk.Button(self.root, text="Record Sale", command=self.record_sale)
        self.record_button.pack()
        self.total_sales_label = tk.Label(self.root, text="Total Sales:")
        self.total_sales_label.pack()
        self.total_sales_value = tk.Label(self.root, text="0.00")
        self.total_sales_value.pack()
        self.load_products_button = tk.Button(self.root, text="Load Products", command=lambda: self.load_products("products.csv"))
        self.load_products_button.pack()
        self.root.mainloop()
   # Create the main window and frames
if __name__ == "__main__":
   pos = POS()
   pos.run()