import tkinter as tk
from tkinter import messagebox

# Placeholder for storing added products (you can replace this with your own data structure)
added_products = []

def add_product():
    # Get the product name and price from the entry fields
    product_name = entry_product.get()
    product_price = entry_price.get()

    # Add the product to the list (you can customize this part)
    added_products.append((product_name, float(product_price)))

    # Example: Display a message box with the added product
    messagebox.showinfo("Product Added", f"Product '{product_name}' added successfully!")

def generate_bill():
    # Calculate the total amount based on added products
    total_amount = sum(price for _, price in added_products)
    label_total.config(text=f"Total Amount: ${total_amount:.2f}")

def clear_cart():
    # Clear the list of added products
    added_products.clear()
    listbox_products.delete(0, tk.END)
    label_total.config(text="Total Amount: $0.00")

root = tk.Tk()
root.title("Color Shop POS System")
root.geometry("800x600")

# Create entry fields for product input
label_product = tk.Label(root, text="Enter Product:")
entry_product = tk.Entry(root)

label_price = tk.Label(root, text="Enter Price:")
entry_price = tk.Entry(root)

# Create buttons
button_add = tk.Button(root, text="Add Product", command=add_product)
button_generate_bill = tk.Button(root, text="Generate Bill", command=generate_bill)
button_clear_cart = tk.Button(root, text="Clear Cart", command=clear_cart)

# Create a listbox to display added products
listbox_products = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)

# Create a label for displaying the total amount
label_total = tk.Label(root, text="Total Amount: $0.00")

# Arrange the widgets
label_product.pack()
entry_product.pack()

label_price.pack()
entry_price.pack()

button_add.pack()
button_generate_bill.pack()
button_clear_cart.pack()

listbox_products.pack()

label_total.pack()

root.mainloop()

