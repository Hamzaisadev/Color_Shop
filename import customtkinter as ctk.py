#first i will add required module tkinter AND CUSTOM TKINTER
# First, import the required modules
from tkinter import *
from turtle import width
import customtkinter
from customtkinter import *

# Set the appearance of the custom Tkinter to dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the main window (root)
root = customtkinter.CTk()

# Set window title
root.title('POS System')

# Add an icon to the window (uncomment and provide the correct path to your icon file)
# root.iconbitmap("path/to/your/iconfile.ico")

# Set the window size
root.geometry("1500x750")
root.minsize(1400, 800)

#lets 
    
def get_product():
    # i am using .configure the property of CTk to configure ofcourse
    product_label.configure(text=f'product {enter_product.get()} added successfully')
    
    
# lets make buttons
#editing buttons aswell

#add to cart button
add_to_cart = customtkinter.CTkButton(root,
    text ="add to cart",
    width =120,   # change width of button
    height =60,  # change height of button
    font=("helvetica",19),  # Change font of button
    text_color="black",  #  Change color of button
    fg_color="yellow",  # Change color of button foreground
    hover_color="#c2b84e",  #   Change color of when mouse hovers
    corner_radius=200,#    change corner raduis of button
    command=get_product ) #and now we will add function to our button by calling def function

#exit button
exit_button = customtkinter.CTkButton(root, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)


#total button
total_button = customtkinter.CTkButton(root, text ="Total",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)


#login button
login_button = customtkinter.CTkButton(root, text ="Login",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)


#print button
print_bill_button = customtkinter.CTkButton(root, text ="Print Bill",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200 )

#history buttons
history_button = customtkinter.CTkButton(root, text ="History",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)

    # now i will pack my button and give them padding
add_to_cart.pack(pady=20)
exit_button.pack(pady=20)
total_button.pack(pady=20)
login_button.pack(pady=20)
print_bill_button.pack(pady=20)
history_button.pack(pady=20)





#we use .CTkEntry to make entrybox
#product box
enter_product = customtkinter.CTkEntry(root,
    placeholder_text= "Enter product",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="yellow",
    placeholder_text_color="yellow",
    corner_radius=200)

#Quantity box
enter_quantity = customtkinter.CTkEntry(root,
    placeholder_text= "Enter Quantity",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="yellow",
    placeholder_text_color="yellow",
    corner_radius=200)

#password box
enter_password = customtkinter.CTkEntry(root,
    placeholder_text= "Enter Password",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="yellow",
    placeholder_text_color="yellow",
    corner_radius=200)


#Username box
enter_username= customtkinter.CTkEntry(root,
    placeholder_text= "Enter Username",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="yellow",
    placeholder_text_color="yellow",
    corner_radius=200)




#packing entry boxes
enter_product.pack(pady=10)
enter_quantity.pack(pady=10)
enter_username.pack(pady=10)
enter_password.pack(pady=10)



#using.CTklabels function
#my input from entry box will fo here
product_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

product_label.pack(pady=40)
    
    
    

# Start the main loop
root.mainloop()
#lets make a function that will show output from entry box when i click button
    
