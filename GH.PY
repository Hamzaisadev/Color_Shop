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

    # Update the listbox display
    listbox_products.insert(tk.END, product_name)
    listbox_products.insert(tk.END , f"Price: ${product_price}")

    # Example: Display a message box with the added product
    messagebox.showinfo("Product Added", f"Product '{product_name}' added successfully!")

def generate_bill():
    # Calculate the total amount based on added products
    total_amount = sum(price for _, price in added_products)
    label_total.config(text=f"Total Amount: ${total_amount:.2f}")

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
button_clear_cart = tk.Button(root, text="Clear Cart", command=generate_bill)

# Create a listbox to display added products
listbox_products = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox_cart = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=20)

# Create a label for displaying the total amount
label_total = tk.Label(root, text="Total Amount: $0.00")

# Arrange the widgets
label_product.pack()
entry_product.pack()

label_price.pack()
entry_price.pack()

button_add.pack()
button_generate_bill.pack()

listbox_products.pack()
listbox_cart.pack()
label_total.pack()

root.mainloop()
