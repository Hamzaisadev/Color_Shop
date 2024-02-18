import tkinter as tk
from tkinter import messagebox

def add_product():
    # Get the product name from the entry field
    product_name = entry_product.get()

    # Implement logic to add the product (e.g., store it in a list or display it)
    # You can customize this part based on your requirements

    # Example: Display a message box with the added product
    messagebox.showinfo("Product Added", f"Product '{product_name}' added successfully!")

root = tk.Tk()
root.title("Color Shop POS System")
root.geometry("800x600")

# Create an entry field for product input
label_product = tk.Label(root, text="Enter Product:")
entry_product = tk.Entry(root)
button_add = tk.Button(root, text="Add Product", command=add_product)

# Arrange the widgets
label_product.pack()
entry_product.pack()
button_add.pack()

root.mainloop()
