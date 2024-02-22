from tkinter import *
from tkinter import ttk

import customtkinter
from CTkListbox import *
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image
import tkinter 
import open_excel
import openpyxl 


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

#width= root.winfo_screenwidth() 
#height=root.winfo_screenheight()



# now I will use .geometry to set a size of the window and
#I will give the width and height variable as arguments

root.geometry("1920x1080")

#root.state("zoomed")


#now I will set the title of the window

root.title('POS System')


# Add an icon to the window (uncomment and provide the correct path to your icon file)
#root.iconbitmap("images/logo1.ico")



#creating the first function

#here I am defined the function of add to cart

def add_to_cart():

 #first we will we will take product and quantity from the entry boxes with .get
  product = enter_product.get()
  quantity = int (enter_quantity.get())

  #first I will open the Excel file with. open    xlrd open_workbook()
  
  workbook=open_excel.open_workbook("data/products.xlsx")
  
  #now I will select the sheet I want to use with .sheet_by_name
  
  sheet= workbook.sheet_by_index(0)
  
  #now I will loop through the rows of the sheet and add the data to the dictionary
  
  for row in range(1,sheet.nrow):
  
    #now I will get the product name price and quantity from the excel file
  
    product_name = sheet.cell_value(row,0)
    product_stock =sheet.cell_value(row,1)
    product_price =sheet.cell_value(row,2)
    
    #here i will use if conditíons to check the product
    
    if product == product_price:
      
      # now will check if product stock is available
      
      if product_stock >= quantity:
        
        #using another if so that it only works when stock is available
        #now i will total the price of the product_stock
        
        total_price = product_price * quantity
        
        #now I will format the product detail as a string
        product_details=f"{product_name} × {quantity} × {product_price} = {total_price}"
        #now I will add this formatted string into my cart list box
        cart_listbox.insert("END",product_details)
        #now I will update the stock in my excel file
        sheet.cell_value(row, 2,product_stock - quantity)
        #now I will save the changes in my excel file and break the loop
        workbook.save(workbook)
        #using .delete to delete text from entry boxes
        enter_product.delete(0, "END")
        enter_quantity.delete(0, "END")
        break
    #give same code by using now I will create an else statement that will show an error if product stock is not enough
    #using CTkMessagebox module i imported to show an error
    else:
      CTkMessagebox(title="Error", message="Product is out of stock", icon="warning")
      enter_product.delete(0, "END")
      enter_quantity.delete(0, "END")
      break
  else:
    #Error when Product is not found
    CTkMessagebox(title="Error", message="Product Not Found", icon="warning")
    enter_product.delete(0, "END")
    enter_quantity.delete(0, "END")
      
#Add to cart function done----------------------


#now i am writing exit_program func

#exit program function


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


#exit_program function done 


#now calculate_total function

def calculate_total():
  #first make a total amount var and gave it 0 
  total_amount = 0 
  #now i will loop through the cart
  for item in cart_listbox.get(0,"END"):
    
    #where I will create a variable called item parts and I will use items dot split to convert product detail strain into different strings its like it will create an list with different strings
    
    item_part = item.split()
    #now I will get the total price from the last part of item part string
    total_price = int(item_part[-2])
    #now i will add total price into the total ammount
    total_amount += total_price
    
  #now i will update the total ammount label
  total_label.configure(text=f"Total: {total_amount}")

  break

#calculate_total function done

#login function 

def login():
  #first I will get the username and password from the entry boxes
  username = enter_username.get()
  password = enter_password.get()
  #now I will check if the username and password are correct
  if username == "admin" and password == "admin":
    #if correct creating a new top level window  in root window with argument root
    admin = customtkinter.CTkToplevel(root)
    admin.geometry("1920x1080")
    admin.title("Admin Page")
    #this WM transient command will put top level window in front of my main window
    #thank to stackoverflow i found this command
    admin.wm_transient(root)


  #first i will create the main frames in admin window

    admin_heading_frame = customtkinter.CTkFrame(admin, width=100, height=100)
    product_add_frame = customtkinter.CTkFrame(admin, width=100, height=100)
    exel_file_frame = customtkinter.CTkFrame(admin, width=100, height=100)

#now I will create entry boxes and buttons
    #buttons
    save_product = customtkinter.CTkButton(product_add_frame, text ="Save Product",
      width =120,
      height =60,
      font=("helvetica",19),
      text_color="black",
      fg_color="yellow",
      hover_color="#c2b84e",
      corner_radius=200,
      command = save_product)

    
    
#entry boxes

    enter_product_name = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter product name",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)


    enter_product_quantity = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter product quantity",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)

    


    enter_product_price = customtkinter.CTkEntry(product_add_frame,
      placeholder_text= "Enter Product Price",
      width=500,
      height=60,
      font=("helvetica",24),
      text_color="#F5DD90",
      placeholder_text_color="yellow",
      corner_radius=200)


    admin_heading_Label= customtkinter.CTkLabel(admin_heading_frame ,text='HELLO ADMIN',
      font=('times new roman',50,'bold'),
      text_color='yellow',
      image=img, # i imported this img at the start of the code
      compound=LEFT)


    #now I have configured the rows and columns in my admin window

    admin.columnconfigure(0,weight =1,uniform="a")
    admin.columnconfigure(1,weight =4,uniform="a")
    admin.rowconfigure(0,weight =1,uniform="a")
    admin.rowconfigure(1,weight =5,uniform="a")

    
    # placing my frames in admin window with .grid

    
    admin_heading_frame.grid(row=0, column=0, columnspan=2,padx=5, sticky=tkinter.EW)
    product_add_frame.grid(row=1, column=0,padx=5, sticky=tkinter.NSEW)
    
    # this excel file frame will contain my excel file and show it in my admin window
    
    exel_file_frame.grid(row=1, column=1,padx=5, sticky=tkinter.NSEW)

    admin_heading_frame.columnconfigure(1,weight =5,uniform="a")
    admin_heading_Label.grid(row=0, column=0, columnspan=2,padx=5, sticky=tkinter.EW)

    #now configuring my frames to have rows and columns 
# configuring product add frame
    product_add_frame.columnconfigure(0 ,weight= 1)
    product_add_frame.columnconfigure(1 ,weight= 1)
    product_add_frame.rowconfigure(0,weight= 1)
    product_add_frame.rowconfigure(1,weight= 1)
    product_add_frame.rowconfigure(2 ,weight= 1)
    product_add_frame.rowconfigure(3 ,weight= 1)


    # now putting buttons and entry boxes in product add frames

    
    enter_product_name.grid(row=0 ,column=0,columnspan=1,padx=5)
    enter_product_price.grid(row=1 ,column=0,columnspan=1,padx=5)
    enter_product_quantity.grid(row=2 ,column=0,columnspan=1,padx=5)
    save_product.grid(row=3 ,column=0,padx=5)    
    
    # configuring excel file frame
    
    exel_file_frame.columnconfigure(1, weight=1)
    exel_file_frame.rowconfigure(1, weight=1)



  # so here I will use TTK frame from TTK module
  tree_frame =ttk.Frame(exel_file_frame)
  # will it a grid
  tree_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tkinter.NSEW)

  # now I will create a tuple named colm and i will put names of my columns in excel file
  colm = ("name", "stock", "price")

  #now I will create a treeview with the columns i created

  tree_view = ttk.Treeview(tree_frame, columns=colm, show="headings")
  
  # now i will pack it
  
  tree_view.pack(side="left", fill="both", expand=True)
  


  # now I will use openpyxl modular imported before

    # now I will make a function to load data
  def load_data():
  # I will give a path where my product file is
    path = "data/products.xlsx"
  #now I will open the file with openpyxl module
    workbook = openpyxl.load_workbook(path)
  #now I will select the sheet I want to use
  sheet= workbook.active

  # now I will create a list with tuples of all the data

  list_values = list(sheet.values)
  #now I will loop through the list and add the data to the treeview
  for col_name in list_values[0]:
  # now I will specify the name of my heading in my tree view
    tree_view.heading(col_name, text=col_name)
  
  # now I will loop through the list values and add the data to the treeview

  for value_tuple in list_values[1:]:
    tree_view.insert("", tk.END, values=value_tuple)
  
  


    # let's add two nested functions

  def save_product():
    
    #first we will get the product name, quantity and price from the entry boxes
    product_name = enter_product_name.get()
    product_stock = enter_product_quantity.get()
    product_price = enter_product_price.get()

  # now I will load the excel file same as  I did before in load data function

  # right now I am inserting data into Excel sheet
  path = "data/products.xlsx"
  workbook = openpyxl.load_workbook(path)
  #now I will select the sheet I want to use
  sheet= workbook.active

  # I will give the row values
  row_values =["name", "stock",'price']
  
  # now I will append these ROws into sheets

  sheet.append(row_values)
  # now I will save the workbook
  workbook.save(path)

  # adding this data into tree view

  tree_view.insert("", tk.END, values=row_values)
  
               
    # now I will delete the entry box text

  



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






def save():
  return

def clear_cart():
  return

#lets make heading menu i will include a logo ,name and login function
#first i will make a frame in which i will put widgets

heading_frame = customtkinter.CTkFrame(master=root, width=1100, height=500)
#now i will make a Username and Password entryboxes

enter_username= customtkinter.CTkEntry(heading_frame,
    placeholder_text= "Enter Username",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200,)

enter_password = customtkinter.CTkEntry(heading_frame,
    placeholder_text= "Enter Password",
    width=460,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

#i have entered the name of frame i created as the first argument  it is neccessary

#here i maked a login button ans at last set the command to login function i created earlier

login_button = customtkinter.CTkButton(heading_frame, text ="Login",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=login)

#now i have created the main text label 

headingLabel= customtkinter.CTkLabel(heading_frame ,text='KAMAL PAINT PORTAL',
  font=('times new roman',50,'bold'),
  text_color='yellow',
  image=img, # i imported this img at the start of the code
  compound=LEFT)

  ##so there are two function that are used to place widgets .pack and .grid  so I will use . grid to place the widgets in frame and window and i will do it ate the end of the code





  #-----------------heading frame done----------------------
  #-----------------now i will work on details frame----------------------

  #here is little complicated so i will make a details_frame and inside that details_frame i will place  two more frames
  #                   Main frame   

details_frame = customtkinter.CTkFrame(master=root,
width=10, 
height=10)

  #as you can see master of details_frame is root which is main main window

#                     order detail frame

order_detail_frame = ttk.LabelFrame(master=details_frame,
   text= "Order Details",
   width=200,
   height=200)

##here I used the LabelFrame from ttk ( you will have to import this aswell) 


    #       here i will create entry boxes 

enter_product = customtkinter.CTkEntry(order_detail_frame,
    placeholder_text= "Enter product name",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

#Quantity box
enter_quantity = customtkinter.CTkEntry(order_detail_frame,
    placeholder_text= "Enter Quantity",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

    #as you can see i have these entry boxes in order detail frame

    #now i will create buttons


add_to_cart_button = customtkinter.CTkButton(details_frame,
    text ="add to cart",
    width =120,   # change width of button
    height =60,  # change height of button
    font=("helvetica",19),  # Change font of button
    text_color="black",  #  Change color of button
    fg_color="yellow",  # Change color of button foreground
    hover_color="#c2b84e",  #   Change color of when mouse hovers
    corner_radius=200,#    change corner raduis of button
    command=add_to_cart ) #and now we will add function to our button by calling def function created before



total_button = customtkinter.CTkButton(details_frame,
    text ="Total",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)

    #as  you can see i have these buttons in details_frame outside of order_detail_frame




    #           customer  detail frame
customer_detail_frame = ttk.LabelFrame(master=details_frame,
   text= "Customer Details",
   width=200,
   height=200)


#same as i did with order_detail_frame

#and the master of these 2 frames is my details frame
customer_name = customtkinter.CTkEntry(customer_detail_frame,
    placeholder_text= "Customer Name",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200) 



customer_number = customtkinter.CTkEntry(customer_detail_frame,
    placeholder_text= "Customer Number",
    width=500,
    height=60,
    font=("helvetica",24),
    text_color="#F5DD90",
    placeholder_text_color="yellow",
    corner_radius=200)

print_bill_button = customtkinter.CTkButton(details_frame, text ="Print Bill",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200 )

#now i will create a cart frame in which i will have a label cart and a listbox that i imported in starting

cart_frame = customtkinter.CTkFrame(master=root,
  width=5,
  height=5,
)


cart_label = customtkinter.CTkLabel(cart_frame,
    text ="Cart",
    font=('times new roman',30,'bold'),
  text_color='yellow',)
  
  
total_label = customtkinter.CTkLabel(cart_frame,
    text ="",
    font=('times new roman',30,'bold'),
  text_color='yellow',)


cart_listbox = CTkListbox(cart_frame,
  width=500,
  height=500,
  font=("helvetica",24))


#now i will create a bill frame in which i will have bill label and a text box which will print all bill




bill_frame = customtkinter.CTkFrame(master=root, width=200, height=50)


bill_label = customtkinter.CTkLabel(bill_frame,
    text ="Bill",
    font=('times new roman',30,'bold'),
  text_color='yellow',)




#here i created an  another frame for 3 button clear cart,save and 'exit'

cse_button_frame = customtkinter.CTkFrame(master=root, 
width=100,
height=200)



clear_button = customtkinter.CTkButton(cse_button_frame, text ="Clear Cart",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="#1B1B1E",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200)

save_button = customtkinter.CTkButton(cse_button_frame, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)



exit_button = customtkinter.CTkButton(cse_button_frame, text ="Exit",
    width =120,
    height =60,
    font=("helvetica",19),
    text_color="black",
    fg_color="yellow",
    hover_color="#c2b84e",
    corner_radius=200,
    command=exit_program)





# Creating a grid for the widgets and frames

#firt i will make columns and rows with .configure
root.columnconfigure(0,weight =1,uniform="a")
root.columnconfigure(1,weight =1,uniform="a")
root.columnconfigure(2,weight =1,uniform="a")
root.rowconfigure(0,weight =1,uniform="a")
root.rowconfigure(1,weight =2,uniform="a")
root.rowconfigure(2,weight =1,uniform="a")

#giving weight is neccessary,weight means the size of the particular column

#now that i have configured the rows and column i will use.grid to place widegets in that row .grid takes few arguments like row,column,columnspan,sticky etc

#first i will grid the frames then widgets in them
#columnspan means how much columns our widgets will take
#sticky means direction
heading_frame.grid(column=0 ,row=0,columnspan=3, sticky=tkinter.NSEW, padx=5,pady=5)
details_frame.grid(column=0 ,row=1,rowspan=2, sticky=tkinter.NSEW, padx=5,pady=5)
cart_frame.grid(column=1 ,row=1, sticky=tkinter.NSEW,padx=75,pady=20)
bill_frame.grid(column=2 ,row=1, sticky=tkinter.NSEW, padx=75,pady=20)
cse_button_frame.grid(column=1 ,row=2,columnspan=2, sticky=tkinter.NSEW,padx=5,pady=5)

#now i will place widgets in frames with same grid method

#this time I will use the frame name instead of root

heading_frame.columnconfigure(0,weight =3,)
heading_frame.columnconfigure(1,weight =1,)
heading_frame.columnconfigure(2,weight =1,)
heading_frame.columnconfigure(3,weight =1,)
heading_frame.rowconfigure(0,weight =1)

headingLabel.grid(row=0, column=0,padx=5, sticky=tkinter.EW)

enter_username.grid(row=0, column=2,padx=5)

enter_password.grid(row=0, column=3,padx=5)

login_button.grid(row=0, column=4,padx=5)

#-------------heading frame done------------------



#-----------------now i w