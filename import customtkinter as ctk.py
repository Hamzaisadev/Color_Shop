from tkinter import *
import customtkinter
from customtkinter import *
from CTkMessagebox import CTkMessagebox

#first i will add required module tkinter AND CUSTOM TKINTER
# First, import the custom tkinter module am





# Set the appearance of the custom Tkinter to dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")  
# Themes: "blue" (standard), "green", "dark-blue"

# Create the main window (root)
root = customtkinter.CTk()

# Set window title
root.title('POS System')

# Add an icon to the window (uncomment and provide the correct path to your icon file)
# root.iconbitmap("path/to/your/iconfile.ico")

# Set the window size
root.geometry("1500x750")
root.minsize(1400, 800)


def get_product():
    return

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
  print()
  
    # Add your logic here for calculating total


def login():
  username = enter_username.get()
  password = enter_password.get()
  if username == "admin" and password == "admin":
    admin = customtkinter.CTkToplevel()
    admin.geometry("1200x550")
    admin.title("Admin Page")
    
  elif username == "" and password == "":
    CTkMessagebox(title="Error", message="Please enter username and password", icon="error")


  elif username == "":
    CTkMessagebox(title="Error", message="Please enter username", icon="error")

  elif password == "":
    CTkMessagebox(title="Error", message="Please enter password", icon="error")

  else:
    CTkMessagebox(title="Error", message="Invalid username or password", icon="error")
  
    


def print_bill():
  print()





def show_history():
  return


# lets make buttons

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
    text_color="black",
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




headingLabel= customtkinter.CTkLabel(root ,text='KAMAL PAINT PORTAL',
  font=('times new roman',30,'bold'),
  text_color='yellow',
  fg_color='#F57D1F',
  justify='right')
headingLabel.pack()



#packing And placing Everything

#entry boxes :

enter_product.pack(pady=10)
enter_product.place(x=200,y=100)

enter_quantity.pack(pady=10)
enter_quantity.place(x=200,y=200)

enter_username.pack(pady=10)
enter_username.place(x=200,y=300)

enter_password.pack(pady=10)
enter_password.place(x=200,y=400)

#buttons :

add_to_cart.pack(pady=20)
add_to_cart.place(x=200,y=500)

exit_button.pack(pady=20)
exit_button.place(x=200,y=600)

total_button.pack(pady=20)
total_button.place(x=200,y=700)

login_button.pack(pady=20)
login_button.place(x=200,y=800)

print_bill_button.pack(pady=20)
print_bill_button.place(x=200,y=900)

history_button.pack(pady=20)
history_button.place(x=200,y=1000)

product_label.pack(pady=40)
price_label.pack(pady=40)
login_label.pack(pady=40)
password_label.pack(pady=40)

# Start the main loop
root.mainloop()
#lets make a function that will show output from entry box when i click button