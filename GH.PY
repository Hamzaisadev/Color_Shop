from tkinter import *
import customtkinter
from PIL import Image
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from CTkListbox import *
import pandas as pd
import xlrd
import datetime


bill_amount = 0
#images
img = customtkinter.CTkImage(Image.open('images/logo1.png'),size=(170,170))




# Set the appearance of the custom Tkinter to dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")  
# Themes: "blue" (standard), "green", "dark-blue"

# now i will Create the main window (root)
root = customtkinter.CTk()

#here i am taking the size of the screenof the user with .winfo_screenwidth() and .winfo_screenheight()

width= root.winfo_screenwidth() 
height=root.winfo_screenheight()



# now I will use .geometry to set a size of the window and
#I will give the width and height variable as arguments

root.geometry("%dx%d" % (width, height))

root.state("iconic")


#now I will set the title of the window

root.title('POS System')


# Add an icon to the window (uncomment and provide the correct path to your icon file)
#root.iconbitmap("images/logo1.ico")

#creating the first function

# Define the function for the add to cart button

def add_to_cart():
  
#first we will we will take product and quantity from the entry boxes with .get
  df = pd.read_excel('data/products.xlsx')
  product = enter_product.get()
  quantity = enter_quantity.get()
  #now I will read the data from our Excel file using Panda module I imported
  available_products=pd.read_excel('data/products.xlsx')
  print (available_products)
  
  #now I will locate the name data frame from my excel file by using .df lock
  
  row = df.loc[df['name'] == product]
  
  #as you can see I took the name of the product from the entry box and I used .loc to locate the row of that product in my excel file

  #now I will use the if not condition to check if product is found or not
  
  if not row.empty:
    
    #now I will get the product price in the quantity from the XL file
    
    price = row["price"].item
    stock = row["stock"].item
    
    #now I will check if the stock is greater than the quantity
    if stock >= quantity:
      
      #now I will add the detailed of the product and the quantity and price into the list box I have created later in this code
      
      cart_listbox.insert(customtkinter.END,f"{product} - Quantity: {quantity} - Price: {price}Rs")
      
   #now I will update the bill amount by adding price multipied by the quantity
      
      bill_amount += price * quantity
      bill_label.cofigure(text=f"Bill Amount: {bill_amount}Rs")
      
  #now I will update the stock by subtracting the quantity from the stock

      df.loc[df["name"]==product, "stock"] -quantity
      df.to_excel("data/products.xlsx",
        index = False)

      #now I will show the error if quantity is not available

    else:
      CTkMessagebox(title="error",message="Quantity not available", icon="warning")
        
  #creating and another error if the product is not found
  
  else:
    CTkMessagebox(title="error",message="Product not found", icon="warning")

#function to exit program connected to exit button

def exit_program():
    # Show some retry/cancel warnings
    msg = CTkMessagebox(master=root,
      title="Are You Sure!",
    message="Do you want exit?",
    icon="warning",
    option_1="Yes",
    option_2= "No")
    yes_or_no = msg.get()
    if yes_or_no == "Yes":
        root.destroy()
    else:
        print("press yes to exit")


def calculate_total():

   return 



def login():
  username = enter_username.get()
  password = enter_password.get()
  if username == "admin" and password == "admin":
    admin = customtkinter.CTkToplevel(root)
    admin.geometry("1200x550")
    admin.title("Admin Page")
    admin.wm_transient(root)
    
    
    
    
    save_product = customtkinter.CTkButton(admin, text ="SAVE",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)
    
    delete_product = customtkinter.CTkButton(admin, text ="SAVE",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)
    
    
    
    
    
    enter_product_name = customtkinter.CTkEntry(admin,
    placeholder_text= "Enter product name",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)
    
    
    enter_product_quantity = customtkinter.CTkEntry(admin,
    placeholder_text= "Enter product quantity",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)
    
    
    enter_product_price = customtkinter.CTkEntry(admin,
    placeholder_text= "Enter Product Price",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)
    
    
    
    
    
    
    
    
    save_product.grid(row=1, column=3, )
    delete_product.grid(row=2, column=3, )
    enter_product_name.grid(row=3, column=3, )
    enter_product_quantity.grid(row=4, column=3, )
    enter_product_price.grid(row=admin, column=3, )
    
    
    

  elif username == "" and password == "":
    CTkMessagebox(title="Error", message="Please enter username and password", icon="warning")


  elif username == "":
    CTkMessagebox(title="Error", message="Please enter username", icon="warning")

  elif password == "":
    CTkMessagebox(title="Error", message="Please enter password", icon="warning")

  else:
    CTkMessagebox(title="Error", message="Invalid username or password", icon="warning")




def print_bill():
  print()






def show_history():
  return


# lets make buttons

#add to cart button
add_to_cart_button = customtkinter.CTkButton(root,
    text ="add to cart",
    width =120,   # change width of button
    height =60,  # change height of button
    font=("helvetica",19),  # Change font of button
    text_color="black",  #  Change color of button
    fg_color="yellow",  # Change color of button foreground
    hover_color="#c2b84e",  #   Change color of when mouse hovers
    corner_radius=200,#    change corner raduis of button
    command=add_to_cart ) #and now we will add function to our button by calling def function

#exit button
exit_button = customtkinter.CTkButton(root, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)


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
    corner_radius=200,
    command=login)


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
    text_color="#1B1B1E",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)



#we use .CTkEntry to make entrybox
#product box
enter_product = customtkinter.CTkEntry(root,
    placeholder_text= "Enter product",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

#Quantity box
enter_quantity = customtkinter.CTkEntry(root,
    placeholder_text= "Enter Quantity",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

#password box
enter_password = customtkinter.CTkEntry(root,
    placeholder_text= "Enter Password",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)


#Username box
enter_username= customtkinter.CTkEntry(root,
    placeholder_text= "Enter Username",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200,)




#using.CTklabels function
#my input from entry box will fo here
product_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

price_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

login_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

password_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

bill_label = customtkinter.CTkLabel(root,
    text ="",
    font=("helvetica",19))

headingLabel= customtkinter.CTkLabel(root ,text='KAMAL PAINT PORTAL',
  font=('times new roman',50,'bold'),
  text_color='yellow',
  image=img,
  compound=LEFT)





cart_listbox = CTkListbox(root,
  width=500,
  height=500,
  font=("helvetica",24))


# Create a grid for the input widgets

root.columnconfigure((1,2,3,4,5,6,7,8,9,),weight=0)

# Place the input widgets in the grid
enter_product.grid(row=4, column=0, )
enter_quantity.grid(row=5, column=0, )
enter_username.grid(row=1, column=2,)
enter_password.grid(row=1, column=3, )

# Place the buttons in the grid
add_to_cart_button.grid(row=2, column=3, )
exit_button.grid(row=3, column=3,)
total_button.grid(row=4, column=3, )
login_button.grid(row=5, column=3, )
print_bill_button.grid(row=6, column=3, )
history_button.grid(row=7, column=3,)
cart_listbox.grid(row=5, column=4, )
headingLabel.grid(row=1, column=0 ,)
# ...

# Start the main loop









# -------------------------ADMIN WINDOW----------------------------


# exit_button = customtkinter.CTkButton(admin, text ="Exit",
#     width =120,
#     height =60,
#     font=("helvetica",19),
#     text_color="black",
#     fg_color="yellow",
#     hover_color="#c2b84e",
#     corner_radius=200,
#     command=exit_program)



# enter_quantity = customtkinter.CTkEntry(admin,
#     placeholder_text= "Enter Quantity",
#     width=500,
#     height=60,
#     font=("helvetica",24),
#     text_color="#F5DD90",
#     placeholder_text_color="yellow",
#     corner_radius=200)








root.mainloop()
#lets make a function that will show output from entry box when i click button
